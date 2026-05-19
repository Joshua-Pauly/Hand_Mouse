# Hand_Mouse
<h2>Summary</h2>
This project uses a webcam and MediaPipe hand landmark detection to control the mouse and click actions via finger counts. The script detects a single hand, draws landmarks on the camera feed, counts extended fingers, and maps finger counts to mouse actions with pyautogui. There is a commented example showing how a two-finger gesture could launch an automated Selenium search.

<h2>What it does</h2>

- <b>Captures webcam frames with OpenCV.</b>
- <b>Uses MediaPipe HandLandmarker (task file model) to detect hand landmarks.</b>
- <b>Draws detected landmarks on the video feed.</b>
- <b>Counts extended/folded fingers via the count_fingers() helper.</b>
- <b>Maps finger counts to actions:</b>
  - 0 no explicit action alowing you to reposition hand on screen
  - 1 finger — left click
  - 2 fingers — right click
  - 3 fingers — middle click
  - 4 fingers — double left click
  - 5 fingers — mouse movement (moves cursor by scaled difference in hand position)
- <b>Contains a commented-out Selenium block demonstrating opening Edge and performing a Google search when right hand ponter and middle finger is crossed.</b>
- <b>Press q in frame to quit.</b>

<img width="1425" height="1106" alt="image" src="https://github.com/user-attachments/assets/8b6d745c-da36-4e16-9fae-a8e67e35fb72" />
