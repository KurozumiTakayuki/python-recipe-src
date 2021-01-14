# 実行する際は以下から画像をダウンロードし、カレントディレクトリにpython-logo.pngという名前で配置してください。
# https://legacy.python.org/community/logos/python-powered-h-50x65.png

from PIL import Image

image = Image.open('python-logo.png')
# ファイルフォーマットの取得
print(image.format)

# ピクセル形式 ( "1", "L", "RGB", "CMYK"など)
print(image.mode)

# 画像サイズ
print(image.size)
