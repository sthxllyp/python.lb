from PIL import Image, ImageDraw
image = Image.new('RGB', (800, 600), 'white')
draw = ImageDraw.Draw(image)
#Н
draw.line((50, 50, 50, 150), fill='red', width=5)
draw.line((50, 100, 100, 100), fill='yellow', width=5)
draw.line((100, 50, 100, 150), fill='orange', width=5)
#а
draw.line((150, 150, 200, 50), fill='green', width=5)
draw.line((200, 50, 250, 150), fill='pink', width=5)
draw.line((175, 100, 225, 100), fill='violet', width=5)
#с
draw.arc((275, 50, 375, 150), start=40, end=300, fill='orange', width=5)
#т
draw.line((350, 50, 400, 50), fill='pink', width=5)
draw.line((375, 50, 375, 150), fill='black', width=5)
#я
draw.line((450, 150, 500, 95), fill='teal', width=5)
draw.line((500, 50, 500, 150), fill='purple', width=5)
draw.arc((450, 50, 550, 100), start=90, end=-90, fill='silver', width=5)
image.save('name.png')