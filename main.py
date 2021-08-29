import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

load_dotenv()
chrome_driver_path = os.environ['CHROME_DRIVER_PATH']
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://tinder.com/')
time.sleep(5)

login = driver.find_element_by_xpath(
    '//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()
time.sleep(5)

login_w_fb = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div[1]/div/div[3]/span/div[2]/button')
login_w_fb.click()
time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.title)

email_fb = driver.find_element_by_xpath('//*[@id="email"]')
email_fb.send_keys(os.environ['EMAIL'])
password_fb = driver.find_element_by_xpath('//*[@id="pass"]')
password_fb.send_keys(os.environ['PASSWORD'])
password_fb.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
# print(driver.title)

time.sleep(8)
cookies_allow = driver.find_element_by_xpath('//*[@id="o-738591094"]/div/div[2]/div/div/div[1]/button')
cookies_allow.click()
time.sleep(5)
location_allow = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div/div/div[3]/button[1]')
location_allow.click()
time.sleep(5)
notification_disallow = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div/div/div[3]/button[2]')
notification_disallow.click()
time.sleep(8)
like = driver.find_element_by_xpath(
    '//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button')

while True:
    time.sleep(1)
    try:
        like.click()
    except ElementClickInterceptedException:
        try:
            match = driver.find_element_by_css_selector(".itsAMatch a")
            match.click()
        except NoSuchElementException:
            try:
                home_screen_disallow = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div[2]/button[2]')
                home_screen_disallow.click()
            except NoSuchElementException:
                print('Loading up people near me, sleep 2 seconds.')

# driver.quit()
