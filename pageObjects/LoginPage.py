import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginActions:

    name_username = "username"
    name_password = "password"
    xpath_login = "//button[@type='submit']"
    xpath_logout = "//ul[@class='oxd-dropdown-menu']/li[4]/a"

    def __init__(self,driver):  #initialize driver
        self.driver = driver

    def enterUserName(self,name):
        self.driver.find_element(By.NAME,self.name_username).clear()
        self.driver.find_element(By.NAME, self.name_username).send_keys(name)

    def enterPassword(self,password):
        self.driver.find_element(By.NAME,self.name_password).clear()
        self.driver.find_element(By.NAME, self.name_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.xpath_login).click()


    def clickLogout(self):
        self.driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']/i").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.xpath_logout).click()