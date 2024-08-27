# Squid Game Motion Detection
This project is a simple motion detection game inspired by the "Red Light, Green Light" game from the popular show Squid Game. The game uses a webcam to detect player movements during the "Red Light" phase, and if movement is detected, the game ends. The player wins if they reach the "Green Light" phase and press the designated key within the time limit.

## Features
#### 1. Webcam Integration: The game captures video input from the webcam.
#### 2. Motion Detection: Movement is detected during the "Red Light" phase using frame differencing.
#### 3. Time Limit: The game includes a countdown timer, after which the game automatically ends.
#### 4. Graphics Display: Game phases ("Red Light", "Green Light") are displayed using images loaded from a specified folder.

## Prerequisites
Ensure you have the following installed on your system:

    1. Python 3.x
    2. OpenCV (cv2) library
    3. NumPy (numpy) library

## Run Locally 
```
pip install opencv-python-headless numpy
```

## Setup

Prepare the Image Folder:

    1. Create a folder named frames in the same directory as the script.
    2. Place the following images in the folder:
        a. green.png: The image for the "Green Light" phase.
        b. red.png: The image for the "Red Light" phase.
        c. kill.png: The image displayed when the game ends due to motion detection.
        d. winner.png: The image displayed when the player wins the game.
        e. intro.png: The introductory image displayed at the beginning of the game.

## Execute the script using Python:

```sh
python squid_game.py
```

## Gameplay Instructions:

- The game starts with the introductory screen.
- During the "Green Light" phase, press the w key to indicate movement.
- During the "Red Light" phase, remain still. If any movement is detected, the game ends.
- The goal is to press the w key during the "Green Light" phase without getting caught moving during the "Red Light" phase.

## Code Explanation
- Image Loading: The images for different phases of the game are loaded from the frames folder and resized for display.
- Motion Detection: The game captures frames from the webcam and compares them to detect movement. If significant movement is detected during the "Red Light" phase, the game ends.
- Timer: The game runs with a countdown timer. If the timer reaches zero and the player has not won, the game ends.

## Customization
- Adjusting Sensitivity: Modify the maxMOVE variable to change the sensitivity of motion detection.
- Timer Duration: Change the TIMER_MAX variable to set a different countdown duration.
- Image Scaling: Adjust the fx and fy parameters in the cv2.resize() function calls to change the size of the displayed images.

## Troubleshooting
- Webcam Issues: Ensure that your webcam is properly connected and accessible. If the game cannot access the webcam, it will not start.
- Image Not Found: Make sure that the images in the frames folder are named correctly and are in a supported format (e.g., .png).
