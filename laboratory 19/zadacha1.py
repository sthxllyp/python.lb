from PIL import Image
def calculate_average_color(image):
    width, height = image.size
    pixels = image.load()
    total_r = total_g = total_b = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            total_r += r
            total_g += g
            total_b += b
    num_pixels = width * height
    avg_r = total_r // num_pixels
    avg_g = total_g // num_pixels
    avg_b = total_b // num_pixels
    return avg_r, avg_g, avg_b
def display_average_color(avg_r, avg_g, avg_b):
    print(f"Average color (R G B): {avg_r} {avg_g} {avg_b}")
    avg_color_image = Image.new('RGB', (100, 100), (avg_r, avg_g, avg_b))
    avg_color_image.show()
def main():
    image_path = "image1.jpg"  
    image = Image.open(image_path)
    avg_r, avg_g, avg_b = calculate_average_color(image)
    display_average_color(avg_r, avg_g, avg_b)
if __name__ == "__main__":
    main()