from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Selenium_automation.Pages.loginpage  import LoginPage
from Selenium_automation.Pages.homepage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome('/Users/shefalikamalnakhawa/Desktop/Selenium_automation/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        time.sleep(5)

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(5)

        homepage = HomePage(driver)
        homepage.click_welcome()
        time.sleep(5)
        homepage.click_logout()
        time.sleep(5)


    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/shefalikamalnakhawa/Desktop/Selenium_automation/reports'))