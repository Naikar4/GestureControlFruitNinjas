import cv2

img = cv2.imread("sword.png", cv2.IMREAD_UNCHANGED)

if img is None:
    print("❌ sword.png not loaded.")
else:
    print("✅ sword.png loaded. Shape:", img.shape)
    cv2.imshow("Sword Test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
