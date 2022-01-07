from pynput.mouse import  Button, Controller
import time

mouse = Controller()
#1920 x 1080
def mouse_left_click():
    mouse.click(Button.left, 1)

def mouse_left_doubleclick():
    mouse.click(Button.left, 2)

def mouse_right_click():
    mouse.click(Button.right, 1)

def mouse_move(x=0, y=0):
    mouse.position = (x, y)

def mouse_scroll_down(x=0, y=10):
    mouse.scroll(x, -y)

def mouse_scroll_up(x=0, y=10):
    mouse.scroll(x, y)

def mouse_scroll_right(x=10, y=0):
    mouse.scroll(x, y)

def mouse_scroll_left(x=10, y=0):
    mouse.scroll(-x, y)



if __name__ == '__main__':
    while True:
        print('scroll')
        time.sleep(2)

