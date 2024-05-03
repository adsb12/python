from PIL import Image

image = Image.open("11.jpg")
even = Image.new('RGB',(image.size[0],image.size[1]))

for x in range(image.size[0]):
    for y in range(image.size[1]):
        if (x+y)%2 == 0:
            even.putpixel((x,y),image.getpixel((x,y)))

even.show()
even.save('11_an.jpg')