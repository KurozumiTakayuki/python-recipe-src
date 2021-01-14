# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image

image = Image.open("pillow_sample.jpg")
new_image = image.convert("L")
new_image.save("pillow_gray.jpg")
