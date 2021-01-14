# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image

image = Image.open('pillow_sample.jpg')
image.thumbnail((400, 400))
image.save('pillow_resize2.jpg')
