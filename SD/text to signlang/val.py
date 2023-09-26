import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Read a frame from the webcam
ret, frame = cap.read()

# Check if the frame was read successfully
if not ret:
    print("Error: Could not read a frame from the webcam.")
    cap.release()
    exit()

# Display the captured frame
cv2.imshow("Captured Image", frame)

# Save the captured frame to a file (e.g., "captured_image.jpg")
cv2.imwrite("captured_image.jpg", frame)

# Release the webcam
cap.release()

# Close any OpenCV windows when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
# Read the image
image = cv2.imread('captured_image.jpg')  # Replace 'your_image.jpg' with the path to your image

# Convert the image to RGB format
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Process the image and extract hand landmarks
results = hands.process(image_rgb)

if results.multi_hand_landmarks:
    for landmarks in results.multi_hand_landmarks:
        # Convert landmarks to pixel coordinates
        h, w, c = image.shape
        landmark_points = []
        for landmark in landmarks.landmark:
            x, y = int(landmark.x * w), int(landmark.y * h)
            landmark_points.append((x, y))

        # Draw the hand landmarks
        for point in landmark_points:
            cv2.circle(image, point, 5, (0, 255, 0), -1)  # Green circles at each landmark point

        # Draw the hand skeleton
        connections = mp_hands.HAND_CONNECTIONS
        print(connections)
        for connection in connections:
            start_point = landmark_points[connection[0]]
            end_point = landmark_points[connection[1]]
            cv2.line(image, start_point, end_point, (0, 255, 0), 2)  # Green lines connecting keypoints

# Display the image with the hand skeleton
cv2.imshow('Hand Skeleton', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
