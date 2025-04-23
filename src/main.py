import cv2
import os
import time
from utils.image_processing import preprocess_ir
from utils.defect_detection import detect_hotspots
from utils.visualization import draw_defects

# 固定路径配置（新手无需修改路径）
RAW_DIR = r"D:\solar_project\data\raw"
PROCESSED_DIR = os.path.join(r"D:\solar_project\data\processed", time.strftime("%Y%m%d_%H%M"))

def process_single(img_path):
    """处理单张光伏板图片"""
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ 跳过无法读取的文件: {os.path.basename(img_path)}")
        return
    
    # 处理流程（与原代码一致）
    processed = preprocess_ir(img)
    contours = detect_hotspots(processed)
    result = draw_defects(img, contours)
    
    # 保存结果
    filename = os.path.basename(img_path)
    output_path = os.path.join(PROCESSED_DIR, filename)
    cv2.imwrite(output_path, result)
    print(f"✅ 已处理: {filename} → 检测到 {len(contours)} 处缺陷")

def main():
    # 自动创建结果文件夹（带时间戳）
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    
    # 获取所有光伏板图片（支持PNG/JPG）
    image_files = [f for f in os.listdir(RAW_DIR) if f.lower().endswith(('.png', '.jpg'))]
    
    # 进度提示
    print(f"▶️ 开始批量处理 {len(image_files)} 张光伏板图片...")
    
    # 批量处理
    for idx, file in enumerate(image_files, 1):
        print(f"\n--- 正在处理第 {idx}/{len(image_files)} 张 ({idx/len(image_files):.0%}) ---")
        process_single(os.path.join(RAW_DIR, file))
    
    print(f"\n🎉 全部完成！结果已保存至：{PROCESSED_DIR}")

if __name__ == "__main__":
    main()