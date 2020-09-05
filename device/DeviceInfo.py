class DeviceInfo:

    def getRoomId(self):
        try:
            f = open('./info.txt', 'r')
            line = f.readline()
            f.close()
            return line
        except:
            return None

    def setRoomId(self, roomId):
        f = open('./info.txt', 'w')
        f.write(str(roomId))
        f.close()
