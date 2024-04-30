import zipfile

zp = zipfile.ZipFile("C:\\Users\\fpa50\\Downloads\\channel.zip")
f = open("C:\\Users\\fpa50\\Downloads\\channel\\90052.txt","r")
filename = f.read().replace("Next nothing is ", "")
print(zp.getinfo("90052.txt").comment.decode("utf-8"), end="")

while filename:
    FILE = "C:\\Users\\fpa50\\Downloads\\channel\\"+filename+".txt"
    f = open(FILE)
    
    filename = f.read().replace("Next nothing is ", "")
    print(zp.getinfo(filename+".txt").comment.decode("utf-8"), end="")