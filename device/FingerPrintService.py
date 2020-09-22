from pyfingerprint.pyfingerprint import PyFingerprint


class FingerPrintService:
    fingerPrinter = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)

    def getFinger(self):
        try:
            if (self.fingerPrinter.verifyPassword() == False):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('지문 인식 센서 초기화 에러')
            print('에러 메시지1: ' + str(e))
            exit(1)

        try:
            print('지문 인식 대기중')
            while (self.fingerPrinter.readImage() == False):
                pass
            self.fingerPrinter.convertImage(0x01)
            finger = str(self.fingerPrinter.downloadCharacteristics(0x01))
            return finger

        except Exception as e:
            print('지문 인식 에러')
            print('에러 메시지2: ', str(e))
            exit(1)

    def compareFinger(self, studentList):
        try:
            if (self.fingerPrinter.verifyPassword() == False):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            print('지문 인식 센서 초기화 에러')
            print('에러 메시지1: ' + str(e))
            exit(1)

        try:
            print('지문 인식 대기중')
            while (self.fingerPrinter.readImage() == False):
                pass

            self.fingerPrinter.convertImage(0x01)

            for student in studentList:
                self.fingerPrinter.uploadCharacteristics(0x02, eval(student['fingerprint']))
                score = self.fingerPrinter.compareCharacteristics()
                if score > 60:
                    return student

            return None

        except Exception as e:
            print('지문 인식 에러')
            print('에러 메시지2: ', str(e))
            exit(1)
