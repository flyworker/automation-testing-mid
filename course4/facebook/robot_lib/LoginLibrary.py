import os.path
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
WAITING_TIME = 5

class LoginLibrary(object):

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome('./robot_lib/chromedriver', chrome_options=options)
        self.driver.get("http://www.facebook.com")

    def create_user(self, username, password):
        print('create', username, password)

    def attempt_to_login_with_credentials(self, username, password):
        # super().__init__()

        assert "Facebook" in self.driver.title

        self.driver.implicitly_wait(WAITING_TIME)
        elem = self.driver.find_element_by_id("email")
        elem.send_keys(username)
        elem = self.driver.find_element_by_id("pass")

        elem.send_keys(password)

        self.driver.implicitly_wait(WAITING_TIME)

        elem.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(WAITING_TIME)

    def status_should_be(self, expected_status):
        header= self.driver.find_element_by_xpath('//*[@id="header_block"]/span').text
        if expected_status != header:
            raise AssertionError("Expected status should be '%s' but was '%s'."
                                 % (expected_status, header))
