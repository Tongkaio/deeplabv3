import os
import random

def split_images(data_dir):
    jpeg_images_dir = os.path.join(data_dir, 'JPEGImages')
    imagesets_dir = os.path.join(data_dir, 'ImageSets')
    os.makedirs(imagesets_dir, exist_ok=True)

    # 获取图片文件名（不含后缀）
    all_images = [f[:-4] for f in os.listdir(jpeg_images_dir) if f.endswith('.jpg')]
    a_images = [f for f in all_images if f.startswith('A')]
    c_images = [f for f in all_images if f.startswith('C')]
    print(len(a_images))
    print(len(c_images))
    # 打乱文件名
    random.shuffle(a_images)
    random.shuffle(c_images)

    # 计算分割点
    a_split = int(len(a_images) * 0.7)
    b_split = int(len(c_images) * 0.7)

    # 写入文件
    train_file = os.path.join(imagesets_dir, 'train.txt')
    val_file = os.path.join(imagesets_dir, 'val.txt')

    with open(train_file, 'w') as f:
        f.writelines(f'{name}\n' for name in a_images[:a_split] + c_images[:b_split])

    with open(val_file, 'w') as f:
        f.writelines(f'{name}\n' for name in a_images[a_split:] + c_images[b_split:])

    print(f"已生成 {train_file} 和 {val_file}")


if __name__ == '__main__':
    split_images('datasets/data/VOC_GroundCover')
