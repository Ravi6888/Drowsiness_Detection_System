# Drowsiness_Detection_System

Drowsiness Detection System

A real-time computer vision system that monitors eye activity to detect driver drowsiness using MediaPipe FaceMesh, OpenCV, and Pygame for alert sounds.

When the driver’s eyes remain closed for a defined duration, an audible alarm is triggered to prevent accidents due to fatigue.

________________________________________

	**Features**

•	Real-time face and eye tracking using MediaPipe.

•	 Calculates Eye Aspect Ratio (EAR) to detect eye closure.

•	 Triggers an alert sound when drowsiness is detected.

•	 Uses webcam feed for live monitoring.

•	 Lightweight and easy to run locally with Python.

________________________________________

	**Tech Stack**

Component	Description

Language:	Python 3.x

Libraries:	opencv-python, mediapipe, numpy, pygame

Hardware:	Webcam

Platform:	Windows / macOS / Linux

________________________________________

	**Installation**

1.	Clone the Repository

git clone https://github.com/Ravi6888/Drowsiness_Detection_System.git

cd Drowsiness_Detection_System

2.	 Install Dependencies

Install the required Python libraries using pip:

pip install opencv-python mediapipe numpy pygame 

3.	Add Alert Sound File

Place an audio file named alert.wav in the same directory as the script.

This file will be played when drowsiness is detected.

4.	Run the Program

python drowsiness_detection.py

________________________________________

	**How It Works**

1.	The webcam captures live video frames.

2.	MediaPipe FaceMesh identifies facial landmarks, focusing on the eyes.

3.	The Eye Aspect Ratio (EAR) is calculated using six eye landmarks.

4.	If the EAR drops below a threshold (0.3) for more than 20 consecutive frames,
it indicates the user’s eyes are closed → drowsiness alert is triggered.

5.	Pygame plays an alert sound (alert.wav) and displays a warning on screen.

________________________________________

	**Output Preview**

When running, the webcam window displays:

•	Green dots marking eye landmarks.

•	Red “DROWSINESS ALERT!” text when fatigue is detected.

 <img width="495" height="391" alt="image" src="https://github.com/user-attachments/assets/4d4b3caa-5f83-4771-a8fe-eab1ca3bd8f8" />


Press ESC to exit the program.

________________________________________

	**Configuration**

Parameter----------------Description----------------------------Default

EAR_THRESHOLD-------Minimum eye aspect ratio for open eyes---------0.3

EAR_CONSEC_FRAMES--------Frames below threshold before alert-------20

alert.wav----------------Sound file for drowsiness warning---------Required

________________________________________

	**Customization Ideas**

•	Add face orientation (head tilt) detection for additional accuracy.

•	Integrate yawning detection using mouth landmarks.

•	Display real-time EAR graph or fatigue score.

•	Add SMS/email alert using twilio or similar APIs.

•	Deploy on a Raspberry Pi with a small display.
