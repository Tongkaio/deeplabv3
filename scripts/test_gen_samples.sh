#!/bin/bash

# 定义要处理的图像文件列表
IMAGES=(A021.jpg A083.jpg C166.jpg C033.jpg)

# 遍历图像文件列表
for IMG in "${IMAGES[@]}"; do
    echo "Processing $IMG..."

    # 执行语义分割
    python predict.py \
        --input datasets/data/VOC_GroundCover/JPEGImages/$IMG \
        --dataset voc_gc \
        --model deeplabv3plus_mobilenet \
        --ckpt checkpoints/best_deeplabv3plus_mobilenet_voc_gc_os16.pth \
        --save_val_results_to samples/

    # 拷贝原始图像到samples目录
    cp datasets/data/VOC_GroundCover/JPEGImages/$IMG samples/$IMG

done

echo "Processing completed!"