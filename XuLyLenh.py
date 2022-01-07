from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

import cv2
from lunarcalendar import Converter, Solar

now = datetime.now()
# now.strftime("%d/%m/%Y %H:%M:%S")
# print(now)
date_str = now.strftime("%d")
month_str = now.strftime("%m")
year_str = now.strftime("%Y")
week_str = now.strftime("%A").lower()
dictWeek = {"monday":"hai", "tuesday":"ba", "wednesday":"tư", "thursday":"năm", "friday":"sáu", "saturday":"bảy", "sunday":"chủ nhật"}
week_str_vn = dictWeek[week_str]

solar = Solar(int(year_str), int(month_str), int(date_str))
luna = Converter.Solar2Lunar(solar)

lichHoc = {"năm": "anh văn", "sáu": "anh văn", "bảy": "lập trình", "chủ nhật": "lập trình"}
try:
    monHoc = lichHoc[week_str_vn]
except:
    monHoc = ""





def xuLyNgayGio(text):
    # print(f'bat dau xl {text}')
    if text.strip().find("ngày") >= 0:
        strText = f'hôm nay là ngày {date_str}'
        # print(strText)
        return False, strText

    if text.strip().find("tháng") >= 0:
        strText = f'tháng này là tháng {month_str}'
        # print(strText)
        return False, strText

    if text.strip().find("năm") >= 0:
        strText = f'năm nay là năm {year_str}'
        # print(strText)
        return False, strText

    if text.strip().find("thứ") >= 0:
        strText = f'hôm nay là thứ {week_str_vn}'
        # print(strText)
        return False, strText

    if text.strip().find("giờ") >= 0:
        now = datetime.now()
        hour_str = now.strftime("%H")
        min_str = now.strftime("%M")
        strText = f'bây giờ là {hour_str} giờ, {min_str} phút'
        # print(strText)
        return False, strText

    if text.strip().find("âm lịch") >= 0:
        strText = f'hôm nay là ngày {luna.day} tháng {luna.month} năm {luna.year} âm lịch'
        return False, strText

    if text.strip().find("tết") >= 0:
        lunadate = datetime(luna.year, luna.month, luna.day)
        # print(lunadate)
        newyear = datetime(luna.year + 1, 1, 1)
        # print(newyear)
        delta = newyear - lunadate
        soNgayDenTet = delta.days
        strText = f'còn {soNgayDenTet} ngày nữa là đến tết âm lịch nhé.'
        # print(soNgayDenTet)
        return False, strText

def kiemTraLichHoc():
    if len(monHoc) > 0:
        now = datetime.now()
        hour_str = now.strftime("%H")
        min_str = now.strftime("%M")
        # print(min_str)
        if hour_str == "19":
            if min_str == "20":
                return f'còn 10 phút nữa là đến giờ học {monHoc} bum chuẩn bị đi học nhé'
            elif min_str =="25":
                return f'còn 5 phút nữa là đến giờ học {monHoc} bum chuẩn bị đi học nhé'
            else:
                return ""
        else:
            return ""
    else:
        return ""

def xuLyTinhToan(text):

    if text.find("+") >= 0:
        strSo = text.split("+")
        so1 = float(strSo[0])
        so2 = float(strSo[1])
        tong = so1 + so2
        kq = f'{round(so1,0)} cộng {round(so2,0)} bằng {round(tong,0)}'
        return False, kq
    elif text.find("-") >= 0:
        strSo = text.split("-")
        so1 = float(strSo[0])
        so2 = float(strSo[1])
        hieu = so1 - so2
        kq = f'{round(so1,0)} trừ {round(so2,0)} bằng {round(hieu,0)}'
        return False, kq
    elif text.find("*") >= 0:
        strSo = text.split("*")
        so1 = float(strSo[0])
        so2 = float(strSo[1])
        nhan = so1 * so2
        kq = f'{round(so1,0)} nhân {round(so2,0)} bằng {round(nhan,0)}'
        return False, kq
    elif text.find("/") >= 0:
        strSo = text.split("/")
        so1 = float(strSo[0])
        so2 = float(strSo[1])
        chia = so1 // so2
        du = so1 - (chia*so2)
        kq = f'{round(so1,0)} chia {round(so2,0)} bằng {round(chia,0)} và dư {round(du,0)}'
        return False, kq



def xuLyChuoiTinhToan(kq):
    kq = "tính 876 dsf dfds chia 3 sdf "
    kq = kq.strip()
    string = kq.split(" ")
    so1 = 0
    so2 = 0
    phepTinh = ""
    chuoiPhepTinh = "cộng trừ nhân chia"
    for chuoi in string:
        try:
            if float(chuoi):
                if so1 == 0:
                    so1 = float(chuoi)

        except:
            pass

        try:
            if float(chuoi):
                if so1 > 0:
                    so2 = float(chuoi)

        except:
            pass
        if chuoiPhepTinh.find(chuoi) >= 0:
            phepTinh = chuoi
    return so1, so2, phepTinh

    # print(f'{so1} {phepTinh} {so2}')
def LayNhietDo():
    try:
        driver = webdriver.Chrome()
        url = "https://www.weather-forecast.com/locations/Dalat/forecasts/latest"
        driver.get(url)
        page_source = BeautifulSoup(driver.page_source)
        profiles = page_source.find_all('span', class_="temp b-forecast__table-value")
        temp = profiles[38].getText()
        driver.close()
        return int(temp)
    except:
        return 0




def main():

    running, text = xuLyNgayGio("ngày")
    print(f'{running}/ {text}')



if __name__ == "__main__":
    main()

