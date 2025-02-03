import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginActions
from utilities.customLogger import LogGen

class Test_001_Login:

        base_url = ReadConfig.getBaseUrl()
        username = ReadConfig.getUsername()
        password = ReadConfig.getPassword()

        logger = LogGen.logGen()

        @pytest.mark.sanity
        def test_HomePageTitle(self,setup):

            self.logger.info("**********Test_001_Login************")
            self.logger.info("***********Verifying Home Page Title************")
            self.driver = setup
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.act_title = self.driver.title
            time.sleep(2)
            if self.act_title == "OrangeHRM1238":
                assert True
                self.driver.close()
                self.logger.info("***********Home Page Title is Passed************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\"+"failedTitle.png")
                self.driver.close()
                self.logger.debug("***********Home Page Title is Failed************")
                assert False

        @pytest.mark.sanity
        @pytest.mark.regression   
        def test_Login(self,setup):
            self.logger.info("***********Verifying Login Test************")
            self.driver = setup
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.lp = LoginActions(self.driver)
            self.lp.enterUserName(self.username)
            self.lp.enterPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.act_title = self.driver.title
            if self.act_title == "OrangeHRM":
                assert True
                self.driver.close()
                self.logger.info("***********Login Test is Passed************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\failedLogin.png")
                self.driver.close()
                self.logger.info("***********Login Test is Failed************")
                assert False

