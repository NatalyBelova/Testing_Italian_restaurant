import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Team_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    value_team = "//*[@id='section-4']/div/div/div"


    """Getters"""

    def get_value_team(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_team)))


    """Actions"""


    """Methods"""

    """Проверяем, что действительно попали в раздел Команда"""
    def team(self):
        with allure.step("Team"):
            Logger.add_start_step(method='team')
            self.assert_word(self.get_value_team(), "Наша команда - дружные во всех отношениях ребята. Проффессионалы своего дела. Вдохновленные Италией, мы готовы погрузить Вас в атмосферу раземероенного, солнечного и вкусного итальянского быта!")
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#section-4")
            Logger.add_end_step(url=self.driver.current_url, method='team')







