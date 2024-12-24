#!/bin/bash

model="$1"
mix_ckp=""
mix_opt=""

if [ "$2" == "mix_labels" ]; then
    mix_ckp="_mix"
    mix_opt="--mix_labels"
fi

CMD="python predict.py \
    --input test \
    --dataset voc_gc \
    --model deeplabv3plus_${model} \
    --ckpt checkpoints/best_deeplabv3plus_${model}_voc_gc${mix_ckp}_os16.pth \
    --save_val_results_to test_results ${mix_opt}"

echo "Command: $CMD" 
$CMD

# 设置文件路径
val_file="datasets/data/VOC_GroundCover/ImageSets/val.txt"
output_file="test.md"

# 创建或清空输出文件
> "$output_file"

# 读取 val.txt 文件中的每一行
counter=0
html_code="<div>"

while IFS= read -r image_name; do
    # 生成对应的图片路径（jpg 和 png）
    jpg_image="${image_name}.jpg"
    png_image="${image_name}.png"
    
    # 每三个图片名称，生成一个 div 代码块
    if (( counter % 3 == 0 )) && (( counter > 0 )); then
        # 把上一个 div 代码块写入 test.md
        html_code+="</div>"
        echo "$html_code" >> "$output_file"
        # 清空 html_code 为下一个 div 代码块准备
        html_code="<div>"
    fi
    
    # 添加当前图片的 HTML 代码段
    html_code+="
    <img src='./test/$jpg_image' width='15%'>
    <img src='./test_results/$png_image' width='15%'>"

    ((counter++))
done < "$val_file"

# 将最后一批 HTML 代码写入 test.md
if [ -n "$html_code" ]; then
    html_code+="</div>"
    echo "$html_code" >> "$output_file"
fi

echo "HTML code has been written to $output_file"
