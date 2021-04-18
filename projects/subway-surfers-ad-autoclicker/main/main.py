from time import sleep

import PIL.ImageGrab
from pynput.mouse import Button, Controller


def main():
    sleep(7)
    rgb = PIL.ImageGrab.grab().load()[857, 579]
    while rgb != (69, 157, 44):
        rgb = PIL.ImageGrab.grab().load()[857, 579]
    mouse.position = (1001, 766)
    mouse.click(Button.left)
    sleep(38)
    mouse.position = (1780, 85)
    mouse.click(Button.left)
    sleep(1)
    mouse.position = (1190, 55)
    mouse.click(Button.left)
    sleep(1)
    mouse.position = (666, 58)
    mouse.click(Button.left)
    sleep(1)
    mouse.position = (793, 995)
    mouse.click(Button.left)
    sleep(3)
    mouse.position = (793, 995)
    mouse.click(Button.left)


mouse = Controller()
while True:
    main()
