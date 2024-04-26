from PIL import Image, ImageDraw
width, height = 400, 200
background_color = "white"
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)
coords = {
    "Н": [(50, 0), (80, 0), (80, 150), (110, 150), (110, 0), (140, 0), (140, 200), (110, 200), (110, 50), (80, 50), (80, 200), (50, 200)],
    "а": [(50, 100), (100, 0), (150, 100), (130, 100), (110, 50), (90, 100), (70, 100), (80, 150), (120, 150)],
    "с": [(170, 50), (220, 50), (220, 150), (170, 150)],
    "т": [(240, 50), (290, 50), (290, 150), (240, 150)],
    "я": [(310, 50), (360, 50), (360, 150), (310, 150)]
}
for letter, coord in coords.items():
    draw.polygon(coord, fill="blue")
image.save("name_polygon.png")
print("Изображение успешно сохранено в файле name_polygon.png")