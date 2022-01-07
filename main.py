# pip install playsound==1.2.2
import time

import autopy as autopy
import cv2

from playsound import playsound


import FireBaseRealTimeDB
import MouseControl
import ScreenCapture
import WebBrowserModule

import speech_recognition as sr
from pygame import mixer
from gtts import gTTS

import XuLyLenh
from MouseControl import *
from ScreenCapture import screenCapture, imageShowFullScreen, drawLine

import speech_recognition as sr

r = sr.Recognizer()



count = 0
dsToaDoFlix = []
wScr, hScr = autopy.screen.size()
x = 0
h = 350

firebase = FireBaseRealTimeDB.FireBase()
firebase.delete()

r = sr.Recognizer()
text = ""
temp = 0
import ctypes
import win32gui, win32con
import pyautogui

############# DK VOLUMN #######################

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = maxVol
volume.SetMasterVolumeLevel(vol, None)
############# DK VOLUMN #######################







def hideConsoleW():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide, win32con.SW_HIDE)


def toaDoChuot():
    list = []
    w, h = autopy.screen.size()
    scale = int(w / 1080)
    x = 700 * scale
    y = 275 * scale
    list.append((x, y))
    for index in range(0, 3):
        y = y + 225 * scale
        list.append((x, y))
    print(list)
    return list


def speak(data):
    global count

    tts = gTTS(data, tld='com.vn', lang='vi')
    tts.save(f'speech{count % 2}.mp3')
    mixer.init()
    mixer.music.load(f'speech{count % 2}.mp3')
    mixer.music.play()
    count += 1


def noi(s='xin chào bé Bull, bây giờ mình sẽ mở Nikia và Vlad cho Bull nhé. Thằng anh Bum không được xem ké đâu nhé. Mời bé Bull lên ghế ngồi xem nào.'):
    try:
        tts = gTTS(s, tld='com.vn', lang='vi')
        tts.save("hello.mp3")
        playsound("hello.mp3")
    except:
        pass


# linkIp = f'rtsp://admin:BQTDNG@192.168.1.10/H264?ch=1&subtype=0'

webB = ""
checkEndclip = False
dic = dict(YT_skip_ad="ytp-ad-skip-button-text", YT_overlay_close="ytp-ad-overlay-close-button",
           YT_play="ytp-large-play-button", YT_full_screen="ytp-fullscreen-button",
           YT_auto_play="ytp-autonav-toggle-button")
toadoChuot = toaDoChuot()


def veHinh(webB, toadoChuot):
    screenCapture()
    img = cv2.imread('screencapture\screencapture.png')
    webB.driver.minimize_window()
    # time.sleep(2)
    # pyautogui.hotkey('winleft', 'd')

    for index in range(0, 4):
        x = toadoChuot[index][0]
        y = toadoChuot[index][1]
        img = cv2.putText(img, f'{index + 1}', (x, y),
                          cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 8)

    imageShowFullScreen(img)
    webB.driver.maximize_window()
    return list


def xuLyLenh(webB, lenh, toadoChuot):
    if lenh.strip().find("một") or lenh.strip().find("1"):
        x = toadoChuot[0][0]
        y = toadoChuot[0][1]
        mouse_move(x, y)
        mouse_left_click()
        time.sleep(2)
        webB.clickClassName(dic["YT_full_screen"])

    elif lenh.strip().find("hai") or lenh.strip().find("2"):
        x = toadoChuot[1][0]
        y = toadoChuot[1][1]
        mouse_move(x, y)
        mouse_left_click()
        time.sleep(2)
        webB.clickClassName(dic["YT_full_screen"])

    elif lenh.strip().find("ba") or lenh.strip().find("3"):
        x = toadoChuot[2][0]
        y = toadoChuot[2][1]
        mouse_move(x, y)
        mouse_left_click()
        webB.clickClassName(dic["YT_full_screen"])

    elif lenh.strip().find("bốn") or lenh.strip().find("4"):
        x = toadoChuot[3][0]
        y = toadoChuot[3][1]
        mouse_move(x, y)
        mouse_left_click()
        time.sleep(2)
        webB.clickClassName(dic["YT_full_screen"])

    # print(hScr)
    return False


