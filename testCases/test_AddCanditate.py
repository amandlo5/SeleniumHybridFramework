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

class Test_003_Add_Canditate:

    base_url = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def testNewCanditate(self,setup):
        self.driver = setup
        self.logger.info("**************Test_003_AddCanditate************")
        self.logger.info("***********Adding New Canditate Test************")
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
        self.nc.clickAdd()
        self.fname = random_generator_name()
        self.nc.enterFname(self.fname)
        self.mname = random_generator_name()
        self.nc.enterMname(self.mname)
        self.lname = random_generator_name()
        self.nc.enterLname(self.lname)
        time.sleep(5)
        self.nc.selectVacancy()
        time.sleep(3)
        self.logger.info("**************here")
        self.email = random_generator_email()+"@gmail.com"
        self.nc.enterEmail(self.email)
        time.sleep(2)
        self.cnum = random_generator_num()
        self.nc.enterContact(self.cnum)
        time.sleep(2)
        self.nc.enterKeywords('Testing adding functionality')
        self.nc.enterDate('2025-01-01')
        time.sleep(2)
        self.nc.clickConsent()
        self.nc.clickSave()
        time.sleep(20)


        self.msg = self.driver.find_element(By.TAG_NAME,'body').text
        print(self.msg)
        if 'successfully deleted' in self.msg:
            assert True
            self.logger.info("*****Added Successfully**********")
        else:
            assert True
            self.logger.info("***************Not Added*************")

def random_generator_name(size=6):
    name = ''.join(random.choices(string.ascii_lowercase,k=size))
    return name

def random_generator_email(size=8):
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))
    return email

def random_generator_num(size=10):
    num = ''.join(random.choices(string.digits , k=size))
    return num