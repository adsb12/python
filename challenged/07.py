from PIL import Image

def result(img1):
    result = ""
    
    for x in range(0,img1.size[0],7):
        pixels = img1.getpixel((x,49))
        if pixels[0] == pixels[1] == pixels[2]:
            result += chr(pixels[1])
    print(result)
    
    sp_w = []
    sp_l = []
    sp_w = result.split("[")
    sp_o = sp_w[1].replace("]","")
    
    sp_l = sp_o.split(",")
    sp_s = ""
    for i in range(0,len(sp_l)):
        sp_s += chr(int(sp_l[i]))
    return print(sp_s, end="")
        
if __name__ == "__main__":
    imagefile = Image.open("C:\\Users\\fpa50\\Downloads\\oxygen.png")
    result(imagefile)