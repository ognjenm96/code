import sys

from PIL import Image

Image =[]

for arg in sys.argv:
    Image = Image.open(arg)