# API

## Spring REST API Domain

* /login (POST)
* /students/{id}/courses (GET)
  * /students/{studentId}/courses/{courseId}/attendances (GET)
  * /students/{studentId}/courses/{courseId}/attendances (POST)
* /professors/{id}/courses (GET)
  * /professors/{professorId}/courses/{courseId}/seats (GET)
  * /professors/{professorId}/courses/{courseId}/students (GET)
  * /professors/{professorId}/courses/{courseId}/students/{studentId}/attendances (GET)
  * /professors/{professorId}/courses/{courseId}/students/{studentId}/attendances/{attendanceId} (PUT)
* /rooms/{roomId}/courses (GET)
  * /rooms/{roomId}/courses/{courseId}/seats (GET)
  * /rooms/{roomId}/courses/{courseId}/seats/{seatId} (PUT)

<br>

### POST /login

로그인 요청 API

* 수신 데이터

  ```json
  {
    "option": String,			// 교수 or 학생. ex) professor , student
    "username": String,		// 학번
    "password": String		// 비밀번호
  }
  ```

* 송신 데이터

  * 성공 시

    ```json
    {
      "id": Integer,			// 식별자
      "name": String 			// 이름
    }
```
    

* 매퍼

  * option == professor

    ```sql
    select id, name
    from professor
    where professorCode = #{username} and
    password = #{password}
    ```

  * option == student

    ```sql
    select id, name
    from student
    where studentCode = #{username} and
    password = #{password}
    ```

<br>

### /students

#### GET /students/{id}/courses

자신이 수강하는 강좌 조회 API

* 수신 데이터: Integer id (학생 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer, 					// 강의코드
      "title": String,				// 강좌이름
      "startTime": String, 		// 시작시간
      "endTime": String, 			// 종료시간
      "day": String,			 		// 강의요일
      "name": String, 				// 수업 담당교수 성함
      "_class": Integer, 	 		// 분반
      "dong": String, 			// 동
      "ho": Integer 				// 호
    },
    ...
  ]
  ```

* 매퍼

  ```sql
  select c.id, c.title, c.startTime, c.endTime, c._class, c.day, p.name,
  r.dong, r.ho
  from take t, course c, professor p, room r
  where t.studentId = #{id} and t.courseId = c.id and 
  c.professorId = p.id and c.roomId = r.id
  ```

<br>

#### GET /students/{studentId}/courses/{courseId}/attendances

자신이 수강하는 하나의 강좌의 출석 조회 API

* 수신 데이터

  * Integer studentId(학생 식별자)
  * Integer courseId(강의 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer, 			// 번호
      "week": Integer, 		// 주차
      "attendance": Text 	// 출결
    },
    ...
  ]
  ```

* 매퍼

  ```sql
  select week, attendance
  from attend
  where studentid = #{studentid} and courseId = #{courseId}
  ```

<br>

#### POST /students/{studentId}/courses/{courseId}/attendances

한 강좌를 수강하는 한 학생의 출석 생성 API

* 수신 데이터

  * Integer studentId(학생 식별자)

  * Integer courseId(강의 식별자)

  * body

    ```json
    {
      "week": Integer, 			// 주차
      "attendance": String 	// 출석상태
    }
    ```

* 매퍼

  ```sql
  insert into attend (studentId, courseId, week, attendance) values (#{studentId}, #{courseId}, #{week} , #{attendance})
  ```

<br>

### /professors

#### GET /professors/{id}/courses

자신이 강의하는 강좌 조회 API

* 수신 데이터

  * Integer id(교수 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer, 				// 강의코드
      "title": String,			// 강좌이름
      "startTime": String, 	// 시작시간
      "endTime": String, 		// 종료시간
      "day": String,			 	// 강의요일
      "_class": Integer, 	 	// 분반
      "dong": String, 			// 동
      "ho": Integer 				// 호
    },
    ...
  
  ```

* 매퍼

  ```sql
  select c.id, c.title, c.startTime, c.endTime, c.day, c.class, r.dong, r.ho
  from course c, room r
  where c.professorId = #{id} and c.roomId = r.id
  ```

<br>

#### GET /professors/{professorId}/courses/{courseId}/seats

자신이 강의하는 강좌의 강의실의 좌석들 조회 API

* 수신 데이터

  * Integer professorId(교수 식별자)
  * Integer courseId(강의 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer,
      "seatNumber" : Integer,
      "status": String
    },
    ...
  ]
  ```

