import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class History_page(Base):

    def init(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    value_story = "//*[@id='section-2']/div/div/div"


    """Getters"""

    def get_value_story(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.value_story)))


    """Actions"""



    """Methods"""

    """Проверяем, что действительно попали в раздел История"""

    def history(self):
        with allure.step("History"):
            Logger.add_start_step(method='history')
            print((self.get_value_story().text))
            self.assert_word(self.get_value_story(), "У каждого ресторана есть стиль, дизайн и душа. В нашем вы найдете улочки Италии провинциального городка, где встречают с распростёртыми объятьями и широкой душой и с лёгкостью подстраиваются к желанию гостя - друга. Квалифицированные повора и официанты не оставят вас равнодушными.")
            self.assert_url("https://mr-usackiy.github.io/amici-D-italia/index.html#section-2")
            Logger.add_end_step(url=self.driver.current_url, method='history')

