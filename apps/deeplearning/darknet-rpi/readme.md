# YOLO Costomizing
- [커스터마이징 테스트 작업 과정 문서](YOLO_Costoming.md)

# 재실 & 출입인원 감지 시스템

## 구성
- PIR을 이용한 사용자 출입자 확인 시스템
- 2대 PRI를 연동하여 저가형 출입자 확인 시스템 구축
- 재실 여부 확인용 시스템
- 안면인식 가능 여부 테스트

### 하드웨어
&nbsp; RPI, PIR <br>

### 소프트웨어
&nbsp; YOLO, Python,  <br>

### 데이터 모니터
&nbsp; 데이터 분석 : 그라파다
&nbsp; 안드로이드앱 <br>

### 시스템 구성
&nbsp; PIR, RPI, Server, Web, App<br>

### 기타 
&nbsp; 최신 사진을 서버로 보내서 App에서 확인
&nbsp; 서버에서 YOLO분석 가능 테스트

<br><br>
# RPI 3B+ install Darknet-nnpack 

## 설치 참고 
  - [darknet-nnpack](https://github.com/digitalbrain79/darknet-nnpack)<br>
  - [Raspberry pi YOLO Real-time Object Detection](http://raspberrypi4u.blogspot.com/2018/10/raspberry-pi-yolo-real-time-object.html)<br>
  - [카메라 추가 테스트](https://webnautes.tistory.com/929)<br>
  
## YOLO와 Camera 연동
  ### Test 환경<br>
  &nbsp; <img width="600" src="./images/testenv.png"></img><br>
  ### run_dc.py program flow<br>
  &nbsp; <img width="600" src="./images/flow.png"></img><br>
  
## DB 구축
  ## Server 환경
  &nbsp; ssh ID@10.10.10.10 -p 7771<br>
  &nbsp; [MySQL 설치 방법](./MySQL_Install.md)<br>
  
  
## 설치 설명 파일
  [설치&동작 설명파일 InstallRun.md](https://github.com/jeonghoonkang/BerePi/blob/master/apps/deeplearning/darknet-rpi/InstallRun.md)<br>
  [YOLO 설정파일 커스텀 custom-yolo.md](https://github.com/jeonghoonkang/BerePi/blob/master/apps/deeplearning/darknet-rpi/custom-yolo.md)<br>

## 속도 향상 방법 테스트
  [사진 크기에 따른 속도 변화](https://github.com/jeonghoonkang/BerePi/tree/master/apps/deeplearning/darknet-rpi/runtime_test/readme.md)<br>
  
#### 오류 리포트
  1. -- 정면은 잘 찾음<br>
  &nbsp; <img width="600" src="./images/error_predictions2.jpg"></img><br>
  &nbsp; -- 현재 24개월 유아는 옆모습은 못찾음<br>
  &nbsp; <img width="600" src="./images/error_predictions3.jpg"></img><br>
  &nbsp; -- 1<br>
  &nbsp; <img width="600" src="./images/error/0616_1.jpg"></img><br>
  &nbsp; -- 2<br>
  &nbsp; <img width="600" src="./images/error/0616_2.jpg"></img><br>
  &nbsp; -- 3<br>
  &nbsp; <img width="600" src="./images/error/0616_3.jpg"></img><br>
  &nbsp; -- 4<br>
  &nbsp; <img width="600" src="./images/error/0616_4.jpg"></img><br>
  &nbsp; -- 5<br>
  &nbsp; <img width="600" src="./images/error/0616_5.jpg"></img><br>
    
#### 기타 
