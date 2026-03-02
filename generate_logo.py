from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('static/images', exist_ok=True)
img = Image.new('RGBA', (400,100), (31,163,108,255))
draw = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype('arial.ttf', 40)
except Exception:
    font = ImageFont.load_default()
text = 'EVShare'
# Compute text bounding box using textbbox (works with recent Pillow)
bbox = draw.textbbox((0,0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
draw.text(((400-w)/2, (100-h)/2), text, fill=(255,255,255), font=font)
img.save('static/images/logo.png')
print('Generated static/images/logo.png')