dateTmp = ""
text = ""
import os

running = True
time.sleep(3)
pyautogui.hotkey('winleft', 'd')
ktLichHocCount = 0

def nghe():
    try:
        with sr.Microphone() as source:
            # print('A Bi: I am listening')
            # audio_data = r.record(source, duration=5)
            audio_data = r.record(source, duration=3)
            kqNghe = r.recognize_google(audio_data, language='vi')
    except:
        kqNghe = ''
    return kqNghe

while True:
    try:
        running = True
        ktHoc = XuLyLenh.kiemTraLichHoc()
        # print(ktLichHocCount)
        if len(ktHoc) > 0:
            if ktLichHocCount == 0:
                speak(ktHoc)
                ktLichHocCount += 1
            elif ktLichHocCount == 200:
                speak(ktHoc)
                ktLichHocCount = 0
            else:
                ktLichHocCount += 1
        else:
            ktLichHocCount = 0
        # success, img = cap.read()
        # print("VL lớn")
        date, message = firebase.getData()
        if dateTmp != date:
            dateTmp = date
            text = message.lower().strip()
        else:
            text = ""



        if text == "":
            text = nghe()


        # print(text)

        if len(text) > 0:
            if running:
                if text.strip().find("nói") >= 0:
                    text = text[4:]
                    speak(text)
                    running = False
                if text.strip().find("shutdown") >= 0 or text.strip().find("shut down") >= 0 or text.strip().find(
                        "tắt máy") >= 0:
                    os.system("shutdown /s /t 1")
                if text.strip().find("restart") >= 0 or text.strip().find("re start") >= 0 or text.strip().find(
                        "khởi động") >= 0:
                    os.system("shutdown -t 0 -r -f")
            ######################## YOUTUTBE ########################
            if running:
                if text.strip().find("mở") >= 0:
                    text = text[3:].strip()
                    # webB.close()
                    webB = WebBrowserModule.Browser()

                    # print(text)
                    links, locations = webB.getLinks(text)
                    webB.driver.maximize_window()
                    running = False

            ######################## YOUTUTBE ########################

            ######################## NETFLIX ########################
            if running:
                if text.strip().find("flix") >= 0:
                    # webB.close()
                    webB = WebBrowserModule.Browser()
                    webB.getNetFlix()
                    webB.driver.maximize_window()
                    running = False
                if text.strip().find("trẻ em") >= 0:
                    # webB.close()
                    webB.driver.get("https://www.netflix.com/SwitchProfile?tkn=M2QG2DSF5JDM5CPSF4OHICZJLA")
                    running = False
                if text.strip().find("người lớn") >= 0:
                    # webB.close()
                    webB.driver.get("https://www.netflix.com/SwitchProfile?tkn=Y7D3RAAACNDX7AFNS3WG24S2ZY")
                    running = False
                if text.strip().find("lưới") >= 0:
                    screenCapture()
                    time.sleep(1)
                    img = cv2.imread("screencapture\\screencapture.png")
                    dsToaDoFlix, img = ScreenCapture.drawLine(img, 6, wScr, hScr)
                    # print(dsToaDoFlix)
                    webB.driver.minimize_window()
                    # time.sleep(2)
                    # pyautogui.hotkey('winleft', 'd')

                    ScreenCapture.imageShowFullScreen(img)
                    webB.driver.maximize_window()
                    running = False
                if text.strip().find("số") >= 0:
                    index = text[3:].strip()
                    index = int(index)
                    # print(dsToaDoFlix)
                    td = dsToaDoFlix[index - 1]
                    x = int(td[0])
                    y = int(td[1])
                    mouse_move(x, y)
                    mouse_left_click()
                    ######
                    time.sleep(1)
                    MouseControl.mouse_move(700, 275)
                    mouse_left_click()
                    time.sleep(5)
                    mouse_left_doubleclick()

                    running = False
                if text.strip().find("phóng to") >= 0:
                    mouse_left_doubleclick()
                    running = False
                if text.strip().find("thu nhỏ") >= 0:
                    mouse_left_doubleclick()
                    running = False

                    # print(list)

            ######################## NETFLIX ########################

            ######################## VE HINH ########################
            if running:
                if text.strip().find("vẽ") >= 0:
                    veHinh(webB, toadoChuot)
                    running = False

            ######################## VE HINH ########################

            ######################## CHUP HINH ########################
            if running:
                if text.strip().find("chụp hình") >= 0:
                    screenCapture();
                    firebase.upImage()
                    running = False

            ######################## CHUP HINH #######################

            ######################## XU LY NGAY GIO ########################
            # print(f'{running} / {text}')
            if running:
                # print('xu ly ngay gio')
                if text.strip().find("nay") >= 0 or text.strip().find("tháng") >= 0 or text.strip().find("năm") >= 0 or text.strip().find("thứ") >= 0 \
                        or text.strip().find("giờ") >= 0 or text.strip().find("âm lịch") >= 0 or text.strip().find("tết") >= 0:
                    try:
                        running, strText = XuLyLenh.xuLyNgayGio(text)
                        # print(f'ket qua {strText}')
                        if len(strText) > 0:
                            speak(strText)
                    except BaseException as err:
                        print(f'Unexpected {err}, {type(err)}')

            ######################## XU LY NGAY GIO ########################

            ######################## XU LY TINH TOAN ########################
            if running:
                # print(text)

                if text.find("/") >= 0 or text.find("+") >= 0 or text.find("-") >= 0 or text.find("*") >= 0:
                    try:
                        running, kqTinh = XuLyLenh.xuLyTinhToan(text)
                        if len(kqTinh) > 0:
                            speak(kqTinh)
                    except BaseException as err:
                        print(f'Unexpected {err}, {type(err)}')

            ######################## XU LY TINH TOAN ########################

            ######################## NHIET DO ########################
            if running:
                if text.strip().find("nhiệt độ") >= 0:
                    if temp > 0:
                        speak(f'nhiệt độ đêm nay là {temp} độ c')
                        running = False
                    else:
                        temp = XuLyLenh.LayNhietDo()
                        if temp > 0:
                            speak(f'nhiệt độ đêm nay là {temp} độ c')
                            running = False


            ######################## NHIET DO ########################

            ######################## TANG GIAM VOLUMN ########################
            if running:
                # print(vol)
                # print(minVol)
                # print(maxVol)
                if text.strip().find("tăng âm thanh") >= 0:
                    if vol <= -5:
                        vol = vol + 5
                        # print(vol)
                        volume.SetMasterVolumeLevel(vol, None)
                        running = False
                    else:
                        running = False
                if text.strip().find("giảm âm thanh") >= 0:
                    if vol >= minVol + 5:
                        vol = vol - 5
                        # print(vol)
                        volume.SetMasterVolumeLevel(vol, None)
                        running = False
                    else:
                        running = False
                if text.strip().find("tắt âm thanh") >= 0:
                    vol = minVol
                    volume.SetMasterVolumeLevel(vol, None)
                    running = False




            ######################## SCROLL MOUSE, CLICK SELECTED ########################
            if running:
                if text.strip().find("xuống") >= 0:
                    try:
                        webB.driver.execute_script(f'window.scrollTo({x}, {x + h});')
                        x = x + h
                        running = False

                    except:
                        running = False
                    running = False
                if text.strip().find("lên") >= 0:
                    try:
                        x = x - h
                        webB.driver.execute_script(f'window.scrollTo({x}, {x + h});')
                        running = False

                    except:
                        running = False
                if text.strip().find("stop") >= 0 or text.strip().find("start") >= 0 \
                        or text.strip().find("dừng") >= 0 or text.strip().find("chạy") >= 0:
                    MouseControl.mouse_move(int(wScr/2), int(hScr/2))
                    MouseControl.mouse_left_click()
                    running = False

            if running:
                running = xuLyLenh(webB, text, toadoChuot)

            ######################## SCROLL MOUSE ########################

        ######################## TAT QUANG CAO YOUTUBE ########################
        if webB != "":
            webB.clickClassName(dic["YT_skip_ad"])
            webB.clickAgument()
        ######################## TAT QUANG CAO YOUTUBE ########################
    except BaseException as err:
        print(f'Unexpected {err}, {type(err)}')
