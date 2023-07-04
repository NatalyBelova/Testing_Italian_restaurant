import time
from telnetlib import EC

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from pages.contacts_page import Contacts_page
from pages.main_page import Main_page


"""Отправка email"""
@allure.description("Test Sending Email")
def test_sending_email():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    mp = Main_page(driver)
    mp.select_contacts()

    cp = Contacts_page(driver)
    cp.send_email()


    print("Finish Test")
    time.sleep(2)
    driver.quit()





