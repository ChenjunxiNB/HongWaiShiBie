# image_processing.py 改进版（添加类型检查和异常处理）
import cv2
import numpy as np

def preprocess_ir(img):
    if not isinstance(img, np.ndarray):
        raise ValueError("输入必须为OpenCV图像数组（numpy.ndarray）")
    if img.size == 0:
        raise ValueError("输入图像为空")
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(gray)