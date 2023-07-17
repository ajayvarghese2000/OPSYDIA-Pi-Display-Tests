"""Display the Lena picture in 3 color modes."""
import time
from PIL import Image
from st7789v.interface import RaspberryPi
from st7789v import Display
import cv2


# Create a 240x320 imagle of black and white lines one pixel wide

image = [(0, 0, 0)] * 240 * 320


for x in range(0, 240, 2):
    for y in range(0, 320):
        image[x + y * 240] = (255, 0, 0)
        #image[x + y * 240+1] = (255, 0, 0)
        #image[x + y * 240+2] = (255, 0, 0)
        #image[x + y * 240+3] = (255, 0, 0)





with RaspberryPi() as rpi:
    display = Display(rpi)
    display.initialize(color_mode=666)

    # Black image of 240x320 pixels
    data = [(0, 0, 0)] * 240 * 320

    display.draw_rgb_bytes(data)

    logo = Image.open('logo.png')
    data = list(logo.convert('RGB').getdata())

    display.draw_rgb_bytes(image)