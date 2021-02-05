# 🏃 한다. 🏃
### **[SW중심대학 공동해커톤]**   **```🔩+💻=한다 팀```** 

### ```홈 라이프```를 위한, ```홈 트레이닝```을 위한 웹 개발

# TECHNOLOGY
### 💻[python] 기술적인 부분
- ```mediapipe```라이브러리 사용한 모션 인식
- **세밀한 자세 교정**은 **수학적인 요소** 사용

<웹 내 classifier>
- 기술적인 노!가!다!

### 💻[json] 기술적인 부분

### requirements
```
pip install python==3.7.4
pip install mediapipe==0.8.2
pip install opencv-python==4.5.0
```
### 실행하기
```
## HAN_DA-python 코드 실행하기
python main.py

## HAN_DA-json 코드

```
# SERVICE
## 🧘작업하기🧘
### 동일 기능
- 앉은 자세 판별
- 앉은 상태에서 정자세 및 잘못된 자세 판별

### 📑 HAN-DA_python
- 앉은 자세 시간 계산
  - Timer 추가 (앉은 시간 판별 후 📢 ALERT)
- 거북목 진단
- 정면 자세 판단

### 📑 HAN-DA_json
정자세, 굽은 자세, 턱 괸 자세 판단

**바른 자세를 유지해주세요**

![image](https://user-images.githubusercontent.com/72767245/107079706-93f72300-6833-11eb-98e5-f3752f4471a8.png)


## 🤸운동하기🤸

### 동일 기능
- **[운동 횟수] COUNT**
- **[운동 자세 인식]**

### 📑 HAN-DA_Python
- ```SQUAT```: 무릎 각도와 엉덩이 각도를 내적을 통하여 연산
  - 운동 횟수 세기 
  - 잘못된 자세 알림 
- ```PUSH UP```: 팔꿈치 각도를 이용하여 연산
  - 운동 횟수 세기  
  - 잘못된 자세 알림  
- ```SIDE LEGRAISES```: 다리 각도 연산
  - 운동 횟수세기 
  - 잘못된 자세 알림 
  
### 📑 HAN-DA_json

![image](https://user-images.githubusercontent.com/72767245/107079798-b0935b00-6833-11eb-895b-c57b1d305780.png)

- ```SQUAT```
  - 운동 횟수 세기
  - 잘못된 자세 인식
- ```PUSH UP```
  - 운동 횟수 세기
  - 잘못된 자세 인식
- ```DUMBBELL CURL```
  - 운동 횟수 세기
  - 잘못된 자세 인식
