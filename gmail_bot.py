# This is browser bot example written on Python with Selenium
# It uses browser to send gmail message automatically
# You can write your own bot to solve your specific problem
# For example trading bot
#
# My youtube channel: https://www.youtube.com/c/mautoztech
# My channel about programming: https://www.youtube.com/@aidev
#
# Licensed under GNU GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html

import undetected_chromedriver as uc
import pickle
from selenium.common import exceptions
import keyboard
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
driver = uc.Chrome(use_subprocess=True)
#driver = uc.Chrome(use_subprocess=True, version_main=109) # If you have chrome version error use this line instead. And specify your chrome version
driver.get("https://mail.google.com/mail/u/0/?tab=wm#inbox")

keyboard.write("PUT_HERE_YOUR_GMAIL_ACCOUNT");
driver.execute_script('nextButton = document.getElementsByClassName("VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"); nextButton[0].click();');
while True:
        try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Wz0RKd")))
                sleep(1)
                break
        except:
                print("Page loading failed. Out of time error.")
                sleep(10)

keyboard.write("PUT HERE YOUR PASSWORD");
driver.execute_script('nextButton = document.getElementsByClassName("VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"); nextButton[0].click();');
while True:
        try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "T-I-KE")))
                sleep(1)
                break
        except:
                print("Page loading failed. Out of time error.")
                sleep(10)
driver.execute_script('nextButton = document.getElementsByClassName("T-I T-I-KE L3"); nextButton[0].click();');

while True:
        try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "T-I-atl")))
                sleep(1)
                break
        except:
                print("Page loading failed. Out of time error.")
                sleep(10)
keyboard.write("RECEPIENT@gmail.com"); #RECEPIENT ПОЛУЧАТЕЛЬ 
driver.execute_script('document.getElementsByClassName("aoD az6")[0].click();');
keyboard.write("Subject of our message"); # SUBJECT ТЕМА СООБЩЕНИЯ
driver.execute_script('document.getElementsByClassName("LW-avf")[0].innerHTML = "Our message";');
#MESSAGE ТЕМА СООБЩЕНИЯ
driver.execute_script('document.getElementsByClassName("T-I J-J5-Ji aoO v7 T-I-atl L3")[0].click();');
