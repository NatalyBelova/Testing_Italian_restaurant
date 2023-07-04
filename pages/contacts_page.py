import time
import allure

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger



class Contacts_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.fake = Faker() # Создаем экземпляр класса Faker

    """Locators"""

    email = "//input[@placeholder='Enter your email here*']"
    send_button = "/html/body/footer/div/div/form/button"
    value_header = "//*[@id='footer']/div/div/h2"
    opening_hours = "//*[@id='footer']/div/div/div/div[1]/p[2]"
    address = "//*[@id='footer']/div/div/div/div[2]/p[2]"
    contact = "//*[@id='footer']/div/div/div/div[3]/p[2]"
    messenger_facebook = "//*[@id='footer']/div/div/div/div[4]/a[1]"
    messenger_instagram = "//*[@id='footer']/div/div/div/div[4]/a[2]"
    messenger_twitter= "//*[@id='footer']/div/div/div/div[4]"



    """Getters"""

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_send_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.send_button)))

    def get_value_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_header)))

    def get_opening_hours(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.opening_hours)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_contact(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.contact)))

    def get_messenger_facebook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.messenger_facebook)))

    def get_messenger_instagram(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.messenger_instagram)))

    def get_messenger_twitter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.messenger_twitter)))



    """Actions"""

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input Get Email")

    def click_send_button(self):
        self.get_send_button().click()
        print("Click Send button")

    def click_messenger_facebook(self):
        self.get_messenger_facebook().click()
        print("Click Messenger Facebookn")

    def click_messenger_instagram(self):
        self.get_messenger_instagram().click()
        print("Click Messenger Instagram")

    def click_messenger_twitter(self):
        self.get_messenger_twitter().click()
        print("Click Messenger Twitter")



    """Methods"""

    """Отправляем email для подписки"""

    def send_email(self):
        with allure.step("Send Email"):
            Logger.add_start_step(method='send_email')
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#footer")
            self.assert_word(self.get_value_header(), "Подпишитесь на вкусные обновления")
            self.input_email(self.fake.ascii_free_email())
            self.get_screenshot()
            self.click_send_button()
            Logger.add_end_step(url=self.driver.current_url, method='send_email')

    def check_information(self):
        with allure.step("Check Information"):
            Logger.add_start_step(method='check_information')
            self.assert_word(self.get_opening_hours(), "понедельник-воскресение 12.00-23.00")
            self.assert_word(self.get_address(), "Полтавский пр., 2, Санкт-Петербург")
            self.assert_word(self.get_contact(), "+7911-176-83-69\nlalal@mail.ru")
            Logger.add_end_step(url=self.driver.current_url, method='check_information')

    def check_messendger(self):
        with allure.step("Check Messendger"):
            Logger.add_start_step(method='check_messendger')
            time.sleep(1)
            # self.click_messenger_facebook()
            self.click_messenger_instagram()
            time.sleep(2)
            self.get_screenshot()
            # self.click_messenger_twitter()
            Logger.add_end_step(url=self.driver.current_url, method='check_messendger')



