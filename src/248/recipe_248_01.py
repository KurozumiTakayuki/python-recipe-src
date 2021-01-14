# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image

image = Image.open("pillow_sample.jpg")
new_image1 = image.rotate(45)
new_image1.save("pillow_rotate1.jpg")
new_image2 = image.rotate(45, expand=True)
new_image2.save("pillow_rotate2.jpg")
