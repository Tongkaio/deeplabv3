环境：
```bash
# env
conda create -n deeplabv3 python=3.6

# CUDA 11.0
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=11.0 -c pytorch
```

训练：
```bash
python main.py --model deeplabv3plus_mobilenet --gpu_id 1 --crop_val --lr 0.01 --crop_size 513 --batch_size 16 --output_stride 16
```

测试：
```bash
python predict.py --input datasets/data/VOC_GroundCover/JPEGImages/C018.jpg  --dataset voc_gc --model deeplabv3plus_mobilenet --ckpt checkpoints/best_deeplabv3plus_mobilenet_voc_gc_os16.pth --save_val_results_to test_results
```

测试结果图：
<div>
<img src="./samples/A021.jpg"  width="20%">
<img src="./samples/A021.png"  width="20%">
<img src="./samples/C018.jpg"  width="20%">
<img src="./samples/C018.png"  width="20%">
</div>

<div>
<img src="./samples/A061.jpg"  width="20%">
<img src="./samples/A061.png"  width="20%">
<img src="./samples/C033.jpg"  width="20%">
<img src="./samples/C033.png"  width="20%">
</div>

<div>
<img src="./samples/A083.jpg"  width="20%">
<img src="./samples/A083.png"  width="20%">
<img src="./samples/C166.jpg"  width="20%">
<img src="./samples/C166.png"  width="20%">
</div>