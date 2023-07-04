import time

from faker import Faker
import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
from selenium.webdriver.common.action_chains import ActionChains


class Main_page(Base):

    url = 'https://mr-usackiy.github.io/amici-D-italia/index.html#'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker()



    """Locators"""

    history_button = "/html/body/div[2]/header/div/div[2]/ul/li[1]/a"
    team_button = "//a[@href='#section-4']"
    contact_button = "//a[@href='#footer']"
    menu_button = "//a[@href='#menu__2']"
    book_button = "//button[@class='book-table']"
    language_english_button = "/html/body/div[2]/section/div[2]/div[1]/div[1]/a"
    language_russian_button = "//a[@class='rus']"

    date = "//input[@type='date']"
    time = "//input[@type='time']"
    phone_number = "//input[@placeholder='+7-999-999-99-99']"
    email = "//input[@placeholder='lalala@mail.ru']"
    book = "/html/body/div[2]/section/div[1]/div/form/button"



    """Getters"""

    def get_history_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.history_button)))

    def get_team_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.team_button)))

    def get_contact_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.contact_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_book_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book_button)))

    def get_language_english_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.language_english_button)))

    def get_language_russian_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.language_russian_button)))

    def get_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date)))

    def get_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.time)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_book(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.book)))



    """Actions"""

    def click_history_button(self):
        self.get_history_button().click()
        print("Click History button")

    def click_team_button(self):
        self.get_team_button().click()
        print("Click Team button")

    def click_contact_button(self):
        self.get_contact_button().click()
        print("Click Contact button")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Click Menu button")

    def click_book_button(self):
        self.get_book_button().click()
        print("Click Book button")

    def click_language_english_button(self):
        self.get_language_english_button().click()
        print("Click Language English button")

    def click_language_russian_button(self):
        self.get_language_russian_button().click()
        print("Click Language Russian button")

    def input_date(self, date):
        self.get_date().send_keys(date)
        print("Input Date")

    def input_time(self, time):
        self.get_time().send_keys(time)
        print("Input Time")

    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input Phone Number")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input Email")

    def click_book(self):
        self.get_book().click()
        print("Click Book")





    """Methods"""

    """Метод проверки работы все разделов меню"""
    def sections(self):
        with allure.step("Select Sections"):
            Logger.add_start_step(method='select_sections')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            time.sleep(3)
            self.click_history_button()
            time.sleep(2)
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#section-2")
            self.driver.back()
            time.sleep(2)
            self.click_team_button()
            time.sleep(2)
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#section-4")
            self.driver.back()
            time.sleep(2)
            self.click_contact_button()
            time.sleep(2)
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#footer")
            self.driver.back()
            time.sleep(2)
            self.click_menu_button()
            time.sleep(2)
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#menu__2")
            self.driver.back()
            time.sleep(2)
            Logger.add_end_step(url=self.driver.current_url, method='select_sections')


    """Метод проверки смены языка"""
    def change_language(self):
        with allure.step("Select Change Language"):
            Logger.add_start_step(method='change_language')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            time.sleep(2)
            self.click_language_english_button()
            time.sleep(3)
            self.get_screenshot()
            self.click_language_russian_button()
            time.sleep(3)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='change_language')


    """Выбор раздела История"""
    def select_history(self):
        with allure.step("Select History"):
            Logger.add_start_step(method='select_history')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            time.sleep(2)
            self.click_history_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_history')


    """Выбор раздела Команда"""
    def select_team(self):
        with allure.step("Select Team"):
            Logger.add_start_step(method='select_team')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            time.sleep(2)
            self.click_team_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_team')


    """Выбор раздела Контакты"""
    def select_contacts(self):
        with allure.step("Select Contacts"):
            Logger.add_start_step(method='select_contacts')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            time.sleep(2)
            self.click_contact_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_contacts')


    """Выбор раздела Меню"""
    def select_menu(self):
        with allure.step("Select Menu"):
            Logger.add_start_step(method='select_menu')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            time.sleep(2)
            self.click_menu_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_menu')


    """Выбор кнопки Забронируйте столик"""
    def select_book(self):
        with allure.step("Select Book"):
            Logger.add_start_step(method='select_book')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            time.sleep(3)
            self.click_book_button()
            self.get_screenshot()
            self.input_date("2023-07-01")
            self.input_time("12:00")
            self.input_phone_number("+7-999-999-99-99")
            self.input_email("lalala@mail.ru")
            self.get_screenshot()
            self.click_book()
            Logger.add_end_step(url=self.driver.current_url, method='select_book')


    """Смена языка на английский"""
    def select_language_english(self):
        with allure.step("Select Language English"):
            Logger.add_start_step(method='select_language_english')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            time.sleep(2)
            self.click_language_english_button()
            time.sleep(3)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='select_language_english')


    """Смена языка на русский"""
    def select_language_russian(self):
        with allure.step("Select Language Russian"):
            Logger.add_start_step(method='select_language_russian')
            self.driver.get(self.url)  # Метод, который открывает нашу url
            self.driver.maximize_window()
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#")
            self.click_language_russian_button()
            Logger.add_end_step(url=self.driver.current_url, method='select_language_russian')

    """Смена размера дисплея"""
    # def select_display(self):
    #     with allure.step("Select Language Russian"):
    #         Logger.add_start_step(method='select_language_russian')
    #         self.driver.get(self.url)  # Метод, который открывает нашу url
    #         # self.driver.maximize_window()
    #
    #         self.driver.execute_script("window.scrollTo(0, 5000)")
    #         self.get_screenshot()
    #         Logger.add_end_step(url=self.driver.current_url, method='select_language_russian')

