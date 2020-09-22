import sys

from PyQt5.QtWidgets import *

from Client import Client
from DeviceInfo import DeviceInfo


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
        self.showLoginForUsernameAttendanceDialog()

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
        print(self.usernameEditForAttendance.text())
        print(self.birthdayEditForAttendance.text())
        result = self.client.login('student',
                                   self.usernameEditForAttendance.text(),
                                   self.birthdayEditForAttendance.text())
        if result.status_code == 200:
            self.loginForAttendanceDialog.close()
            self.showSeatsDialog(result.json()['id'])
        elif result.status_code == 500:
            self.showServerErrorMessageBox()
        else:
            self.showFailLoginMessageBox()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DeviceApp()
    sys.exit(app.exec_())
