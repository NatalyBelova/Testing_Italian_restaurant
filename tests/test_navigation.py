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

from pages.main_page import Main_page

"""Проверка, что основное меню переходит на соответствующие страницы"""
@allure.description("Test Sections")
def test_sections():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    mp = Main_page(driver)
    mp.sections()

    print("Finish Test")
    time.sleep(1)
    driver.quit()

"""Проверка смены языка - Не работает"""
@allure.description("Test Language")
def test_language():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    mp = Main_page(driver)
    mp.change_language()

    print("Finish Test")
    time.sleep(1)
    driver.quit()
#