* 매퍼

  ```sql
  select s.seatNumber, s.status
  from course c, seat s
  where c.id = #{courseId} and c.roomId = s.roomId
  ```

<br>

#### GET /professors/{professorId}/courses/{courseId}/students

자신이 강의하는 하나의 강좌의 학생들 조회 API

* 수신 데이터

  * Integer professorId(교수 식별자)
  * Integer courseId(강의 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer, 					// 식별자
      "studentCode": String,	// 학번
      "name": String 					// 학생 이름
    },
    ...
  ]
  ```

* 매퍼

  ```sql
  select s.id, s.studentCode, s.name
  from take t, student s
  where t.courseId = #{courseId} and t.studentId = s.id
  ```

<br>

#### GET /professors/{professorId}/courses/{courseId}/students/{studentId}/attendances

자신이 강의하는 하나의 강좌의 한 명의 학생의 출석들 조회 API

* 수신 데이터

  * Integer professorId(교수 식별자)
  * Integer courseId(강좌 식별자)
  * Integer studentId(학생 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer, 				// 식별자
      "week": Integer,			// 주차
      "attendance": String	// 출결
    },
    ...
  ]
  ```

* 매퍼

  ```sql
  select id, week, attendance
  from attend
  where studentId = #{studentId} and courseId = #{courseId}
  ```

<br>

#### PUT /professors/{professorId}/courses/{courseId}/students/{studentId}/attendances/{attendanceId}

자신이 강의하는 하나의 강좌의 한 명의 학생의 출석 변경 API

* 수신 데이터

  * Integer professorId(교수 식별자)

  * Integer courseId(강좌 식별자)

  * Integer studentId(학생 식별자)

  * body

    ```json
    {
      "attendance": String	// 출결
    }
    ```

* 매퍼

  ```sql
  update attend
  set attendance=#{attendance}
  where id=#{attendanceId}
  ```

<br>

### /rooms

#### GET /rooms/{roomId}/courses

하나의 강의실에서 강의하는 강좌들 조회 API

* 수신 데이터

  * Integer roomId(강의실 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer, 				// 강좌번호
      "title": String,			// 강좌이름
      "startTime": String, 	// 시작시간
      "endTime": String, 		// 종료시간
      "day": String,			 	// 강의요일
      "professor": String, 	// 수업 담당교수 성함
      "class": Integer, 	 	// 분반
    },
    ...
  ]
  ```

* 매퍼

  ```sql
  select c.id, c.title, c.startTime, c.endTime, c.day, c.professor, c.class
  from room r, course c
  where r.id=#{roomId} and r.id = c.roomId
  ```

<br>

#### GET /rooms/{roomId}/courses/{courseId}/seats

해당 강의실에서 강의하는 한 강좌의 좌석을 조회 API

* 수신 데이터

  * Integer roomId(강의실 식별자)
  * Integer courseId(강좌 식별자)

* 송신 데이터

  ```json
  [
    {
      "id": Integer,					// 식별자
      "seatNumber": Integer,	// 좌석 번호
      "status": String				// 좌석 상태
    },
    ...
  ]
  ```

* 매퍼

  ```sql
  select s.id, s.seatNumber, s.status
  from course c, seat s
  where c.id = #{courseId} and c.roomId = s.roomId
  ```

<br>

#### PUT /rooms/{roomId}/courses/{courseId}/seats/{seatId}

해당 강의실에서 강의하는 한 강좌의 좌석 상태 변경 API

* 수신 데이터

  * Integer roomId(강의실 식별자)

  * Integer courseId(강좌 식별자)

  * Integer seatId(좌석 식별자)

  * body

    ```json
    {
      "status": String // 좌석 상태
    }
    ```

* 매퍼

  ```sql
  update seat
  set status=#{status}
  where seatId=#{seatId}
  ```

<br>

