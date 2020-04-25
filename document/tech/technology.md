# 기술 설계

## 전체 기술도

![image-20200425231255810](../../../Library/Application Support/typora-user-images/image-20200425231255810.png)

<br>

## 흐름도

### 지문 인식

![image](https://user-images.githubusercontent.com/43431081/80282050-3bdeac80-874a-11ea-8d93-a838e0cdfb57.png)

1. 사용자가 지문 인식한다.

2. 라즈베리 파이는 측정한 지문을 Flask 모듈을 통해 인터넷으로 지문 데이터를 전송한다.

3. 인터넷을 통해 Spring에게 지문 데이터가 전달된다.

4. Spring은 지문 데이터를 DB로부터 검색한다.

5. DB는 지문 데이터가 존재하면 해당 정보를 반환하고, 존재하지 않으면 지문과 일치하는 사용자가 없다는 정보를 반환한다.

6. Spring은 반환된 데이터를 인터넷을 통해 전송한다.

7. Flask는 지문 검색 결과를 수신받고 라즈베리 파이는 디스플레이에 결과를 출력한다.

<br>

### 사용자

![image](https://user-images.githubusercontent.com/43431081/80282051-3e410680-874a-11ea-87e2-68446207aa0a.png)

1. 인터넷을 통해 UI를 요청한다.
2. Vue는 요청된 UI를 생성한다. UI에 필요한 데이터들을 Spring에게 요청한다.
3. Spring은 Vue가 요청한 데이터를 DB로부터 불러온다.
4. DB는 해당 데이터들을 불러와서 반환한다.