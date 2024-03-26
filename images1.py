import sys

from PIL import Image

Image = []

for arg in sys.argv:
    image =  Image.open(arg)
    Image.append(image)

Image[0].save(
    "image.gif", save_all=True, append_images=Image[1:], loop=0, duration=1000
)