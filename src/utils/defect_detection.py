# defect_detection.py
import cv2
import numpy as np

def detect_hotspots(processed_img):
    # ----------------------------- 全局温度统计法 -----------------------------
    mean_temp = np.mean(processed_img)
    std_temp = np.std(processed_img)
    global_thresh = mean_temp + 3 * std_temp  # 光斑温度 > 均值+3σ
    
    # 全局阈值二值化
    _, binary_global = cv2.threshold(
        processed_img, global_thresh, 255, cv2.THRESH_BINARY
    )
    
    # ----------------------------- 自适应阈值法 -----------------------------
    binary_adaptive = cv2.adaptiveThreshold(
        processed_img, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 15, 3  # 调优后的参数
    )
    
    # ----------------------------- 融合检测结果 -----------------------------
    combined = cv2.bitwise_or(binary_global, binary_adaptive)
    
    # ----------------------------- 形态学优化 -----------------------------
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    closed = cv2.morphologyEx(combined, cv2.MORPH_CLOSE, kernel, iterations=2)
    
    # ----------------------------- 提取轮廓 -----------------------------
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours