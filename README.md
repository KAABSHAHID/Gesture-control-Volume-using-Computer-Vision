# Gesture-control-Volume-using-Computer-Vision
This project allows users to control the system's volume through hand gestures, using the distance between their thumb and index finger. The system captures hand gestures via a webcam and adjusts the volume in real-time using the Python libraries OpenCV and Mediapipe for hand tracking, and PyCaw to interact with the system's volume settings.

## Features  
- Hand Tracking: Uses Mediapipe to track the position of key points on the hand.  
- Volume Control: Dynamically adjusts the system volume based on the distance between the thumb and index finger.  
- Real-Time Feedback: Displays visual cues such as circles on fingertips, lines between fingers, and the current system volume percentage.
- Frame Rate: Can also show the framerate, by default it is set to 30 FPS.

## How It Works  
1. Hand Tracking Module (`HandTrackingModule.py`):  
This module detects the user's hand in a webcam feed and tracks specific landmarks (fingertips, joints) using Mediapipe’s hand detection model. It provides the coordinates of hand landmarks, which are used by the main script to perform volume adjustments.  

2. Main Script (`P1_volume.py`):  
The main script calculates the distance between the tips of the thumb and index finger, mapping this distance to a volume range. As the distance between these two fingers increases or decreases, the system volume is raised or lowered. It also provides visual feedback through OpenCV, such as a real-time volume bar, FPS display, and hand tracking annotations.

## Requirements  
- Python 3.x  
- OpenCV  
- Mediapipe  
- PyCaw  
- Numpy  
- comtypes

### Install the dependencies
To install the necessary Python libraries, run the following:
```bash
pip install opencv-python mediapipe pycaw numpy comtypes
```

## Usage
1. Clone this reppository to your local machine:
```bash
git clone https://github.com/KAABSHAHID/Gesture-control-Volume-using-Computer-Vision.git
cd Gesture-control-Volume-using-Computer-Vision
```
2. Ensure your webcam is working and run the main script to start gesture-controlled volume adjustment:
```bash
python P1_volume.py
```
3. The system will start tracking your hand through the webcam. Adjust the distance between your thumb and index finger to change the system volume:  
- Move your thumb and index finger closer to decrease the volume.  
- Move them apart to increase the volume.

And HOLA! you can control volume of your system using your fingers.  

### Key Mapping
- Press 's' to stop the program.

## Code Overview  
`HandTrackingModule.py`  
This file contains the `handDetector` class that tracks the hand and finds specific landmarks on it.  
- `findHands()`: Detects hands in the video feed and draws landmarks on the image.  
- `findPosition()`: Finds the positions of landmarks on the hand and returns a list of coordinates for each.

`P1_volume.py`    
This is the main script that integrates the hand tracking module and maps the distance between the thumb and index finger to control the system volume.  

- `vol = np.interp(length, [20, 200], [minvol, maxvol])`: Maps the distance between fingertips to the system's volume range.  
- `volume.SetMasterVolumeLevel(vol, None)`: Sets the system's master volume based on the calculated distance.  


