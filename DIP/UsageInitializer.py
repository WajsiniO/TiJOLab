from DIP.Button import Button
from DIP.Light import Light

light = Light()
light_button = Button(light)

light_button.press()