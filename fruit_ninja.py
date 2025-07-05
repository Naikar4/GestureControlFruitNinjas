import cv2
import random
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import pygame

# === INITIAL SETUP ===
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

pygame.init()
slice_sound = pygame.mixer.Sound("slice.mp3")  

sword_img = cv2.imread("sword.png", cv2.IMREAD_UNCHANGED)
fruit_imgs = [
    cv2.imread("apple.png", cv2.IMREAD_UNCHANGED),
    cv2.imread("banana.png", cv2.IMREAD_UNCHANGED),
    cv2.imread("orange.png", cv2.IMREAD_UNCHANGED)
]

if sword_img is None or any(f is None for f in fruit_imgs):
    raise Exception("Missing image files (sword.png or fruits)")

sword_img = cv2.resize(sword_img, (100, 100), interpolation=cv2.INTER_AREA)
detector = HandDetector(detectionCon=0.8, maxHands=1)

def overlay_transparent(bg, overlay, x, y):
    h, w, _ = overlay.shape
    for i in range(h):
        for j in range(w):
            if 0 <= y+i < bg.shape[0] and 0 <= x+j < bg.shape[1]:
                alpha = overlay[i, j, 3] / 255.0
                if alpha > 0:
                    bg[y+i, x+j, :3] = alpha * overlay[i, j, :3] + (1 - alpha) * bg[y+i, x+j, :3]

# === FRUIT CLASS ===
class Fruit:
    def __init__(self):
        self.img = random.choice(fruit_imgs)
        self.x = random.randint(100, 500)
        self.y = 480
        self.vx = random.randint(-3, 3)
        self.vy = -random.randint(20, 25)
        self.gravity = 0.8
        self.active = True

    def move(self):
        self.x += self.vx
        self.vy += self.gravity
        self.y += self.vy
        if self.y > 500 or self.x < 0 or self.x > 640:
            self.active = False

    def draw(self, frame):
        if self.active:
            resized = cv2.resize(self.img, (60, 60))
            overlay_transparent(frame, resized, int(self.x), int(self.y))

# === GAME STATE ===
fruits = []
last_spawn_time = time.time()
trail = []
score = 0
font = cv2.FONT_HERSHEY_SIMPLEX

# === GAME LOOP ===
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame)

    sword_pos = None
    if hands:
        lmList = hands[0]["lmList"]
        tip_x, tip_y = lmList[8][0], lmList[8][1]
        sword_pos = (tip_x, tip_y)
        overlay_transparent(frame, sword_img, tip_x - 50, tip_y - 50)

        trail.append(sword_pos)
        if len(trail) > 10:
            trail.pop(0)

    # Sharp glowing trail
    for i in range(1, len(trail)):
        cv2.line(frame, trail[i - 1], trail[i], (255, 255, 255), 6)
        cv2.line(frame, trail[i - 1], trail[i], (0, 255, 255), 2)

    # Spawn fruits
    if time.time() - last_spawn_time > 1.3:
        fruits.append(Fruit())
        last_spawn_time = time.time()

    # Update fruit state
    for fruit in fruits:
        fruit.move()
        fruit.draw(frame)

        if fruit.active and sword_pos:
            for point in trail:
                fx, fy = fruit.x + 30, fruit.y + 30
                if abs(fx - point[0]) < 35 and abs(fy - point[1]) < 35:
                    fruit.active = False
                    score += 1
                    slice_sound.play()
                    break

    fruits = [f for f in fruits if f.active]

    # Score display
    cv2.putText(frame, f"Score: {score}", (10, 40), font, 1.2, (0, 255, 255), 3)
    cv2.imshow("Fruit Ninja", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
