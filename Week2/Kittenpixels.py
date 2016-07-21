from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

im = Image.open("kitten.jpeg")
#data = im.getdata()
pixels = list(im.getdata())
index = 0
new_img=[]
#intensity = pixels[index][0] + pixels[index][1] + pixels[index][2]
while index<=50625:
    intensity = pixels[index][0] + pixels[index][1] + pixels[index][2]
    if intensity<182:
        new_img.append(darkBlue)
    elif (182 <= intensity and 364 > intensity):
        new_img.append(red)
    if (364 <= intensity and 546 > intensity):
        new_img.append(lightBlue)
    if (546 <= intensity):
        new_img.append(yellow)
    index += 1

#print(intensity)
#im.putdata()
print(new_img)
     
    
    

im.save("kitten_converted.jpg")

