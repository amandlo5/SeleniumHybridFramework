import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginActions
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_002_LoginData:

        base_url = ReadConfig.getBaseUrl()
        path = ReadConfig.getFilePath()

        logger = LogGen.logGen()

        @pytest.mark.sanity
        def test_Login_ddt(self,setup):
            self.logger.info("**************Test_002_LoginData************")
            self.logger.info("***********Verifying Login DDT Test************")
            self.driver = setup
            self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.lp = LoginActions(self.driver)

            self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
            result = []  #created empty list
            for r in range(2,self.rows+1):

                self.username = ExcelUtils.readData(self.path,'Sheet1',r,1)
                self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
                self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

                self.lp.enterUserName(self.username)
                self.lp.enterPassword(self.password)
                self.lp.clickLogin()
                time.sleep(5)

                self.act_title = self.driver.title
                self.exp_title = "OrangeHRM"

                if self.act_title == self.exp_title:
                    if self.exp == "Pass":
                        self.logger.info("******Test Passed")
                        self.lp.clickLogout()
                        result.append('Pass')
                    elif self.exp == 'Fail':
                        self.logger.info("******Test Failed")
                        # self.lp.clickLogout()
                        result.append('Pass')
                elif self.act_title != self.exp_title:
                    if self.exp == 'Pass':
                        self.logger.info("***Failed")
                        result.append('Fail')
                    elif self.exp == 'Fail':
                        self.logger.info("***Passed")
                        result.append('Pass')
            print(result)

            if 'Fail' not in result:
                self.logger.info("***********Test is Passed***********")
                self.driver.close()
                assert True
            else:
                self.logger.info("************Test is Failed*********")
                self.driver.close()
                assert False
            self.logger.info("***********End of Login DDT Test*******************")



