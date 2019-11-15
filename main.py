from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

print type(sense)
green = (0,255,0)
yellow=(255,255,0)
blue=(0,0,255)
red=(255,0,0)
white=(255,255,255)
nothing=(0,0,0)
pink=(255,105,180)

def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)
  
sense.clear()
while(true)
  {
    sense.show_letter("B")
    sleep(1)
    sense.show_letter("O",text_colour=pick_random_colour())
    sleep(1)
    sense.show_letter("R",text_colour=pick_random_colour())
    sleep(1)
    sense.show_letter("I",text_colour=pick_random_colour())
    sleep(1)
    sense.show_letter("S",text_colour=pick_random_colour())
  }


