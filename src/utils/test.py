import sys
import os
import cv2
current_dir = os.path.dirname(__file__)
# 获取当前文件所在目录的父目录（即src目录）
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
# 将父目录添加到模块搜索路径
sys.path.append(parent_dir)

# 打印模块搜索路径，查看是否添加成功
print("模块搜索路径：", sys.path)

from utils.image_processing import preprocess_ir
# 获取 utils 目录绝对路径（假设项目结构不变）


# 打印当前文件路径
print(f"当前文件路径: {__file__}")
current_dir = os.path.dirname(__file__)
print(f"当前目录: {current_dir}")
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
print(f"父目录: {parent_dir}")
sys.path.append(parent_dir)
print(f"添加后的搜索路径: {sys.path}")

# 定义图像文件路径
image_path = r'd:\PVF-10_data\PVF_onlyhotspot\train\images\youtube-3_jpg.rf.2b333817c9f900a19e03ce90563ff7ff.jpg'  # 替换为实际的图像文件路径

# 检查文件是否存在
if os.path.exists(image_path):
    img = cv2.imread(image_path)
    if img is not None:
        print("调用 preprocess_ir 前，img 是否为 None:", img is None)
        processed = preprocess_ir(img)
        print("调用 preprocess_ir 后，processed 的类型:", type(processed))
    else:
        print(f"无法读取图像文件: {image_path}")
else:
    print(f"图像文件不存在: {image_path}")