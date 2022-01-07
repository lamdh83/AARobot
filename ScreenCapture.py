import autopy
import pyautogui
import cv2
import screeninfo
#1920 x 1080
import MouseControl


def screenCapture(name='screencapture'):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'screencapture\{name}.png')



def imageShowFullScreen(img):
    screen_id = 0
    is_color = False

    # get the size of the screen
    screen = screeninfo.get_monitors()[screen_id]
    width, height = screen.width, screen.height

    # create image


    img = cv2.resize(img, (width, height))

    window_name = 'screen'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, img)
    MouseControl.mouse_move(width - 100, height - 100)
    MouseControl.mouse_left_click()
    # pyautogui.hotkey('alt', 'tab')
    cv2.waitKey(10000)
    cv2.destroyAllWindows()


def drawLine(img, size=5, frameWidth=1920, framHeight=1080):
    list = []
    x = 0
    y = 0
    w = frameWidth / size
    h = framHeight / size
    for i in range(1, size + 1):
        if i < size + 1:
            # VE LINE DUNG
            x1 = int(x + w)
            y1 = 0
            x2 = int(x + w)
            y2 = int(framHeight)
            # print(f'{x1}, {y1}')
            # print(f'{x2}, {y2}')
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # cv2.line(img, (x1, y1), (x2, y2), ((255, 0, 0)), 2)

            # VE LINE NGANG
            x3 = 0
            y3 = int(y + h)
            x4 = int(frameWidth)
            y4 = int(y + h)
            cv2.line(img, (x3, y3), (x4, y4), (255, 0, 0), 2)
            # cv2.line(img, (x1, y1), (x2, y2), ((255, 0, 0)), 2)

        if i == 1:
            a = x + int(w / 2)
            b = y + int(h / 2)
        else:
            a = int(x + int(w / 2) - w * (i - 1))
            b = y + int(h / 2)

        for j in range(1, size + 1):
            list.append((a, b))
            # print(f'{i} : {j} : {len(list)} : ({a},{b})')
            cv2.putText(img, f'{len(list)}'
                        , (a, b),
                        cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 3)
            a = int(a + w)

        x = x1
        y = y3

    return list, img



if __name__ == '__main__':
    img = cv2.imread("screencapture//screencapture.png")
    list, img = drawLine(img,6,1920, 1080)
    imageShowFullScreen(img)

