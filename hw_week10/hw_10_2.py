import cv2
import numpy as np


def detect_maskY_BGR(frame):
    B = frame[:, :, 0]
    G = frame[:, :, 1]
    R = frame[:, :, 2]

    # Y (Yellow) channel을 계산합니다.
    Y = R * 0.5 + G * 0.5 - B * 0.7
    Y = Y.astype(np.uint8)

    # GaussianBlur를 적용하여 노이즈를 줄입니다.
    Y = cv2.GaussianBlur(Y, (5, 5), cv2.BORDER_DEFAULT)

    # Threshold를 적용하여 마스크를 생성합니다.
    _, mask_Y = cv2.threshold(Y, 100, 255, cv2.THRESH_BINARY)

    return mask_Y


# 1.jpg부터 4.jpg까지 이미지를 불러와 마스크를 생성하고 표시합니다.
for i in range(1, 5):
    img = cv2.imread(f'./{i}.jpg')
    mask_Y = detect_maskY_BGR(img)

    cv2.imshow(f"Original Image {i}", img)
    cv2.imshow(f"Yellow Mask {i}", mask_Y)

    cv2.waitKey(0)

cv2.destroyAllWindows()
