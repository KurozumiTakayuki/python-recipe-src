# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image

image = Image.open('pillow_sample.jpg')
new_image = image.resize((400, 200))
new_image.save('pillow_resize1.jpg')
