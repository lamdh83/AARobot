import cv2
from selenium import webdriver
from bs4 import BeautifulSoup
import random
import time


class Browser():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions();
        prefs = {"profile.default_content_setting_values.notifications": 2,
                 "credentials_enable_service": False,
                 "profile.password_manager_enabled": False
                 }
        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
        self.dictionary = {"YT_skip_ad": "ytp-ad-skip-button-text", "YT_overlay_close": "ytp-ad-overlay-close-button",
                           "YT_play": "ytp-large-play-button", "YT_full_screen": "ytp-fullscreen-button",
                           "YT_auto_play": "ytp-autonav-toggle-button"}

    # def getLinks(self, className='yt-simple-endpoint style-scope ytd-video-renderer', link='https://www.youtube.com'):
    #     links = []
    #     times = []
    #     page_source = BeautifulSoup(self.driver.page_source)
    #     # print(page_source)
    #     profiles = page_source.find_all('a', class_=className)
    #     # print(profiles[0].get('aria-label'))
    #     for index in range (0, len(profiles) - 1):
    #         profile_ID = profiles[index].get('href')
    #         time = profiles[index].get('aria-label')
    #         # print(time)
    #         chuoi = str(time).replace(',','')
    #         list = chuoi.split(' ')
    #
    #         # print(list)
    #         indexMin = list.index('minutes')
    #         min = int(list[indexMin-1])
    #         # print(min)
    #         try:
    #             indexSe = list.index('seconds')
    #             second = int(list[indexSe-1])
    #         except:
    #             second = 0
    #
    #         # print(second)
    #         totalTime = min*60 + second
    #         times.append(str(totalTime))
    #         # print(profile_ID)
    #         links.append(link + profile_ID)
    #     return links, times

    def getLinks(self, query='nikita+and+vlad'):
        url = f'https://www.youtube.com/results?search_query={query}'
        className = 'yt-simple-endpoint style-scope ytd-video-renderer'
        link = 'https://www.youtube.com'
        self.driver.get(url)
        self.driver.maximize_window()
        links = []
        locations = []

        page_source = BeautifulSoup(self.driver.page_source)
        # print(page_source)
        profiles = page_source.find_all('a', class_=className)
        list = self.driver.find_elements_by_class_name("style-scope ytd-video-renderer")

        # print(profiles[0].get('aria-label'))
        # print(profiles)
        for index in range(0, len(profiles) - 1):
            profile_ID = profiles[index].get('href')
            e = list[index]
            locations.append(e.location)
            links.append(link + profile_ID)
        return links, locations

    def getNetFlix(self):
        url = 'https://www.netflix.com/vn-en/login'
        self.driver.get(url)
        time.sleep(2)
        user = open('user.txt')
        line = user.readlines()
        username = line[0]
        password = line[1]
        time.sleep(2)

        # dinh vi email theo id id_userLoginId
        email_field = self.driver.find_element_by_id('id_userLoginId')
        # nhap dia chi email
        email_field.send_keys(username)
        time.sleep(3)

        # dinh vi password theo name password
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(password)
        print('- Finish keying in password')
        time.sleep(2)

        # dinh vi nut sign in bang xpath
        login_field = self.driver.find_element_by_xpath(
            '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
        login_field.click()
        time.sleep(5)
        self.driver.get("https://www.netflix.com/SwitchProfile?tkn=Y7D3RAAACNDX7AFNS3WG24S2ZY")

    def clickClassName(self, className):
        try:
            button = self.driver.find_element_by_class_name(className)
            button.click()
        except:
            pass

    def clickAgument(self, className="ytp-ad-overlay-close-button"):
        try:
            button = self.driver.find_element_by_class_name(className)
            # print(button)
            self.driver.execute_script("arguments[0].click();", button)
        except:
            pass

    def openLink(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()

    def closeAutoPlay(self, close="true"):
        try:
            source = BeautifulSoup(self.driver.page_source)
            profile = source.find_all('div', class_="ytp-autonav-toggle-button")
            name = profile[0].get("aria-checked")
            if name != close:
                self.clickClassName(self.dictionary["YT_auto_play"])
        except:
            pass

    def checkEndClip(self):
        try:
            source = BeautifulSoup(self.driver.page_source)
            profile = source.find_all('div', class_="ytp-progress-bar")
            value = profile[0].get("aria-valuetext")
            values = str(value).split('of')
            if values[0].strip() == values[1].strip():
                return True
            else:
                return False

        except:
            return False


def main():
    checkEndclip = False
    webB = Browser()
    dic = webB.dictionary
    links, times = webB.getLinks()
    # print(links)
    # print(times)
    index = random.randint(0, len(links) - 1)
    # print(index)

    webB.openLink(links[index])
    webB.clickClassName(dic["YT_play"])
    webB.clickClassName(dic["YT_full_screen"])
    while True:
        webB.clickClassName(dic["YT_skip_ad"])
        webB.clickAgument()
        checkEndclip = webB.checkEndClip()
        if checkEndclip:
            index = random.randint(0, len(links) - 1)
            webB.openLink(links[index])
            webB.clickClassName(dic["YT_full_screen"])


if __name__ == "__main__":
    main()
