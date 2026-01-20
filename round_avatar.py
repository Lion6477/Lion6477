# pip install pillow
from PIL import Image, ImageDraw

inp = "assets/Main_412kb.png"
out = "assets/avatar_round.png"
size = 512

img = Image.open(inp).convert("RGBA")

w, h = img.size
m = min(w, h)
img = img.crop(((w - m)//2, (h - m)//2, (w + m)//2, (h + m)//2))
img = img.resize((size, size), Image.LANCZOS)

mask = Image.new("L", (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size, size), fill=255)

res = Image.new("RGBA", (size, size), (0, 0, 0, 0))
res.paste(img, (0, 0), mask)
res.save(out)
print("Saved:", out)
