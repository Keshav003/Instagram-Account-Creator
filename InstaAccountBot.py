import csv
import string
import threading
import time

import pyperclip as pc
from proxyserver import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def Proxy():
    proxy = Random_Proxy()

    url = 'https://www.youtube.com'
    request_type = "get"

def randomString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def Password(length):
    str_ = string.hexdigits
    return ''.join(random.choice(str_) for i in range(length))


def Instagram():
    driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
    driver.delete_all_cookies()
    driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')
    driver.delete_all_cookies()
    driver.execute_script("window.open('')")

    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://temp-mail.org/en/')

    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "click-to-copy"))
        )
    finally:
        driver.find_element_by_xpath('//*[@id="mail"]').click()
        driver.find_element_by_xpath('//*[@id="mail"]').click()
        driver.find_element_by_xpath('//*[@id="mail"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/button[1]').click()
        from ctypes import windll
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()
        email = driver.find_element_by_id('click-to-copy').click()
        email = pc.paste()

    driver.switch_to.window(driver.window_handles[0])

    driver.find_element_by_css_selector('input[name="emailOrPhone"').send_keys(email)
    driver.find_element_by_name('fullName').send_keys(randomString(10))

    username = randomString(30)
    password = 'instagrambot'

    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password + Keys.RETURN)
    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'option[title="2000"]'))
        )
    finally:
        driver.find_element_by_css_selector('option[title="2000"]').click()
        driver.find_element_by_css_selector('button[class="sqdOP  L3NKy _4pI4F  y3zKF     "]').click()

    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_id('click-to-refresh').click()

    try:
        wait = WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Insta"))
        )
    finally:
        driver.find_element_by_partial_link_text('Insta').click()
    try:
        wait = WebDriverWait(driver, 10000).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            'td[style="padding:10px;color:#565a5c;font-size:32px;font-weight:500;text-align:center;padding-bottom:25px;"]'))
        )
    finally:
        gmail_verification = driver.find_element_by_css_selector(
            'td[style="padding:10px;color:#565a5c;font-size:32px;font-weight:500;text-align:center;padding-bottom:25px;"]').text

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_css_selector('input[class="j_2Hd    RO68f  M5V28"]').send_keys(gmail_verification)
    driver.find_element_by_css_selector('button[class="sqdOP  L3NKy   y3zKF     "]').click()

    print('Username:' + username)
    print('Password:' + password)

    def print_cred():
        with open('credentials.csv', 'a+', newline='') as cred:
            write = csv.writer(cred)
            credentials = [email]
            write.writerow(credentials)

    print_cred()
    time.sleep(1048778)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    driver.get('https://www.instagram.com/v_keshav_/?hl=en')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button')

def main():
    Proxy()
    Instagram()

N = 10
thread_list = list()
def run():
    for i in range(N):
        t = threading.Thread(name='Test {}'.format(i), target=main)
        t.start()
        time.sleep(1)
        thread_list.append(t)
    for thread in thread_list:
        thread.join()

run()