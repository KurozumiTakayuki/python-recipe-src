# 実行する際はimgフォルダのpillow_sample.jpgをカレントディレクトリに配置してください。
# また、フォントパスはお使いの環境に合わせて適宜変更してください。

from PIL import Image, ImageFont, ImageDraw

image = Image.open("pillow_sample.jpg")
text = "Pythonレシピ"
color = (255, 255, 255)
font_size = 128
font = ImageFont.truetype(r"C:\Windows\Fonts\msgothic.ttc", font_size)
draw = ImageDraw.Draw(image)
draw.text((100, 100), text, font=font, fill=color)
image.save("pillow_text.jpg")
