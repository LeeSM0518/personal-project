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

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.roomId = self.deviceInfo.getRoomId()

        if self.roomId is None:
            self.showLoginDialog()
        else:
            self.showMainWindow()

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

    def showLoginDialog(self):
        self.loginDialog = QDialog(self)

        self.loginDialog.setWindowTitle('로그인')

        usernameLayout = QHBoxLayout()
        passwordLayout = QHBoxLayout()
        parentLayout = QVBoxLayout()

        description = QLabel('디바이스 설정을 해주세요(로그인은 교수만 가능)')

        usernameLabel = QLabel('아이디 : ')
        self.usernameEdit = QLineEdit(self)
        passwordLabel = QLabel('비밀번호 : ')
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        loginBtn = QPushButton('로그인')
        loginBtn.clicked.connect(self.login)

        usernameLayout.addWidget(usernameLabel)
        usernameLayout.addWidget(self.usernameEdit)
        passwordLayout.addWidget(passwordLabel)
        passwordLayout.addWidget(self.passwordEdit)

        parentLayout.addWidget(description)
        parentLayout.addLayout(usernameLayout)
        parentLayout.addLayout(passwordLayout)
        parentLayout.addWidget(loginBtn)

        self.loginDialog.setLayout(parentLayout)
        self.loginDialog.show()

    def login(self):
        result = self.client.login('professor', self.usernameEdit.text(), self.passwordEdit.text())
        if result.status_code == 200:
            self.loginDialog.close()
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

    def showServerErrorMessageBox(self):
        QMessageBox.question(self, 'Server Error', '서버 에러 발생', QMessageBox.Yes, QMessageBox.Yes)

    def showFailLoginMessageBox(self):
        QMessageBox.question(self, '로그인 실패', '아이디나 비밀번호가 잘못되었습니다.',
                             QMessageBox.Yes, QMessageBox.Yes)

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

    ''' 지문 인식 완료 후 메소드'''
    def mouseReleaseEvent(self, QMouseEvent):
        self.fingerProcessingLabel.setText('')
        self.setBeforeFingerImage()
        self.showCheckFingerMessageBox()

    def showCheckFingerMessageBox(self):
        reply = QMessageBox.question(self, '지문 인식', '지문 인식이 완료되었습니다.\n김민주 님이 맞습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            print('자리 선택 구현')

    # def showSuccessMessageBox(self):
    #     reply = QMessageBox.question(self, '', '출석이 완료되었습니다.',
    #                                  QMessageBox.Yes, QMessageBox.Yes)
    #     if reply == QMessageBox.Yes:
    #         print('yes')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DeviceApp()
    sys.exit(app.exec_())
