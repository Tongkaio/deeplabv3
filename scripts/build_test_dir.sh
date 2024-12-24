#!/bin/bash

# 设置文件路径
val_file="datasets/data/VOC_GroundCover/ImageSets/val.txt"
source_dir="datasets/data/VOC_GroundCover/JPEGImages"
destination_dir="test"

# 创建目标目录（如果不存在）
mkdir -p "$destination_dir"

# 读取 val.txt 文件中的每一行
while IFS= read -r image_name; do
    # 为每个图片名称加上 .jpg 后缀
    image_file="${image_name}.jpg"
    
    # 构造源文件路径
    source_file="${source_dir}/${image_file}"
    
    # 检查源文件是否存在
    if [ -f "$source_file" ]; then
        # 拷贝文件到目标目录
        cp "$source_file" "$destination_dir"
        echo "Copied: $image_file"
    else
        echo "File not found: $image_file"
    fi
done < "$val_file"
