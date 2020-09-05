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

    def postFingerprint(self, finger):
        '''
            지문 인식 메소드

            *
        '''

    def postAttendance(self, studentId):
        '''
            출석 인증 메소드

            * 지문 인식 API로 응답받은 studentId로 출석 인증 API를 호출
        '''


if __name__ == '__main__':
    client = Client('http://localhost:8080')

    rooms = client.getRooms().json()
    roomsTexts = [rooms[i]['dong'] + '동 ' + rooms[i]['ho']  + '호' for i in range(len(rooms))]
