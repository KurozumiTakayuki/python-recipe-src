# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image

image = Image.open("pillow_sample.jpg")
rect = (400, 500, 525, 625)
new_image = image.crop(rect)
new_image.save("pillow_crop.jpg")
