import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow

import time

def hit(key):
    pyautogui.press(key)
    return

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(175, 210):
        for j in range(150, 390):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(180, 210):
        for j in range(250, 445):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # Draw the rectangle for cactus
        # for i in range(144, 215):
        #     for j in range(380, 445):
        #         data[i, j] = 84
        
        # # Draw the rectangle for birds
        # for i in range(164, 205):
        #     for j in range(250, 380):
        #         data[i, j] = 71

        # image.show()
        # break

