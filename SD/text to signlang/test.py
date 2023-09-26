import pickle
import cv2
import mediapipe as mp
import numpy as np

image = np.ones((600, 600, 3), dtype=np.uint8) * 255  # 255 represents white in RGB

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

data_dict = pickle.load(open('./data.pickle', 'rb'))

data = data_dict['data']


labels = data_dict['labels']


connections = data_dict['connection']

dataset = ["hello","i love you","yes","no","back","please","doubt","right","left","bye"]
text = "hello"
val = str(text.index(text))

index = labels.index(val)

landmark_points = data[index]

landmark_points = [[landmark_points[i], landmark_points[i + 1]] for i in range(0, len(landmark_points), 2)]

connection_points = connections[index]
connection_points = [[connection_points[i], connection_points[i + 1]] for i in range(0, len(connection_points), 2)]

points=[]

for landmark in landmark_points:
    x, y = int(landmark[0] * 600), int(landmark[1] * 600)
    points.append((x, y))

for point in points:
    cv2.circle(image, point, 5, (0, 0, 255), -1)

for connection in connections:
            start_point = points[connection[0]]
            end_point = points[connection[1]]
            cv2.line(image, start_point, end_point, (0, 255, 0), 2)

cv2.imshow(text, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
