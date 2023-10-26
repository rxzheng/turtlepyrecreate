from PIL import Image
import sys
sys.stdout = open("hexifier.txt", "w")
# REPLACE IMGPATH WITH THE IMAGE'S PATH
img = Image.open('/Users/richardzheng/Documents/GitHub/turtlepyrecreate/hangingRockImage.jpg')

#RGB
rgb_img = img.convert('RGB')

# Get the width and height of the image
width, height = rgb_img.size
print(str(width)+" "+str(height))

hexl = []
# LOOP THROUgH ALL PIXELS
for y in range(height):
    for x in range(width):
        #RGB of every pixel
        r, g, b = rgb_img.getpixel((x, y))

        #RGB to HEX
        hex_code = '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)

        # Print the hex code
        hexl.append(hex_code)
import sys
sys.stdout = open("hexifier.txt", "w")
for i in hexl:
  print(i+" ", end = '')