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

from pages.history_page import History_page
from pages.main_page import Main_page
from pages.team_page import Team_page



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


"""Проверка правильности смены языка"""
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


"""Проверка верного перехода на страницу Команды"""
@allure.description("Test Team Page ")
def test_team_page():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    mp = Main_page(driver)
    mp.select_team()

    tp = Team_page(driver)
    tp.team()


    print("Finish Test")
    time.sleep(1)
    driver.quit()



"""Проверка верного перехода на страницу История"""
@allure.description("Test History Page ")
def test_history_page():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\resource\\chromedriver.exe', chrome_options = options)
    driver = webdriver.Chrome(service=service)
    print("Start Test")

    mp = Main_page(driver)
    mp.select_history()

    hp = History_page(driver)
    hp.history()


    print("Finish Test")
    time.sleep(1)
    driver.quit()
