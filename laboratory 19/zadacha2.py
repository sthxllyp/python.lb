from PIL import Image
#def convert_to_grayscale(image_path):
#    image = Image.open(image_path)
#   grayscale_image = image.convert('L')
#    grayscale_image.save("image1.jpg")  
#   grayscale_image.show()
#def main():
#   image_path = "image1.jpg"  
#   convert_to_grayscale(image_path)
#if __name__ == "__main__":
#    main()

    
#def mirror_image(image_path):
#   image = Image.open(image_path)
#    width, height = image.size
#   mirrored_image = Image.new('RGB', (width, height))
#    for y in range(height):
#        for x in range(width):
#            pixel_color = image.getpixel((x, y))
#            mirrored_x = width - x - 1
#            mirrored_image.putpixel((mirrored_x, y), pixel_color)
#    mirrored_image.save("image1.jpg") 
#    mirrored_image.show()
#def main():
#    image_path = "image1.jpg_mirrored"  
#    mirror_image(image_path)
#if __name__ == "__main__":
#    main()

def resize_image(input_image_path, output_image_path, new_width, new_height):
    image = Image.open(input_image_path)
    resized_image = image.resize((new_width, new_height))
    resized_image.save(output_image_path)
def main():
    new_width = 800  
    new_height = 600 
    input_image_path = "image1.jpg"
    output_image_path = "image2.jpg"
    resize_image(input_image_path, output_image_path, new_width, new_height)
    print("Изображение успешно изменено и сохранено в файл image2.jpg")
if __name__ == "__main__":
    main()