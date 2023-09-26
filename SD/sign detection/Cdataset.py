import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

data = []
labels = []
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            # Initialize variables to keep track of the selected hand
            selected_hand_landmarks = None
            max_landmark_y = float('-inf')  # Initialize with negative infinity

            for hand_landmarks in results.multi_hand_landmarks:
                # Iterate through all detected hands and find the one with the highest landmark point
                landmark_y = hand_landmarks.landmark[0].y  # You can use any landmark point for this check

                if landmark_y > max_landmark_y:
                    max_landmark_y = landmark_y
                    selected_hand_landmarks = hand_landmarks

            # Check if a hand was selected
            if selected_hand_landmarks:
                for i in range(len(selected_hand_landmarks.landmark)):
                    x = selected_hand_landmarks.landmark[i].x
                    y = selected_hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(selected_hand_landmarks.landmark)):
                    x = selected_hand_landmarks.landmark[i].x
                    y = selected_hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)

                data.append(data_aux)
                labels.append(dir_)

f = open('data1.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()