from PIL import Image

img = Image.open("14.png")

img_new = Image.new('RGB',[100,100])

img_new.save("14_new.png")