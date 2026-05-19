import cv2
import pyautogui
import time
import mediapipe as mp
from mediapipe.tasks.python.core.base_options import BaseOptions
from mediapipe.tasks.python import vision as mp_v
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# create HandLandmarker with model asset (task file) and VIDEO running mode
options = mp_v.HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=r"C:\Users\hp226f\PycharmProjects\PythonProject\hand_landmarker.task"),
    num_hands=1,
    min_hand_detection_confidence=0.5)

landmarker = mp_v.HandLandmarker.create_from_options(options)
finger_count = 0

def count_fingers(landmarks):
    fingers = []
    #Thumb
    fingers.append(landmarks[4].x < landmarks[3].x )
    for tip in [8, 12,16,20]:
        fingers.append(landmarks[tip].y > landmarks[tip-2].y)
    return fingers.count(False)

webcam = cv2.VideoCapture(0)
hand_pos_x, hand_pos_y = 0,0
hand_pos_x1, hand_pos_y1 = 0,0
point_pos_x, mid_pos_x = 0,0

while webcam.isOpened():
    ret, img = webcam.read()
    img - cv2.flip(img,1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    results = landmarker.detect(mp_image)

    if results.hand_landmarks:
        for handLM in results.hand_landmarks:
            finger_count = count_fingers(handLM)
            h,w,c = img.shape
            hand_pos_x1, hand_pos_y1 = handLM[0].x, handLM[0].y
            point_pos_x, mid_pos_x = handLM[8].x, handLM[12].x
            for lm in handLM:
                circle_x, circle_y = int(lm.x *w), int(lm.y *h)
                cv2.circle(img, (circle_x, circle_y), 5, (0,255,0),-1)
            cv2.putText(img, f'Fingers: {finger_count}',(10,30),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)

    cv2.imshow('test', img)
    if finger_count == 5:
        pyautogui.move((hand_pos_x- hand_pos_x1)*2000, (hand_pos_y1 - hand_pos_y)*2000)

    if finger_count == 1:
        time.sleep(0.5)
        if finger_count == 1:
            pyautogui.click(button='left')

    if finger_count == 2:
        time.sleep(0.5)
        if finger_count == 2:
            pyautogui.click(button='right')

    if finger_count == 3:
        time.sleep(0.5)
        if finger_count == 3:
            pyautogui.click(button='middle')

    if finger_count == 4:
        time.sleep(0.5)
        if finger_count == 4:
            pyautogui.click(clicks=2, button='left')

    """if finger_count == 2 and mid_pos_x < point_pos_x:
        time.sleep(2)
        if finger_count == 2 and mid_pos_x < point_pos_x:
            driver = webdriver.Edge()
            driver.get("https://www.google.com")
            time.sleep(2)
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys("San Antonio Spurs")
            search_box.send_keys(Keys.RETURN)
            """
    hand_pos_x = hand_pos_x1
    hand_pos_y = hand_pos_y1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



webcam.release()
cv2.destroyAllWindows()


