# PIL Module installed with <python3 -m pip install --upgrade Pillow>

# Open, rotate, and display an image (using the default viewer)

from PIL import Image

with Image.open("../../statics/imgs/storm_trooper.jpeg") as im:
    im.rotate(45).show()
    