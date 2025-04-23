import os
import random
import shutil

# 原始数据路径（根据你的实际位置修改）
RAW_DIR = r"D:\solar_project\data\raw"  
TRAIN_RATIO = 0.7
VAL_RATIO = 0.1

def split_dataset():
    # 创建目标路径
    splits = ['train', 'val', 'test']
    for split in splits:
        os.makedirs(os.path.join('data', split, 'images'), exist_ok=True)
        os.makedirs(os.path.join('data', split, 'labels'), exist_ok=True)

    # 获取所有图片文件
    images = [f for f in os.listdir(RAW_DIR) if f.lower().endswith(('.png', '.jpg'))]
    random.shuffle(images)

    # 计算划分点
    total = len(images)
    train_end = int(TRAIN_RATIO * total)
    val_end = train_end + int(VAL_RATIO * total)

    # 移动文件
    for i, img in enumerate(images):
        src = os.path.join(RAW_DIR, img)
        if i < train_end:
            dest = os.path.join('data', 'train', 'images', img)
        elif i < val_end:
            dest = os.path.join('data', 'val', 'images', img)
        else:
            dest = os.path.join('data', 'test', 'images', img)
        shutil.copy(src, dest)
        print(f"已分配: {img} → {dest.split('data')[-1]}")

if __name__ == "__main__":
    split_dataset()