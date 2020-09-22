from Client import Client
from FingerPrintService import FingerPrintService

client = Client('http://192.168.43.136:8080')
service = FingerPrintService()

print('중지 저장')
data = service.getFinger()
result = client.updateFingerprint(1, data)
print(result)

print('검지 저장')
data = service.getFinger()
result = client.updateFingerprint(2, data)
print(result)

print('엄지 저장')
data = service.getFinger()
result = client.updateFingerprint(3, data)
print(result)

print('엄지 테스트')
studentList = client.getFingerprint()
print('학생: ', studentList)

service.compareFinger(studentList)

