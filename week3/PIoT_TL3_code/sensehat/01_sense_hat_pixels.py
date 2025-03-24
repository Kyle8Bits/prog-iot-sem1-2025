import time
from sense_hat import SenseHat

sense = SenseHat()
sense.show_message("Hello world")

# Show colour
r = 255
g = 0
b = 0

sense.clear((r, g, b))

# Set single pixels
sense.set_pixel(2, 2, (0, 0, 255))
time.sleep(0.2)
sense.set_pixel(4, 2, (0, 0, 255))
time.sleep(0.2)
sense.set_pixel(3, 4, (255, 255, 255))
time.sleep(0.2)
sense.set_pixel(1, 5, (255, 255, 255))
time.sleep(0.2)
sense.set_pixel(2, 6, (255, 255, 0))
time.sleep(0.2)
sense.set_pixel(3, 6, (255, 255, 0))
time.sleep(0.2)
sense.set_pixel(4, 6, (255, 255, 0))
time.sleep(0.2)
sense.set_pixel(5, 5, (0, 0, 255))
time.sleep(0.2)

# More on display
blue = (0, 0, 255)
yellow = (255, 255, 0)

while True:
  sense.show_message("Raspberry Pi is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)
