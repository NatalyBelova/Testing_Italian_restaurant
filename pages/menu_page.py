import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Menu_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    risotto = "//div[@class='card-1 card delay--2s cards_animation--0-7']"
    salad = "//div[@class='card-6 card delay--05s cards_animation--0-7']"
    bruschetta = "//div[@class='card-5 card delay--2s cards_animation--0-7']"
    pasta = "//div[@class='card-4 card delay--1s cards_animation--0-7']"
    snacks = "//div[@class='card-7 card delay--3s cards_animation--0-7']"
    dessert = "//div[@class='card-2 card delay--1s cards_animation--0-7']"
    pizza = "//div[@class='card-3 card delay--05s cards_animation--0-7']"
    button_close_1 = "//*[@id='menu__2']/div[2]/div[1]/a"
    button_arrow_1 = "//img[@class='next6']"
    button_close_2 = "//*[@id='menu__2']/div[7]/div[1]/a"
    button_close_3 = "//*[@id='menu__2']/div[6]/div[1]/a/img"
    button_arrow_2 = "//img[@class='next4']"
    button_close_4 = "//*[@id='menu__2']/div[5]/div[1]/a/img"
    button_arrow_3 = "//img[@class='next7']"
    button_close_5 = "//*[@id='menu__2']/div[8]/div[1]/a/img"
    button_close_6 = "//*[@id='menu__2']/div[3]/div[1]/a/img"
    button_arrow_4 = "//img[@class='next']"
    button_close_7 = "//*[@id='menu__2']/div[4]/div[1]/a/img"


    """Getters"""

    def get_risotto(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.risotto)))

    def get_salad(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.salad)))

    def get_bruschetta(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bruschetta)))

    def get_pasta(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pasta)))

    def get_snacks(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.snacks)))

    def get_dessert(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dessert)))

    def get_pizza(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pizza)))

    def get_button_close_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_1)))

    def get_button_arrow_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_arrow_1)))

    def get_button_close_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_2)))

    def get_button_close_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_3)))

    def get_button_arrow_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_arrow_2)))

    def get_button_close_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_4)))

    def get_button_arrow_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_arrow_3)))

    def get_button_close_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_5)))

    def get_button_close_6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_6)))

    def get_button_arrow_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_arrow_4)))

    def get_button_close_7(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_close_7)))



    """Actions"""

    def click_risotto(self):
        self.get_risotto().click()
        print("CLick risotto")

    def click_salad(self):
        self.get_salad().click()
        print("CLick salad")

    def click_bruschetta(self):
        self.get_bruschetta().click()
        print("CLick bruschetta")

    def click_pasta(self):
        self.get_pasta().click()
        print("CLick pasta")

    def click_snacks(self):
        self.get_snacks().click()
        print("CLick snacks")

    def click_dessert(self):
        self.get_dessert().click()
        print("CLick dessert")

    def click_pizza(self):
        self.get_pizza().click()
        print("CLick pizza")

    def click_button_close_1(self):
        self.get_button_close_1().click()
        print("CLick Button Close_1")

    def click_button_arrow_1(self):
        self.get_button_arrow_1().click()
        print("CLick Button Arrow_1")

    def click_button_close_2(self):
        self.get_button_close_2().click()
        print("CLick Button Close_2")

    def click_button_close_3(self):
        self.get_button_close_3().click()
        print("CLick Button Close_3")

    def click_button_arrow_2(self):
        self.get_button_arrow_2().click()
        print("CLick Button Arrow_2")

    def click_button_close_4(self):
        self.get_button_close_4().click()
        print("CLick Button Close_4")

    def click_button_arrow_3(self):
        self.get_button_arrow_3().click()
        print("CLick Button Arrow_3")

    def click_button_close_5(self):
        self.get_button_close_5().click()
        print("CLick Button Close_5")

    def click_button_close_6(self):
        self.get_button_close_6().click()
        print("CLick Button Close_6")

    def click_button_arrow_4(self):
        self.get_button_arrow_4().click()
        print("CLick Button Arrow_4")

    def click_button_close_7(self):
        self.get_button_close_7().click()
        print("CLick Button Close_7")



    """Methods"""

    """Проверка просмотра всего меню"""
    def select_dishes(self):
        with allure.step("Select Dishes"):
            Logger.add_start_step(method='select_dishes')
            self.get_screenshot()
            self.click_risotto()
            time.sleep(1)
            self.get_screenshot()
            self.click_button_close_1()
            self.click_salad()
            time.sleep(1)
            self.get_screenshot()
            self.click_button_arrow_1()
            time.sleep(0.5)
            self.click_button_arrow_1()
            time.sleep(0.5)
            self.click_button_arrow_1()
            time.sleep(0.5)
            self.click_button_close_2()
            self.click_bruschetta()
            time.sleep(1)
            self.get_screenshot()
            self.click_button_close_3()
            self.click_pasta()
            time.sleep(1)
            self.get_screenshot()
            self.click_button_arrow_2()
            time.sleep(0.5)
            self.click_button_arrow_2()
            self.click_button_close_4()
            self.click_snacks()
            time.sleep(1)
            self.get_screenshot()
            self.click_button_arrow_3()
            self.click_button_close_5()
            self.click_dessert()
            time.sleep(1)
            self.get_screenshot()
            self.click_button_close_6()
            self.click_pizza()
            time.sleep(1)
            self.get_screenshot()
            self.click_button_arrow_4()
            time.sleep(0.5)
            self.click_button_arrow_4()
            time.sleep(0.5)
            self.click_button_arrow_4()
            time.sleep(0.5)
            self.click_button_arrow_4()
            self.click_button_close_7()
            Logger.add_end_step(url=self.driver.current_url, method='select_dishes')




