import requests


class Client:

    def __init__(self, URL):
        self.URL = URL

    def getRooms(self):
        return requests.get(self.URL + '/rooms')

    def getCoursesByRoomId(self, id):
        return requests.get(self.URL + '/rooms/' + str(id) + '/courses')

    def getSeatsByRoomId(self, id):
        return requests.get(self.URL + '/rooms/' + str(id) + '/seats')

    def putSeatByStudentIdAndRoomIdAndSeatNumber(self, studentId, roomId, seatNumber):
        data = {
            'studentId': studentId,
            'roomId': roomId,
            'seatNumber': seatNumber
        }
        return requests.put(self.URL + '/seats', json=data)

    def login(self, option, username, password):
        data = {
            'option': option,
            'username': username,
            'password': password
        }
        return requests.post(self.URL + '/login', json=data)

    def loginByDevice(self, option, username, password):
        data = {
            'option': option,
            'username': username,
            'birthday': password
        }
        return requests.post(self.URL + '/devicelogin', json=data)

    def getFingerprint(self):
        fingerprintList = requests.get(self.URL + '/students/fingerprint').json()
        notNoneFingerprintList = []
        for elem in fingerprintList:
            if elem['fingerprint'] is not None:
                notNoneFingerprintList.append(elem)
        return notNoneFingerprintList

    def updateFingerprint(self, studentId, fingerprint):
        data = {
            'fingerprint': str(fingerprint)
        }
        return requests.put(self.URL + '/students/' + str(studentId) + '/fingerprint', json=data)

    def postAttendance(self, studentId, courseId):
        data = {
            "attendance": 1
        }
        return requests.post(self.URL + '/students/' + str(studentId) + '/courses/' +
                             str(courseId) + '/attendances', json=data)


if __name__ == '__main__':
    client = Client('http://localhost:8080')
    result = client.getCoursesByRoomId(1)
    print(result)
    print(result.json())
    print(str(result.json()[0]['id']))
    # fingerprint = client.getFingerprint()
    # print(fingerprint)
