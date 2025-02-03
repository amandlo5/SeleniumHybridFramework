import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginActions
from utilities.customLogger import LogGen
from pageObjects.AddNewCanditate import AddCandidate
from pageObjects.SearchCustomerPage import SearchCustomer

class Test_004_Search_Canditate:

    base_url = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    @pytest.mark.regression
    def testSearchCanditate(self,setup):
        self.driver = setup
        self.logger.info("**************Test_003_SearchCanditate************")
        self.logger.info("***********Searching New Canditate Test************")
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginActions(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.nc = AddCandidate(self.driver)
        self.nc.clickRecruitment()

        self.sc = SearchCustomer(self.driver)
        self.sc.setName('John')
        time.sleep(2)
        self.sc.clickSearch()
        status = self.sc.searchCanditateByName('John')
        assert True == status
        time.sleep(3)
        self.logger.info("***********Test case 004 is passed*************")



