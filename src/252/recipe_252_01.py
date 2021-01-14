# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。
# また、以下から画像をダウンロードし、カレントディレクトリにpython-logo.pngという名前で配置してください。
# https://www.python.org/static/community_logos/python-logo-master-v3-TM.png

from PIL import Image

image = Image.open("pillow_sample.jpg")
logo = Image.open("python-logo.png")
image.paste(logo, (100, 100), logo)
image.save("pillow_paste.jpg")
