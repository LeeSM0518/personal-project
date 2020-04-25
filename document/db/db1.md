# DB

## 요구사항

* 학생은 학번, 비밀번호, 이름, 지문 정보를 갖는다.
* 강좌는 강의 코드랑 이름, 시작 시간, 종료 시간, 강의 요일, 강의실, 담당 교수, 분반을 갖는다.
* 강의실은 강의실 번호랑 동, 호를 갖는다.
* 교수는 학번, 비밀번호, 이름을 갖는다.
* 출석부는 강좌, 주차, 출결, 학생을 갖는다.
* 한 명 이상의 학생은 한 개 이상의 강좌를 수강한다.
* 한 명 이상의 학생은 한 번 이상의 출석을 한다.
* 한 명의 교수는 한 개 이상의 강좌를 강의한다.
* 한 개의 강의실에 한 개 이상의 강좌가 할당된다.

<br>

## 명명

* **학생(student)**
  * 학번(id)
  * 비밀번호(password)
  * 이름(name)
  * 지문(fingerprint)
* **강좌(Course)**
  * 강의코드(id)
  * 이름(title)
  * 시작시간(startTime)
  * 종료시간(endTime)
  * 강의요일(day)
  * 담당교수(professorId)
  * 분반(class)
  * 강의실(roomId)
* **강의실(room)**
  * 강의실 코드(id)
  * n동(dong)
  * n호(ho)
* **교수(Professor)**
  * 학번(id)
  * 비밀번호(password)
  * 이름(name)
* **출석하다(Attend)**
  * 강좌(lectureId)
  * 주차(week)
  * 출결(check)
  * 학생(studentId)
* **수강하다(Take)**
  * 학생(studentId)
  * 강좌(courseId)

<br>

## ER 모델

![image](https://user-images.githubusercontent.com/43431081/80275362-a9bfaf80-871b-11ea-8f0a-e32497d392eb.png)

<br>

## ER 다이어그램

![image](https://user-images.githubusercontent.com/43431081/80275932-cf4eb800-871f-11ea-8b13-1e7e2b59ddcf.png)

