from PIL import Image
import os

# 遍历 SegmentationClass 文件夹中的所有 PNG 图像
input_folder = 'datasets/data/VOC_GroundCover/black/SegmentationClass/'
output_folder = 'datasets/data/VOC_GroundCover/black/Modified_SegmentationClass/'

# 如果输出文件夹不存在，则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取文件夹中的所有图像文件
image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

for image_file in image_files:
    # 打开每张图像
    image_path = os.path.join(input_folder, image_file)
    image = Image.open(image_path)
    
    # 获取图像的调色板
    palette = image.getpalette()
    
    # 转换为 numpy 数组以便进行像素级别操作
    pixels = image.load()

    # 遍历所有像素，修改值为 1 的像素为 2
    for i in range(image.width):
        for j in range(image.height):
            if pixels[i, j] == 1:  # 如果像素值为 1
                pixels[i, j] = 2  # 修改为 2

    # 保存修改后的图像
    output_image_path = os.path.join(output_folder, image_file)
    image.save(output_image_path)

    print(f"Processed and saved: {output_image_path}")
