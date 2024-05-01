from PIL import Image, ImageDraw
img = Image.new('RGB', (300, 300), color='lightcyan')
d = ImageDraw.Draw(img)
house_width = 150
house_height = 150
house_left = 0
house_top = 150

house1_width = 50
house1_height = 50

house1left = 150
house1_top = 250

house2_width = 50
house2_height = 50

house2left = 150
house2_top = 200

house3_width = 50
house3_height = 50

house3left = 200
house3_top = 250
d.rectangle([(house_left, house_top), (house_left + house_width, house_top + house_height)], fill='green')
d.rectangle([(house1left, house1_top), (house1left + house1_width, house1_top + house1_height)], fill='red')
d.rectangle([(house2left, house2_top), (house2left + house2_width, house2_top + house2_height)], fill='red')
d.rectangle([(house3left, house3_top), (house3left + house3_width, house3_top + house3_height)], fill='red')

roof_top = house_top - 50
d.polygon([(house_left, house_top), (house_left + house_width // 2, roof_top), (house_left + house_width, house_top)], fill='blue')

d.arc([(10, 70), (50, 128)], start=0, end=150, fill='black', width=2)

d.line([(house_left + house_width // 1, roof_top), (house_left + house_width // 1, roof_top + 50)], fill='black', width=2)
d.line([(house_left + house_width // 1, roof_top), (house_left + house_width // 1 + 25 , roof_top - 30)], fill='black', width=2)
d.line([(house_left + house_width // 1, roof_top), (house_left + house_width // 1 - 25, roof_top - 30)], fill='black', width=2)


d.ellipse([(200, 10), (300, 100)], fill='yellow')

img.save('house.png')