# API

## Spring REST API Domain

* /login (POST)
* /students/{studentId}/courses (GET)
  * /students/{studentId}/courses/{courseId}/attendances (GET)
* /professor/{professorId}/courses (GET)
  * /professor/{professorId}/courses/{courseId}/seats (GET)
  * /professor/{professorId}/courses/{courseId}/students (GET)
  * /professor/{professorId}/courses/{courseId}/students/{studentId}/attendances (GET)
  * /professor/{professorId}/courses/{courseId}/students/{studentId}/attendances/{attendanceId} (GET, PUT)
* /room/{roomId}/courses (GET)
  * /room/{roomId}/courses/{courseId}/seets (GET)
  * /room/{roomId}/courses/{courseId}/seets (PUT)

<br>

### /login

* **POST /login**
  * 수신 데이터: String id(학번), String password(비밀번호)
  * 송신 데이터
    * 성공시: 