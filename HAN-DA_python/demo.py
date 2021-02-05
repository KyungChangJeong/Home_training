import cv2
import mediapipe as mp
import math
import time
import keyboard

#==================================
pose_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
action_status = True
action_count = 0
times=10
#==================================

def is_turtleneck(ear, shoulder):
    print(round(ear,2), round(shoulder,2))
    turtleneck = shoulder * 0.19
    if shoulder - turtleneck < ear:
        print("거북목 아님")
    else:
        print("거북목 의심해보시길...")
        
def is_leg(hip_l, hip_r, ankle_l, ankle_r):
    global action_count
    global action_status
    leg_angle = get_angle_v4(ankle_l, hip_l, hip_r, ankle_r)
    print("다리 각도 {0}".format(round(leg_angle, 2)))
    if leg_angle > 90: #운동중
        action_status = False
    elif leg_angle < 30: #쉬는 중
        print("쉬는 중")
        if action_status == False:
            action_count += 1
            print("action1")
            action_status = True
    else: #운동 대충
        print("다리 더 올리기")

def is_pushup(shoulder_l, shoulder_r, elbow_l, elbow_r, wrist_l, wrist_r, hip_l, hip_r, ankle_l, ankle_r):
    global action_count
    global action_status
    l_elbow_angle = get_angle_v3(wrist_l, elbow_l, shoulder_l)
    r_elbow_angle = get_angle_v3(wrist_r, elbow_r, shoulder_r)
    l_body_angle = get_angle_v3(shoulder_l, hip_l, ankle_l)
    r_body_angle = get_angle_v3(shoulder_r, hip_r, ankle_r)
    elbow_angle = (l_elbow_angle + r_elbow_angle) / 2
    body_angle = (l_body_angle + r_body_angle) / 2
    print("팔꿈치 각도 {0}".format(round(elbow_angle,2)))
    print("몸 각도 {0}".format(round(body_angle,2)))
    if 60 < elbow_angle and 160 < body_angle < 200:
        print("이건 인정해줄게 버텨보던가 ㅋ")
        action_status = False
    elif elbow_angle < 30:
        print("쉬는 중")
        if action_status == False:
            action_count += 1
            print("action1")
            action_status = True
    else:
        if 60 < elbow_angle and body_angle < 160:
            print("어깨 아작나기싫으면 엉덩이 내려라")
        elif 60 < elbow_angle and 200 < body_angle:
            print("엉덩이 들어올려라 허리나간다")
        elif elbow_angle < 60:
            print("더 내려가라")
        elif elbow_angle < 60 and body_angle < 160:
            print("더 내려가고 엉덩이 내려라 팔굽 하기싫으면 지금 그만두던가")
        elif elbow_angle < 60 and 200 < body_angle:
            print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

def is_squat(shoulder_l, shoulder_r, hip_l, hip_r, knee_l, knee_r, ankle_l, ankle_r):
    global action_status
    global action_count
    l_knee_angle = get_angle_v3(hip_l, knee_l, ankle_l)
    l_hip_angle = get_angle_v3(knee_l, hip_l, shoulder_l)
    r_knee_angle = get_angle_v3(hip_r, knee_r, ankle_r)
    r_hip_angle = get_angle_v3(knee_r, hip_r, shoulder_r)
    knee_angle = (l_knee_angle + r_knee_angle) / 2
    hip_angle = (l_hip_angle + r_hip_angle) / 2
    print("무릎 각도 {0} | 엉덩이 각도 {1}".format(round(knee_angle,2), round(hip_angle,2)))
    # 정확한 숫자 수정 필요
    if 165 < knee_angle and 165 < hip_angle:
        print("얘 지금 운동안하고 쉰다 ㅋㅋㄹㅃㅃ")
        if action_status == False:
            action_count += 1
            print("action1")
            action_status = True
    elif 70 < knee_angle < 130 and  80 < hip_angle < 140:
        print("굳")
        action_status = False
    else:
        if knee_angle < 70 or 130 < knee_angle :
            print("스쿼트 제대로해 발목나간다!!")
        elif hip_angle < 80 or 140 < hip_angle:
            print("스쿼트 제대로해 허리나간다!!")
    if 60 < knee_angle < 80 and  60 < hip_angle < 80:
        print("굳")
        action_status = False
    else:
        if knee_angle < 70 or 130 < knee_angle :
            print("스쿼트 제대로해 발목나간다!!")
        elif hip_angle < 80 or 140 < hip_angle:
            print("스쿼트 제대로해 허리나간다!!")
            
def get_angle_v4(p1, p2, p3, p4):
    angle = math.degrees(math.atan2(p4.y - p2.y, p4.x - p2.x) - math.atan2(p1.y - p3.y, p1.x - p3.x))
    return angle + 360 if angle < 0 else angle
