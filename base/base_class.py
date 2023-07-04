from datetime import datetime
import os

class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url", get_url)


    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method Screenshorts"""

    def get_screenshot(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\Testing_Italian_restaurant\\screen\\' + name_screenshot)
        # directory = os.path.join(os.getcwd(), 'screen')
        # self.driver.save_screenshot(os.path.join(directory, name_screenshot))


    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")