import cv2
import numpy as np
import os
from PIL import Image

def get_downloads_path() -> str:  # abs path
    return os.path.join(os.path.expanduser("~"), 'Downloads')

def get_image_path(filename: str) -> str:
    return os.path.join(get_downloads_path(), filename)

def read_as_gray(path: str) -> np.ndarray:
    # cv2はマルチバイトのファイル名が読めない
    a = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(a, cv2.IMREAD_GRAYSCALE)

def adaptive_threshold(img: np.ndarray) -> np.ndarray:
    block_size = 11  # 領域のサイズ
    c = 2  # 平均あるいは加重平均から引かれる値
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, block_size, c)

if __name__ == '__main__':
    
    filename = 'taiko_463.png'
    # filename = '3r2_336.png'
    
    path = get_image_path(filename)
    gray = read_as_gray(path)
    # thres = adaptive_threshold(gray)
    # print(gray.shape)  # (1334, 750)
    crop = gray[400:1100, 0:750]
    h, w = crop.shape
    img = cv2.resize(crop, (h+32, w))
    y = 336
    guide = 100
    for i in range(5):
        cv2.line(img, (100, y+guide*i), (680, y+guide*i), 255, 1)
    m = int(guide / 10)
    for i in range(41):
        if i % 10:
            cv2.line(img, (100, y+m*i), (680, y+m*i), 128, 1)

    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()