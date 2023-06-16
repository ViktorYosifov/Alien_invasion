from PIL import Image

image = Image.open('ship_img.bmp')

new_width = 100
new_height = 80

resized_image = image.resize((new_width, new_height))

resized_image.save('ship_img_small.bmp')


image = Image.open('ship_img_small.bmp')
image = image.convert('RGBA')
new_width, new_height = image.size
background_color = (255, 255, 255)


for x in range(new_width):
    for y in range(new_height):
        pixel_color = image.getpixel((x,y))

        if pixel_color[:3] == background_color:
             image.putpixel((x,y), (0, 0, 0, 0))


image.save('ship_img_small.bmp')