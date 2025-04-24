# main.py
import cv2
import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np  # 新增导入
from utils.image_processing import preprocess_ir
from utils.defect_detection import detect_hotspots
from utils.visualization import draw_defects

# 固定路径配置（无需修改）
RAW_DIR = r"D:\PVF-10_data\PVF-10\PVF_10_112x112\train\04junction box heat"
PROCESSED_DIR = os.path.join(r"D:\solar_project\data\processed", time.strftime("%Y%m%d_%H%M"))

def process_single(img_path):
    """处理单张光伏板图片（新增温度统计）"""
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ 跳过无法读取的文件: {os.path.basename(img_path)}")
        return
    
    # 处理流程
    processed = preprocess_ir(img)
    contours = detect_hotspots(processed)
    result = draw_defects(img, contours)
    
    # ------------- 新增：全局温度统计 -------------
    mean_temp = np.mean(processed)
    std_temp = np.std(processed)
    global_thresh = mean_temp + 3 * std_temp
    print(f"📊 温度统计 | 均值: {mean_temp:.1f} | 标准差: {std_temp:.1f} | 光斑阈值: {global_thresh:.1f}")
    
    # 保存结果
    filename = os.path.basename(img_path)
    output_path = os.path.join(PROCESSED_DIR, filename)
    cv2.imwrite(output_path, result)
    print(f"✅ 已处理: {filename} → 检测到 {len(contours)} 处缺陷")

# main函数保持原有逻辑不变（已自动兼容）

if __name__ == "__main__":
    # 创建保存处理结果的目录
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    print(f"💡 正在处理图像，结果将保存到：\n{PROCESSED_DIR}")
    # 遍历 RAW_DIR 下的所有文件
    for root, dirs, files in os.walk(RAW_DIR):
        for file in files:
            # 只处理常见图像格式的文件
            if file.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(root, file)
                process_single(img_path)