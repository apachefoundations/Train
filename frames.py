import cv2
import random
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('/content/video.mp4')
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total frames:", frame_count)

random_frames = random.sample(range(frame_count), 5)

plt.figure(figsize=(15, 5))

for i, frame_number in enumerate(random_frames):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.subplot(1, 5, i+1)
        plt.imshow(frame_rgb)
        plt.title(f'Frame {frame_number}')
        plt.axis('off')

cap.release()
plt.tight_layout()
plt.show()
