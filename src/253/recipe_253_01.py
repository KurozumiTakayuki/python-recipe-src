# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。

from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open("pillow_sample.jpg")
exif = image._getexif()
for id_, value in exif.items():
    print(id_, TAGS.get(id_), value)
