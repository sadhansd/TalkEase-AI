from PIL import Image, ImageDraw
import mediapipe as mp

# Create a blank image
width, height = 400, 400
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

# Define the color for the keypoints (e.g., red)
keypoint_color = (255, 0, 0)

# Define your hand keypoints as (x, y) coordinates
# These coordinates should be extracted from your MediaPipe results
hand_keypoints = [(200, 200), (180, 180), (220, 180), (160, 160), (240, 160)]

# Set the radius for drawing keypoints
keypoint_radius = 5

# Draw the keypoints as circles
for x, y in hand_keypoints:
    draw.ellipse([(x - keypoint_radius, y - keypoint_radius),
                  (x + keypoint_radius, y + keypoint_radius)], fill=keypoint_color, outline=None)

# Save or display the resulting image
image.show()
# image.save("hand_keypoints.png")
