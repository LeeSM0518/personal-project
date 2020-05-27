# API

## Spring REST API Domain

* /login (POST)
* /students/{id}/courses (GET)
  * /students/{studentId}/courses/{courseId}/attendances (GET)
  * /students/{studentId}/courses/{courseId}/attendances (POST)
* /professor/{id}/courses (GET)
  * /professor/{professorId}/courses/{courseId}/seats (GET)
  * /professor/{professorId}/courses/{courseId}/students (GET)
  * /professor/{professorId}/courses/{courseId}/students/{studentId}/attendances (GET)
  * /professor/{professorId}/courses/{courseId}/students/{studentId}/attendances/{attendanceId} (PUT)
* /room/{roomId}/courses (GET)
  * /room/{roomId}/courses/{courseId}/seets (GET)
  * /room/{roomId}/courses/{courseId}/seets/{seetId} (PUT)

<br>

### POST /login

로그인 요청 API

* 수신 데이터

  ```json
  {
    "studentId": String,	// 학번
    "password": String		// 비밀번호
  }
  ```

* 송신 데이터

  * 성공 시

    ```json
    {
      "name": String // 이름
    }
    ```

    * `200` 코드 반환

  * 실패 시

    * 일치하는 아이디가 존재하지 않을 때 `404` 반환
    * 비밀번호가 맞지 않을 때 `401` 반환

<br>

### /students

#### GET /students/{id}/courses

자신이 수강하는 강좌 조회 API

* 수신 데이터: Integer id (학생 식별자)

* 송신 데이터

  ```json
  [
    {
      "title": String,			// 강좌이름
      "startTime": String, 	// 시작시간
      "endTime": String, 		// 종료시간
      "day": String,			 	// 강의요일
      "professor": String, 	// 수업 담당교수 성함
      "class": Integer, 	 	// 분반
      "room": {							// 강의실
        "dong": String, 			// 동
        "ho": Integer 				// 호
      }
    },
    ...
  ]
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
      "week": Integer, // 주차
      "attendance": Text // 출결
    },
    ...
  ]
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
      "attendance": String 	// 출석상태
    }
    ```

<br>

### /professor

#### GET /professor/{id}/courses

자신이 강의하는 강좌 조회 API

* 수신 데이터

  * Integer id(교수 식별자)

* 송신 데이터

  ```json
  [
    {
      "title": String,			// 강좌이름
      "startTime": String, 	// 시작시간
      "endTime": String, 		// 종료시간
      "day": String,			 	// 강의요일
      "class": Integer, 	 	// 분반
      "room": {							// 강의실
        "dong": String, 			// 동
        "ho": Integer 				// 호
      }
    },
    ...
  ]
  ```

<br>

#### GET /professor/{professorId}/courses/{courseId}/seats

자신이 강의하는 강좌의 강의실의 좌석들 조회 API

* 수신 데이터

  * Integer professorId(교수 식별자)
  * Integer courseId(강의 식별자)

* 송신 데이터

  ```json
  [
    {
      "seatNumber" : Integer,
      "status": String
    },
    ...
  ]
  ```

<br>

#### GET /professor/{professorId}/courses/{courseId}/students

자신이 강의하는 하나의 강좌의 학생들 조회 API

* 수신 데이터

  * Integer professorId(교수 식별자)
  * Integer courseId(강의 식별자)

* 송신 데이터

  ```json
  [
    {
      "studentId": String,	// 학번
      "name": String // 학생 이름
    },
    ...
  ]
  ```

<br>

#### GET /professor/{professorId}/courses/{courseId}/students/{studentId}/attendances

자신이 강의하는 하나의 강좌의 한 명의 학생의 출석들 조회 API

* 수신 데이터

  * Integer professorId(교수 식별자)
  * Integer courseId(강좌 식별자)
  * Integer studentId(학생 식별자)

* 송신 데이터

  ```json
  [
    {
      "week": Integer,			// 주차
      "attendance": String	// 출결
    },
    ...
  ]
  ```

<br>

#### PUT /professor/{professorId}/courses/{courseId}/students/{studentId}/attendances/{attendanceId}

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

<br>

### /room

#### GET /room/{roomId}/courses

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

<br>

#### GET /room/{roomId}/courses/{courseId}/seets

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

<br>

#### PUT /room/{roomId}/courses/{courseId}/seets/{seetId}

해당 강의실에서 강의하는 한 강좌의 좌석 상태 변경 API

* 수신 데이터

  * Integer roomId(강의실 식별자)

  * Integer courseId(강좌 식별자)

  * Integer seetId(좌석 식별자)

  * body

    ```json
    {
      "status": String // 좌석 상태
    }
    ```

<br>