def get_angle_v3(p1, p2, p3):
    angle = math.degrees(math.atan2(p3.y-p2.y, p3.x-p2.x) - math.atan2(p1.y-p2.y, p1.x-p2.x))
    return angle + 360 if angle < 0 else angle
    
    '''
    o1 = math.atan((p1.y - p2.y)/(p1.x - p2.x))
    o2 = math.atan((p3.y - p2.y)/(p3.x - p2.x))
    angle = (abs((o1-o2) * 180/math.pi))
    return angle
    '''

def get_angle_v2(p1, p2):
    x = p2.x - p1.x
    y = p2.y - p1.y
    radian = math.atan2(y, x)
    degree = radian * 180 / math.pi
    if -180 < degree < -170 or 170 < degree < 180:
        print("이사람 정면이다!!!!!!!!")
    else:
        print("이사람 사이드다!!!!!!!!!!")
def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    #웹캠으로 사용
    cap = cv2.VideoCapture(0)
    count = 0
    prevTime = time.time()
    while cap.isOpened():
        global times
        curTime = time.time()
        sec = curTime - prevTime
        prevTime = curTime
        times -= sec
        if times < 0:
            print("Alert!!!!!!!!!!운동하세요!!!!!!!")
            if keyboard.is_pressed('q'):
                times = 10
                continue
        else:
            pass

        if count % 10 == 0:
            success, image = cap.read()
            if not success:
                print("카메라가 인식되지않습니다.")
                continue
            # 이미지를 좌우 반전을 시키고 BGR형태의 이미지를 RGB로 변환하여 활용합니다.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # 해당 영역에서 입력된 이미지를 분석하여 결과값을 도출해줍니다.
            results = pose.process(image)
            try:
                for index in pose_list:
                    if results.pose_landmarks.landmark[index].visibility < 0.000000000000000001:
                        results.pose_landmarks.landmark[index].x = None
                        results.pose_landmarks.landmark[index].y = None
                        results.pose_landmarks.landmark[index].z = None
                l_shoulder = results.pose_landmarks.landmark[11]
                l_elbow = results.pose_landmarks.landmark[13]
                l_wrist = results.pose_landmarks.landmark[15]
                l_hip = results.pose_landmarks.landmark[23]
                l_knee = results.pose_landmarks.landmark[25]
                l_ankle = results.pose_landmarks.landmark[27]
                r_shoulder = results.pose_landmarks.landmark[12]
                r_elbow = results.pose_landmarks.landmark[14]
                r_wrist = results.pose_landmarks.landmark[16]
                r_hip = results.pose_landmarks.landmark[24]
                r_knee = results.pose_landmarks.landmark[26]
                r_ankle = results.pose_landmarks.landmark[28]
                #print(l_ankle)
                #is_squat(l_shoulder, r_shoulder, l_hip, r_hip, l_knee, r_knee, l_ankle, r_ankle)
                #is_leg(l_hip, r_hip, l_ankle, r_ankle)
                #is_pushup(l_shoulder, r_shoulder, l_elbow, r_elbow, l_wrist, r_wrist, l_hip, r_hip, l_ankle, r_ankle)
                l_ear = results.pose_landmarks.landmark[7].x
                l_sh = results.pose_landmarks.landmark[11].x
                is_turtleneck(l_ear, l_sh)
                '''
                #================거북목?======================
                #================정자세인지?==================
                l_sh = results.pose_landmarks.landmark[11]
                r_sh = results.pose_landmarks.landmark[12]
                get_angle_v2(l_sh, r_sh)
                #================앉아있는지?==================
                if results.pose_landmarks.landmark[23].y > 1:
                    print("이사람 앉아있다!!!!")
                else:
                    print("이사람 서있다!!!!!!!!!!")
                '''
            #except TypeError as te:
            #    print(te)
            #except AttributeError as ae:
            #    print(ae)
            except Exception as e:
                print(e)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            # 이미지에 result에 저장된 좌표에 맞게 landmark를 표시합니다.
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            cv2.imshow('MediaPipe Pose', image)
        count +=1
        # esc누르면 끝나요
        if cv2.waitKey(5) & 0xFF == 27:
            if action_count < 10:
                print("총 {0}회 스쿼트를 했습니다".format(action_count))
                print("운동좀 하세요 손에들린 치킨 내려놓고")
            if action_count > 10:
                print("총 {0}회 스쿼트를 했습니다".format(action_count))
                print("겨우 이거했다고 자만하지마세요 니가 찌운살은 아직 안빠졌어요")
            break
           
    pose.close()
    cap.release()

if __name__ == "__main__":
    main()
