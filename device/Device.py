import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Client import Client
from DeviceInfo import DeviceInfo
from FingerPrintService import FingerPrintService
import threading


class DeviceApp(QWidget):
    fingerImage = None
    fingerLabel = None
    fingerProcessingLabel = None
    parentLayout = QVBoxLayout()
    deviceInfo = DeviceInfo()
    client = Client('http://192.168.43.136:8080')
    fingerPrinter = FingerPrintService()

    fingerFailCount = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.roomId = self.deviceInfo.getRoomId()
        result = self.client.getCoursesByRoomId(self.roomId)
        self.courseId = result.json()[0]['id']

        if self.roomId is None:
            self.showLoginForDeviceSettingDialog()
        else:
            self.showMainWindow()

    def showSeatsDialog(self, studentId):
        self.seatsDialog = QDialog(self)
        self.seatsDialog.resize(800, 430)

        blackboard = QLabel('칠판', self.seatsDialog)
        blackboard.setStyleSheet("color: white; background-color: grey;")
        font = blackboard.font()
        font.setPointSize(20)
        blackboard.setFont(font)
        blackboard.setFixedSize(600, 30)
        blackboard.move(100, 10)
        blackboard.setAlignment(Qt.AlignCenter)

        frontDoor = QLabel('앞\n문', self.seatsDialog)
        frontDoor.setStyleSheet("color: white; background-color: grey;")
        frontDoor.setFont(font)
        frontDoor.setFixedSize(30, 80)
        frontDoor.move(750, 80)
        frontDoor.setAlignment(Qt.AlignCenter)

        backDoor = QLabel('뒷\n문', self.seatsDialog)
        backDoor.setStyleSheet("color: white; background-color: grey;")
        backDoor.setFont(font)
        backDoor.setFixedSize(30, 80)
        backDoor.move(750, 300)
        backDoor.setAlignment(Qt.AlignCenter)

        windowLabel = QLabel('창\n문', self.seatsDialog)
        windowLabel.setStyleSheet("color: white; background-color: grey;")
        windowLabel.setFont(font)
        windowLabel.setFixedSize(30, 350)
        windowLabel.move(20, 40)
        windowLabel.setAlignment(Qt.AlignCenter)

        backButton = QPushButton('뒤로가기', self.seatsDialog)
        backButton.move(20, 400)
        backButton.clicked.connect(self.seatDialogBackButtonClicked)

        registerButton = QPushButton('지문 등록', self.seatsDialog)
        registerButton.move(680, 400)
        registerButton.clicked.connect(lambda ch, id=studentId: self.registerFingerprint(id))

        response = self.client.getSeatsByRoomId(self.roomId)
        if response.status_code != 200:
            self.showServerErrorMessageBox()
            return
        seatsByApi = response.json()

        self.seats = {}

        count = 0
        for k in range(4):
            for j in range(4):
                for i in range(2):
                    seatByApi = seatsByApi[count]
                    if seatByApi['reserved'] != 0:
                        seatByApi['seatNumber'] = '예약석'
                    seat = QPushButton(str(seatByApi['seatNumber']), self.seatsDialog)
                    if seat.text() == '예약석':
                        seat.setEnabled(False)
                    seat.move(150 + i * 50 + j * 130, 100 + 80 * k)
                    seat.setFixedSize(60, 30)
                    seat.clicked.connect(lambda ch, seatNum=seat.text(): self.seatButtonClicked(seatNum, studentId))
                    count += 1

        self.centerObject(self.seatsDialog)
        self.seatsDialog.show()

    def registerFingerprint(self, studentId):
        self.fingerDialog = QDialog(self)
        self.fingerDialog.resize(800, 400)
        vBox = QVBoxLayout()
        fingerProcessingLabel = QLabel('지문을 인식기에 올려주세요.\n등록 완료시,'
                                       ' 자동으로 창이 사라집니다.')
        fingerProcessingFont = fingerProcessingLabel.font()
        fingerProcessingFont.setPointSize(15)
        fingerProcessingLabel.setFont(fingerProcessingFont)
        fingerProcessingLabel.setAlignment(Qt.AlignCenter)

        fingerImage = QPixmap('./img/fingerAfter.png')
        fingerLabel = QLabel()
        fingerLabel.setPixmap(fingerImage)
        fingerLabel.setAlignment(Qt.AlignCenter)

        vBox.addWidget(fingerProcessingLabel)
        vBox.addWidget(fingerLabel)

        self.fingerDialog.setLayout(vBox)
        self.fingerDialog.show()

        threading.Thread(target=self.register, args=(str(studentId))).start()

    def register(self, studentId):
        result = self.client.updateFingerprint(studentId, self.fingerPrinter.getFinger())
        if (result.status_code != 200):
            print('실패')
        self.fingerDialog.close()

    def seatDialogBackButtonClicked(self):
        self.seatsDialog.close()

    def seatButtonClicked(self, seatNumber, studentId):
        response = self.client.putSeatByStudentIdAndRoomIdAndSeatNumber(studentId, self.roomId, seatNumber)
        if response.status_code == 200:
            self.client.postAttendance(studentId, self.courseId)
            self.showSuccessMessageBox()
            self.seatsDialog.close()
        else:
            self.showServerErrorMessageBox()

    def showMainWindow(self):
        self.setWindowTitle("출석 확인 시스템")
        background = self.palette()
        background.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(background)

        self.makeUpUI()

        self.resize(800, 480)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def centerObject(self, obj):
        qr = obj.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        obj.move(qr.topLeft())

    def makeUpUI(self):
        mark = QPixmap('./img/mark.png')
        mark = mark.scaledToWidth(300)
        markLabel = QLabel()
        markLabel.setPixmap(mark)
        markLabel.setAlignment(Qt.AlignCenter)

        mainLabel = QLabel('출석 확인 시스템', self)
        mainLabel.setAlignment(Qt.AlignCenter)
        mainLabelFont = mainLabel.font()
        mainLabelFont.setPointSize(30)
        mainLabelFont.setBold(True)
        mainLabel.setFont(mainLabelFont)

        self.fingerProcessingLabel = QLabel('화면 터치시 지문 인식이 진행됩니다')
        fingerProcessingFont = self.fingerProcessingLabel.font()
        fingerProcessingFont.setPointSize(15)
        self.fingerProcessingLabel.setFont(fingerProcessingFont)
        self.fingerProcessingLabel.setAlignment(Qt.AlignCenter)

        self.fingerImage = QPixmap('./img/fingerBefore.png')
        self.fingerLabel = QLabel('', self)
        self.fingerLabel.setPixmap(self.fingerImage)
        self.fingerLabel.setAlignment(Qt.AlignCenter)

        blankLabel = QLabel()

        self.parentLayout.addWidget(markLabel)
        self.parentLayout.addWidget(mainLabel)
        self.parentLayout.addWidget(self.fingerProcessingLabel)
        self.parentLayout.addWidget(self.fingerLabel)
        self.parentLayout.addWidget(blankLabel)

        self.setLayout(self.parentLayout)

    def showLoginForDeviceSettingDialog(self):
        self.loginForDeviceSettingDialog = QDialog(self)

        self.loginForDeviceSettingDialog.setWindowTitle('로그인')

        usernameLayout = QHBoxLayout()
        passwordLayout = QHBoxLayout()
        parentLayout = QVBoxLayout()

        description = QLabel('디바이스 설정을 해주세요(로그인은 교수만 가능)')

        usernameLabel = QLabel('아이디 : ')
        self.usernameEditForDeviceSetting = QLineEdit(self)
        passwordLabel = QLabel('비밀번호 : ')
        self.passwordEditForDeviceSetting = QLineEdit(self)
        self.passwordEditForDeviceSetting.setEchoMode(QLineEdit.Password)
        loginBtn = QPushButton('로그인')
        loginBtn.clicked.connect(self.loginForDeviceSetting)

        usernameLayout.addWidget(usernameLabel)
        usernameLayout.addWidget(self.usernameEditForDeviceSetting)
        passwordLayout.addWidget(passwordLabel)
        passwordLayout.addWidget(self.passwordEditForDeviceSetting)

        parentLayout.addWidget(description)
        parentLayout.addLayout(usernameLayout)
        parentLayout.addLayout(passwordLayout)
        parentLayout.addWidget(loginBtn)

        self.loginForDeviceSettingDialog.setLayout(parentLayout)
        self.loginForDeviceSettingDialog.show()

    def loginForDeviceSetting(self):
        result = self.client.login('professor',
                                   self.usernameEditForDeviceSetting.text(),
                                   self.passwordEditForDeviceSetting.text())
        if result.status_code == 200:
            self.loginForDeviceSettingDialog.close()
            self.showSelectRoomDialog()
        elif result.status_code == 500:
            self.showServerErrorMessageBox()
        else:
            self.showFailLoginMessageBox()

    def showSelectRoomDialog(self):
        self.roomDialog = QDialog(self)
        self.roomDialog.setWindowTitle('강의실 선택')

        result = self.client.getRooms()
        if result.status_code != 200:
            self.showServerErrorMessageBox()

        self.rooms = result.json()

        self.roomsComboBox = QComboBox(self)
        roomsTexts = [self.rooms[i]['dong'] + '동 ' + self.rooms[i]['ho'] + '호' for i in range(len(self.rooms))]

        for item in roomsTexts:
            self.roomsComboBox.addItem(item)

        parentLayout = QVBoxLayout()

        descriptionLabel = QLabel('강의실을 선택해주세요.')

        selectButton = QPushButton('선택 완료')
        selectButton.clicked.connect(self.selectRoom)

        parentLayout.addWidget(descriptionLabel)
        parentLayout.addWidget(self.roomsComboBox)
        parentLayout.addWidget(selectButton)

        self.roomDialog.setLayout(parentLayout)
        self.roomDialog.show()

    def selectRoom(self):
        index = self.roomsComboBox.currentIndex()
        self.roomId = self.rooms[index]['id']
        print(self.roomId)
        self.deviceInfo.setRoomId(self.roomId)
        self.showMainWindow()
        self.roomDialog.close()

    def showServerErrorMessageBox(self):
        QMessageBox.question(self, 'Server Error', '서버 에러 발생', QMessageBox.Yes, QMessageBox.Yes)

    def showFailLoginMessageBox(self):
        QMessageBox.question(self, '로그인 실패', '아이디나 비밀번호가 잘못되었습니다.',
                             QMessageBox.Yes, QMessageBox.No)

    def setBeforeFingerImage(self):
        self.fingerImage = QPixmap('./img/fingerBefore.png')
        self.fingerLabel.setPixmap(self.fingerImage)
        self.fingerLabel.setAlignment(Qt.AlignCenter)

    def setAfterFingerImage(self):
        self.fingerImage = QPixmap('./img/fingerAfter.png')
        self.fingerLabel.setPixmap(self.fingerImage)
        self.fingerLabel.setAlignment(Qt.AlignCenter)

    def mousePressEvent(self, QMouseEvent):
        self.fingerProcessingLabel.setText('지문 인식을 진행중 입니다')
        self.setAfterFingerImage()

    def mouseReleaseEvent(self, QMouseEvent):
        self.checkFinger()

    def checkFinger(self):
        studentList = self.client.getFingerprint()
        student = self.fingerPrinter.compareFinger(studentList)
        if student is None:
            self.showFailFingerMessageBox()
        else:
            self.showCheckFingerMessageBox(student)
        self.fingerProcessingLabel.setText('화면 터치시 지문 인식이 진행됩니다')
        self.setBeforeFingerImage()

    def showCheckFingerMessageBox(self, student):
        reply = QMessageBox.question(self, '지문 인식', '지문 인식이 완료되었습니다.\n' + student['name'] +
                                     ' 님이 맞습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            studentId = student['id']
            self.showSeatsDialog(studentId)
        elif reply == QMessageBox.No:
            self.fingerFailCount += 1
            if self.fingerFailCount == 5:
                self.showLoginForUsernameAttendanceDialog()
                self.fingerFailCount = 0

    def showFailFingerMessageBox(self):
        reply = QMessageBox.question(self, '지문 인식 실패', '지문이 등록되어 있지 않습니다.\n'
                                                       '지문 인식을 재시도 해주세요.',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        self.fingerFailCount += 1
        if reply is not None:
            if self.fingerFailCount == 5:
                self.showLoginForUsernameAttendanceDialog()
                self.fingerFailCount = 0

    def showLoginForUsernameAttendanceDialog(self):
        self.loginForUsernameAttendanceDialog = QDialog(self)

        self.loginForUsernameAttendanceDialog.setWindowTitle('로그인')

        usernameLayout = QHBoxLayout()
        passwordLayout = QHBoxLayout()
        keyLayout = QHBoxLayout()
        parentLayout = QVBoxLayout()
        menuLayout = QHBoxLayout()

        description = QLabel('출석을 위해 로그인을 해주세요.(지문인식 실패 5회)')

        usernameLabel = QLabel('학번 : ')
        self.usernameEditForAttendance = QLineEdit(self)

        for btn in range(10):
            button = QPushButton(str(btn))
            button.setFixedSize(50, 50)
            button.clicked.connect(lambda ch, num=str(btn), editText=self.usernameEditForAttendance:
                                   self.clickedNumKey(editText, num))
            keyLayout.addWidget(button)

        backButton = QPushButton('지우기')
        backButton.clicked.connect(lambda ch, editText=self.usernameEditForAttendance:
                                   self.clickedBackKey(editText))
        keyLayout.addWidget(backButton)

        loginBtn = QPushButton('확인')
        loginBtn.clicked.connect(lambda: self.showLoginForBirthdayAttendanceDialog())

        cancelBtn = QPushButton('취소')
        cancelBtn.clicked.connect(lambda ch, dialog=self.loginForUsernameAttendanceDialog:
                                  dialog.close())

        menuLayout.addWidget(loginBtn)
        menuLayout.addWidget(cancelBtn)

        usernameLayout.addWidget(usernameLabel)
        usernameLayout.addWidget(self.usernameEditForAttendance)

        parentLayout.addWidget(description)
        parentLayout.addLayout(usernameLayout)
        parentLayout.addLayout(passwordLayout)
        parentLayout.addLayout(keyLayout)
        parentLayout.addLayout(menuLayout)

        self.loginForUsernameAttendanceDialog.setLayout(parentLayout)
        self.loginForUsernameAttendanceDialog.show()

    def invisibleDialog(self, dialog):
        dialog.close()

    def showLoginForBirthdayAttendanceDialog(self):
        self.loginForBirthdayAttendanceDialog = QDialog(self)

        self.loginForBirthdayAttendanceDialog.setWindowTitle('로그인')

        usernameLayout = QHBoxLayout()
        passwordLayout = QHBoxLayout()
        keyLayout = QHBoxLayout()
        parentLayout = QVBoxLayout()
        menuLayout = QHBoxLayout()

        description = QLabel('출석을 위해 로그인을 해주세요.(지문인식 실패 5회)')

        usernameLabel = QLabel('생년월일 (주민등록번호 앞 6자) : ')
        self.birthdayEditForAttendance = QLineEdit(self)

        for btn in range(10):
            button = QPushButton(str(btn))
            button.setFixedSize(50, 50)
            button.clicked.connect(lambda ch, num=str(btn), editText=self.birthdayEditForAttendance:
                                   self.clickedNumKey(editText, num))
            keyLayout.addWidget(button)

        backButton = QPushButton('지우기')
        backButton.clicked.connect(lambda ch, editText=self.birthdayEditForAttendance:
                                   self.clickedBackKey(editText))
        keyLayout.addWidget(backButton)

        loginBtn = QPushButton('로그인')
        loginBtn.clicked.connect(self.loginForAttendance)

        cancelBtn = QPushButton('취소')
        cancelBtn.clicked.connect(lambda ch, dialog=self.loginForBirthdayAttendanceDialog:
                                  dialog.close())

        menuLayout.addWidget(loginBtn)
        menuLayout.addWidget(cancelBtn)

        usernameLayout.addWidget(usernameLabel)
        usernameLayout.addWidget(self.birthdayEditForAttendance)

        parentLayout.addWidget(description)
        parentLayout.addLayout(usernameLayout)
        parentLayout.addLayout(passwordLayout)
        parentLayout.addLayout(keyLayout)
        parentLayout.addLayout(menuLayout)

        self.loginForBirthdayAttendanceDialog.setLayout(parentLayout)
        self.loginForBirthdayAttendanceDialog.show()

    def clickedBackKey(self, editText):
        if len(editText.text()) > 0:
            result = editText.text()[:len(editText.text()) - 1]
            editText.setText(result)

    def clickedNumKey(self, editText, btn):
        result = editText.text() + str(btn)
        editText.setText(result)

    def loginForAttendance(self):
        result = self.client.loginByDevice('student',
                                           self.usernameEditForAttendance.text(),
                                           self.birthdayEditForAttendance.text())
        if result.status_code == 200:
            self.loginForUsernameAttendanceDialog.close()
            self.loginForBirthdayAttendanceDialog.close()
            self.showSeatsDialog(result.json()['id'])
        elif result.status_code == 500:
            self.showServerErrorMessageBox()
        else:
            self.showFailLoginMessageBox()

    def showSuccessMessageBox(self):
        self.fingerFailCount = 0
        reply = QMessageBox.question(self, '', '출석이 완료되었습니다.',
                                     QMessageBox.Yes, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            print('yes')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DeviceApp()
    sys.exit(app.exec_())
