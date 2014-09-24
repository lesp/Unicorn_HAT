import ws2812
from time import sleep
from random import randint
ws2812.init(64)

"""
while True:
	for i in range(0,64):
	    ws2812.setPixelColor(i,128,64,64)
	    ws2812.show()
	    sleep(0.02)
	    ws2812.clear()
"""


x = randint(0,64)
y = randint(0,64)
z = randint(0,64)


while True:
	ws2812.setPixelColor(x,255,0,0)
	ws2812.show()
	sleep(0.01)
	ws2812.clear()
	x = randint(0,64)
	ws2812.setPixelColor(y,0,255,0)
	ws2812.show()
	sleep(0.01)
	ws2812.clear()
	y = randint(0,64)
	ws2812.setPixelColor(z,0,0,255)
	ws2812.show()
	sleep(0.01)
	ws2812.clear()
	z = randint(0,64)
