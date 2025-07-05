# GestureControlFruitNinjas
# 🎮 GestureControlFruitNinjas

A Python-based **Fruit Ninja** style game where you slice flying fruits using **hand gestures**, powered by real-time computer vision.

---

## 🧠 Features

- Play **without keyboard or mouse**—your hand controls the slicing.
- Built with **OpenCV** and **MediaPipe** for hand tracking.
- Slice apples, bananas, and oranges with a swinging gesture.
- Realistic **sound effects** when fruits are sliced.

---

## 📁 Project Structure

GestureControlFruitNinjas/
│
├── assets/
│ ├── apple.png
│ ├── banana.png
│ ├── orange.png
│ └── sword.png # Visual “blade” following your finger
├── sounds/
│ └── slice.mp3 # Audio effect on slicing
├── fruit_ninja.py # Main game logic
└── test.py # (Optional) demo/test script

---

## 💾 Requirements

- **Python 3.7+**
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/pro
- ject/mediapipe/)
- [Pygame](https://pypi.org/project/pygame/)

Install with:

```bash
pip install opencv-python mediapipe pygame
🚀 Run the Game
1.Connect and enable your webcam.
2.In a terminal, run:
python fruit_ninja.py
3.Position your hand within the webcam's view—your index fingertip will act as the sword to slice fruits.
🎯 Gesture Control Tips
The tip of your index finger acts as the blade.

Bold, sweeping motions slice fruit mid-air.

Ensure a well-lit environment for accurate hand detection.

🎨 Customization
Add new fruits by placing PNGs in assets/ and updating the asset loader.

Tweak game difficulty: adjust fruit spawn rate and velocity within fruit_ninja.py.

Swap in new sound effects in sounds/.

🧪 Testing & Debugging
Run test.py to visualize real-time hand landmarks and debug tracking.

Use this to ensure precise fingertip detection and calibration.

🎓 License
Open-source and free for education or personal use. Modify as desired.

📌 Support & Contribution
Contributions are welcome! Please:
Fork the repo.

Create a feature branch: git checkout -b feature/new-fruit

Commit your changes.

Open a pull request.
