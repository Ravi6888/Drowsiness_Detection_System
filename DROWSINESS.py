import cv2
import numpy as np
import mediapipe as mp
import pygame
import os

# EAR calculation
def calculate_ear(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

# Eye indices for MediaPipe FaceMesh
LEFT_EYE_IDX = [362, 385, 387, 263, 373, 380]
RIGHT_EYE_IDX = [33, 160, 158, 133, 153, 144]

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Thresholds
EAR_THRESHOLD = 0.3
EAR_CONSEC_FRAMES = 20
COUNTER = 0
ALERT_ON = False

# Initialize sound
pygame.init()
pygame.mixer.init()
sound_path = os.path.join(os.path.dirname(__file__), "alert.wav")

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            mesh = np.array([(int(p.x * w), int(p.y * h)) for p in landmarks.landmark])
            left_eye = mesh[LEFT_EYE_IDX]
            right_eye = mesh[RIGHT_EYE_IDX]

            left_ear = calculate_ear(left_eye)
            right_ear = calculate_ear(right_eye)
            avg_ear = (left_ear + right_ear) / 2.0

            if avg_ear < EAR_THRESHOLD:
                COUNTER += 1
                if COUNTER >= EAR_CONSEC_FRAMES and not ALERT_ON:
                    ALERT_ON = True
                    pygame.mixer.music.load(sound_path)
                    pygame.mixer.music.play()

                if ALERT_ON:
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
            else:
                COUNTER = 0
                ALERT_ON = False

            # Draw eye points
            for point in np.concatenate((left_eye, right_eye)):
                cv2.circle(frame, tuple(point), 2, (0, 255, 0), -1)

    cv2.imshow("Driver Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

# Clean up
cap.release()
face_mesh.close()
cv2.destroyAllWindows()
