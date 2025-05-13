import cv2
from deepface import DeepFace
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("../outputs", exist_ok=True)

# Video path
video_path = "D:\ProtestVideo2.mp4"
cap = cv2.VideoCapture(video_path)

# CSV to log emotions
emotion_log = []

# Frame count
frame_number = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    try:
        results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = results[0]['dominant_emotion']
        print(f"Frame {frame_number}: {dominant_emotion}")

        # Save to log
        emotion_log.append({'frame': frame_number, 'emotion': dominant_emotion})

        # Draw label
        cv2.putText(frame, f"Emotion: {dominant_emotion}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    except Exception as e:
        print(f"Frame {frame_number}: Error - {e}")
        emotion_log.append({'frame': frame_number, 'emotion': 'error'})

    # Show the video
    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_number += 1

cap.release()
cv2.destroyAllWindows()

# Save emotions to CSV
df = pd.DataFrame(emotion_log)
df.to_csv("../outputs/emotion_log.csv", index=False)
print("Emotion log saved to outputs/emotion_log.csv")
