from PIL import Image

im = Image.open("G:\my.png")
rgb_im = im.convert('RGB')
rgb_im.save("G:\colors.jpg")