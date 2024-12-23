"""修改数据集的类别标签。

数据集分三类：
1) A*: 条纹塑料布, 类别1
2) B*: 绿色防尘网, 类别2
3) C*: 黑色防晒网, 类别3
"""

from PIL import Image
import os
from tqdm import tqdm

class BreakLoopException(Exception):
    pass

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

    for image_file in tqdm(image_files, desc="Processing images", unit="image"):
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        pixels = image.load()  # 转换为 numpy 数组以便进行像素级别操作
        
        num = letter_to_number(image_file[0])

        try:
            for i in range(image.width):
                for j in range(image.height):
                    if pixels[i, j] != 0 and pixels[i, j] != num:
                        pixels[i, j] = num
                    elif pixels[i, j] == num:
                        raise BreakLoopException
        except BreakLoopException:
            pass

        output_image_path = os.path.join(output_folder, image_file)
        image.save(output_image_path)
