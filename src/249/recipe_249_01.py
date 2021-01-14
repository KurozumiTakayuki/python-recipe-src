# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image

image = Image.open("pillow_sample.jpg")
new_image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
new_image1.save("pillow_flip1.jpg")
new_image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
new_image1.save("pillow_flip2.jpg")
