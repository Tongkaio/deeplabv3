"""修改数据集的类别标签。

数据集分三类：
1) A*: 条纹塑料布, 类别1
2) B*: 绿色防尘网, 类别2
3) C*: 黑色防晒网, 类别3
"""
import os
import numpy as np
from PIL import Image
from tqdm import tqdm

def voc_cmap(N=256, normalized=False):
    def bitget(byteval, idx):
        return ((byteval & (1 << idx)) != 0)

    dtype = 'float32' if normalized else 'uint8'
    cmap = np.zeros((N, 3), dtype=dtype)
    for i in range(N):
        r = g = b = 0
        c = i
        for j in range(8):
            r = r | (bitget(c, 0) << 7-j)
            g = g | (bitget(c, 1) << 7-j)
            b = b | (bitget(c, 2) << 7-j)
            c = c >> 3

        cmap[i] = np.array([r, g, b])

    cmap = cmap/255 if normalized else cmap
    return cmap

def letter_to_number(letter):
    """将字母 A~Z 转换为 1~26"""
    letter = letter.upper()   # 确保处理的是大写字母
    if 'A' <= letter <= 'Z':  # 确保是字母
        return ord(letter) - ord('A') + 1
    else:
        raise ValueError("Input must be a letter between A and Z")

if __name__ == '__main__':
    input_folder = 'datasets/data/VOC_GroundCover/SegmentationClass'
    output_folder = 'datasets/data/VOC_GroundCover/SegmentationClass_M'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]  # 获取文件夹中的所有图像文件
    
    cmap = voc_cmap()

    for image_file in tqdm(image_files, desc="Processing images", unit="image"):
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        pixels = image.load()  # 转换为 numpy 数组以便进行像素级别操作
        
        num = letter_to_number(image_file[0])

        image = np.array(image)
        image[image != 0] = num
        image = Image.fromarray(image.astype(np.uint8), mode='P')
        image.putpalette(cmap.astype(np.uint8).flatten())

        output_image_path = os.path.join(output_folder, image_file)
        image.save(output_image_path)
