import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DeviceInfo import DeviceInfo
from Client import Client


class DeviceApp(QWidget):
    fingerImage = None
    fingerLabel = None
    fingerProcessingLabel = None
    parentLayout = QVBoxLayout()
    deviceInfo = DeviceInfo()
    client = Client('http://192.168.43.136:8080')
    fingerFailCount = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.roomId = self.deviceInfo.getRoomId()

        if self.roomId is None:
            self.showLoginForDeviceSettingDialog()
        else:
            self.showMainWindow()

    def showSeatsDialog(self, studentId):
        self.seatsDialog = QDialog(self)
        self.seatsDialog.resize(800, 480)
        self.centerObject(self.seatsDialog)

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
        backDoor.move(750, 350)
        backDoor.setAlignment(Qt.AlignCenter)

        windowLabel = QLabel('창\n문', self.seatsDialog)
        windowLabel.setStyleSheet("color: white; background-color: grey;")
        windowLabel.setFont(font)
        windowLabel.setFixedSize(30, 400)
        windowLabel.move(20, 40)
        windowLabel.setAlignment(Qt.AlignCenter)

        backButton = QPushButton('뒤로가기', self.seatsDialog)
        backButton.move(360, 440)
        backButton.clicked.connect(self.seatDialogBackButtonClicked)

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

        self.seatsDialog.show()

    def seatDialogBackButtonClicked(self):
        self.seatsDialog.close()

    def seatButtonClicked(self, seatNumber, studentId):
        response = self.client.putSeatByStudentIdAndRoomIdAndSeatNumber(studentId, self.roomId, seatNumber)
        if response.status_code == 200:
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

        self.fingerProcessingLabel = QLabel()
        fingerProcessingFont = self.fingerProcessingLabel.font()
        fingerProcessingFont.setPointSize(15)
        self.fingerProcessingLabel.setFont(fingerProcessingFont)
        self.fingerProcessingLabel.setAlignment(Qt.AlignCenter)

        self.fingerImage = QPixmap('./img/fingerBefore.png')
        self.fingerLabel = QLabel()
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

    ''' 지문 인식 메소드 '''

    def mousePressEvent(self, QMouseEvent):
        self.fingerProcessingLabel.setText('지문 인식을 진행중 입니다')
        self.setAfterFingerImage()
        # TODO 지문 인식의 결과로 받은 학생 번호(studentId)를 self.studentId에 저장하는 로직

    ''' 지문 인식 완료 후 메소드'''

    def mouseReleaseEvent(self, QMouseEvent):
        self.fingerProcessingLabel.setText('')
        self.setBeforeFingerImage()
        self.showCheckFingerMessageBox()

    def showCheckFingerMessageBox(self):
        reply = QMessageBox.question(self, '지문 인식', '지문 인식이 완료되었습니다.\n김민주 님이 맞습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            ''' 지문인식 완료 후 전달받은 studentId를 넘기는 로직 수정 필요 '''
            studentId = 3
            self.showSeatsDialog(studentId)
        elif reply == QMessageBox.No:
            self.fingerFailCount += 1
            if self.fingerFailCount == 5:
                self.showLoginForAttendanceDialog()
                self.fingerFailCount = 0

    def showLoginForAttendanceDialog(self):
        self.loginForAttendanceDialog = QDialog(self)

        self.loginForAttendanceDialog.setWindowTitle('로그인')

        usernameLayout = QHBoxLayout()
        passwordLayout = QHBoxLayout()
        parentLayout = QVBoxLayout()

        description = QLabel('출석을 위해 로그인을 해주세요.(지문인식 실패 5회)')

        usernameLabel = QLabel('아이디 : ')
        self.usernameEditForAttendance = QLineEdit(self)
        passwordLabel = QLabel('비밀번호 : ')
        self.passwordEditForAttendance = QLineEdit(self)
        self.passwordEditForAttendance.setEchoMode(QLineEdit.Password)
        loginBtn = QPushButton('로그인')
        loginBtn.clicked.connect(self.loginForAttendance)

        usernameLayout.addWidget(usernameLabel)
        usernameLayout.addWidget(self.usernameEditForAttendance)
        passwordLayout.addWidget(passwordLabel)
        passwordLayout.addWidget(self.passwordEditForAttendance)

        parentLayout.addWidget(description)
        parentLayout.addLayout(usernameLayout)
        parentLayout.addLayout(passwordLayout)
        parentLayout.addWidget(loginBtn)

        self.loginForAttendanceDialog.setLayout(parentLayout)
        self.loginForAttendanceDialog.show()

    def loginForAttendance(self):
        result = self.client.login('student',
                                   self.usernameEditForAttendance.text(),
                                   self.passwordEditForAttendance.text())
        if result.status_code == 200:
            self.loginForAttendanceDialog.close()
            self.showSeatsDialog(result.json()['id'])
        elif result.status_code == 500:
            self.showServerErrorMessageBox()
        else:
            self.showFailLoginMessageBox()

    def showSuccessMessageBox(self):
        reply = QMessageBox.question(self, '', '출석이 완료되었습니다.',
                                     QMessageBox.Yes, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            print('yes')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DeviceApp()
    sys.exit(app.exec_())
