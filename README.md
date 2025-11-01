<h1 align="center">Drowsiness Detection System</h1>

<p align="center">
  <b>Real-time Computer Vision System for Driver Fatigue Detection</b><br>
  Built using <b>MediaPipe FaceMesh</b>, <b>OpenCV</b>, and <b>Pygame</b> for real-time monitoring and alert generation.
</p>

<hr>

<h2>➤ Project Overview</h2>
<p>
A real-time computer vision system that monitors <b>eye activity</b> to detect driver drowsiness using
<b>MediaPipe FaceMesh</b>, <b>OpenCV</b>, and <b>Pygame</b> for alert sounds.<br>
When the driver’s eyes remain closed for a defined duration, an audible alarm is triggered to prevent accidents due to fatigue.
</p>

<hr>

<h2>➤ Features</h2>
<ul>
  <li> Real-time face and eye tracking using MediaPipe.</li>
  <li> Calculates Eye Aspect Ratio (EAR) to detect eye closure.</li>
  <li> Triggers an alert sound when drowsiness is detected.</li>
  <li> Uses webcam feed for live monitoring.</li>
  <li> Lightweight and easy to run locally with Python.</li>
</ul>

<hr>

<h2>➤ Tech Stack</h2>
<table>
<tr><th>Component</th><th>Description</th></tr>
<tr><td><b>Language</b></td><td>Python 3.x</td></tr>
<tr><td><b>Libraries</b></td><td>opencv-python, mediapipe, numpy, pygame</td></tr>
<tr><td><b>Hardware</b></td><td>Webcam</td></tr>
<tr><td><b>Platform</b></td><td>Windows / macOS / Linux</td></tr>
</table>

<hr>

<h2>➤ Installation</h2>

<ol>
  <li><b>Clone the Repository</b>
    <pre>
git clone https://github.com/Ravi6888/Drowsiness_Detection_System.git
cd Drowsiness_Detection_System
    </pre>
  </li>

  <li><b>Install Dependencies</b>
    <p>Install the required Python libraries using pip:</p>
    <pre>
pip install opencv-python mediapipe numpy pygame
    </pre>
  </li>

  <li><b>Add Alert Sound File</b>
    <p>
      Place an audio file named <code>alert.wav</code> in the same directory as the script.<br>
      This file will be played when drowsiness is detected.
    </p>
  </li>

  <li><b>Run the Program</b>
    <pre>
python drowsiness_detection.py
    </pre>
  </li>
</ol>

<hr>

<h2>➤ How It Works</h2>
<ul>
  <li> The webcam captures live video frames.</li>
  <li> MediaPipe FaceMesh identifies facial landmarks, focusing on the eyes.</li>
  <li> The Eye Aspect Ratio (EAR) is calculated using six eye landmarks.</li>
  <li> If EAR drops below <code>0.3</code> for more than 20 consecutive frames, it indicates closed eyes → triggers a drowsiness alert.</li>
  <li> Pygame plays an alert sound (<code>alert.wav</code>) and displays a warning message on screen.</li>
</ul>

<hr>

<h2>➤ Output Preview</h2>
<ul>
  <li> Green dots marking eye landmarks.</li>
  <li> Red “<b>DROWSINESS ALERT!</b>” text when fatigue is detected.</li>
  <li> Press <b>ESC</b> to exit the program.</li>
</ul>

<p align="center"><i><img width="330" height="260" alt="image" src="https://github.com/user-attachments/assets/06aa7e4a-6032-4e1e-a18e-5d9c8b3ee0bc" />
</i></p>

<hr>

<h2>➤ Configuration</h2>
<table>
<tr><th>Parameter</th><th>Description</th><th>Default</th></tr>
<tr><td>EAR_THRESHOLD</td><td>Minimum eye aspect ratio for open eyes</td><td>0.3</td></tr>
<tr><td>EAR_CONSEC_FRAMES</td><td>Frames below threshold before alert</td><td>20</td></tr>
<tr><td>alert.wav</td><td>Sound file for drowsiness warning</td><td>Required</td></tr>
</table>

<hr>

<h2>➤ Customization Ideas</h2>
<ul>
  <li> Add face orientation (head tilt) detection for more accuracy.</li>
  <li> Integrate yawning detection using mouth landmarks.</li>
  <li> Display a real-time EAR graph or fatigue score.</li>
  <li> Add SMS/email alerts using Twilio or similar APIs.</li>
  <li> Deploy on Raspberry Pi with a small display for embedded systems.</li>
</ul>

<hr>

<p align="center">
⭐ <i>If you found this project useful, consider giving it a star!</i> ⭐
</p>
