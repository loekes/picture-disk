import os
from PIL import Image, ImageDraw

def average_color_of_frame(file_path):
    image = Image.open(file_path, 'r')
    width, height = image.size
    pixels = list(image.getdata())
    r = 0
    g = 0
    b = 0
    total_pixels = width * height
    for i in range(len(pixels)):
        r += pixels[i][0]
        g += pixels[i][1]
        b += pixels[i][2]
    r = round(r / total_pixels)
    g = round(g / total_pixels)
    b = round(b / total_pixels)
    average_color = (r, g, b, 255)
    return average_color

def process_frames(directory_path):
    colors = []
    count = 0
    for file_name in os.listdir(directory_path):
        colors.append(average_color_of_frame(directory_path + '/' + file_name))
        count += 1
        print(count)
    return colors, count

def draw_image(colors, count, scale, output):
    small_circle = 512
    big_circle = small_circle + count * scale

    image = Image.new('RGBA', (big_circle, big_circle), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    for i in range(count):
        print(i)
        bounding_box = (0 + (i * scale), 0 + (i * scale), big_circle - (i * scale), big_circle - (i * scale))
        draw.ellipse(bounding_box, fill=colors[i])
    image.save(output)

colors, count = process_frames('<path/to/frames>')
draw_image(colors, count, 5, '<path/to/output.png>')