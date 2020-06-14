# 1차 UI 설계

## Mobile App

### 시작화면 (/)

![image](https://user-images.githubusercontent.com/43431081/84584371-96d57b80-ae3e-11ea-9e45-94dfeba26ca3.png)

* 클릭 시 `/login` URL로 이동

<br>

### 로그인 (/login)

![image](https://user-images.githubusercontent.com/43431081/84584408-ef0c7d80-ae3e-11ea-9ab9-13059d80f3be.png)

![image](https://user-images.githubusercontent.com/43431081/84584414-0481a780-ae3f-11ea-8e6c-0dd1a6062e1f.png)

* ID/PW validation
  * ID/PW 둘 다 한 글자 이상이여야 한다.
  * *경고 문구*
    * `ID는 반드시 한 글자 이상이여야 합니다.`
    * `PW는 반드시 한 글자 이상이여야 합니다.`
  * API 서버로 `POST /login` 요청
  * *로그인 실패 시 경고 문구*
    * `아이디나 비밀번호가 일치하지 않습니다.`
  * 로그인 성공 시 메인 화면으로 이동

<br>

### 학생

#### 메인 화면 (/student)

![image](https://user-images.githubusercontent.com/43431081/84584471-c89b1200-ae3f-11ea-84a4-a31dc7309c6e.png)

* API 서버로 `GET /students/{id}/courses` 요청
* API 서버로부터 받은 수강하는 강의 목록을 나열
  * (강의코드), 강좌이름, 시작시간, 종료시간, 강의요일, 수업 담당교수 성함, 분반, 동, 호
* 강의를 선택 시 해당 강의의 출석 현황을 보는 URL로 이동

<br>

#### 출석 현황 (/student/attendances)

<img src="https://user-images.githubusercontent.com/43431081/84584531-7f978d80-ae40-11ea-8b2b-3e82b5c9f39f.png" alt="image" style="zoom:40%;" />

* API 서버로 `GET /students/{studentId}/courses/{courseId}/attendances` 요청
* API 서버로부터 받은 출석 정보 나열
  * (번호), 주차, 출결