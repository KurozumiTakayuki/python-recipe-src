# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image

image = Image.open('pillow_sample.jpg')
image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
image2.show()
image2.save('new_sample.jpg')
