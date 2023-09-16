本项目基于https://github.com/lukas-blecher/LaTeX-OCR

其项目的webui不太好用，本项目为重写为复制截图、直接在网页粘贴的功能，而不是需要先下载存储起来，更加便捷

# 启动方式

## 1 启动ocr模型 
默认8502端口，建议看https://github.com/lukas-blecher/LaTeX-OCR 文档，使用docker启动，很方便

或者可以直接运行下面的代码，把docker镜像后台运行

docker pull lukasblecher/pix2tex:api

docker run --rm -d -p 8502:8502 lukasblecher/pix2tex:api


## 2 启动webui 
直接本地启动，默认8501端口


# to do
* 优化ui界面
* 发现图片大小越大，识别的准确率越高，后面需要改善一下，让输入模型前图片自动放大一些
