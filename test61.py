import cv2
import os

# Load the video file
video_path = "C:/Users/Florian/Downloads/videoplayback.mp4"
cap = cv2.VideoCapture(video_path)

# Create a directory to save the frames
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_filename = f'{output_dir}/frame_{frame_number:04d}.jpg'
    cv2.imwrite(frame_filename, frame)
    frame_number += 1

cap.release()



          
        