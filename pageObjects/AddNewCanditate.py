import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

class AddCandidate:

    xpath_recruitment = "//ul[@class='oxd-main-menu']/li[5]"
    xpath_add = "//div[@class='orangehrm-header-container']/button"
    name_fname = "firstName"
    name_mname = "middleName"
    name_lname = "lastName"
    xpath_vacancy = "//div[@class='oxd-select-wrapper']/div/div"

    xpath_email = "//form[@class='oxd-form']/div[3]/div/div/div/div[2]/input"
    xpath_contact = "//form[@class='oxd-form']/div[3]/div/div[2]/div/div[2]/input"
    xpath_keywords = "//div[@class='oxd-form-row'][5]/div/div/div/div[2]/input"
    xpath_date = "//div[@class='oxd-date-input']/input"
    xpath_checkbox = "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"
    xpath_save = "//div[@class='oxd-form-actions']/button[2]"
    xpath_cancel = "//div[@class='oxd-form-actions']/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def clickRecruitment(self):
        self.driver.find_element(By.XPATH,self.xpath_recruitment).click()

    def clickAdd(self):
        self.driver.find_element(By.XPATH,self.xpath_add).click()

    def enterFname(self,fname):
        self.driver.find_element(By.NAME,self.name_fname).send_keys(fname)

    def enterMname(self,mname):
        self.driver.find_element(By.NAME,self.name_mname).send_keys(mname)

    def enterLname(self,lname):
        self.driver.find_element(By.NAME,self.name_lname).send_keys(lname)

    def selectVacancy(self):
        vacancy_element = self.driver.find_element(By.XPATH, self.xpath_vacancy)
        actions = ActionChains(self.driver)
        # Perform the repetitive key down actions in a loop

        actions.click(vacancy_element)

        for _ in range(6):
            actions.key_down(Keys.ARROW_DOWN)

        actions.key_down(Keys.ENTER).perform()
    def enterEmail(self,email):
        self.driver.find_element(By.XPATH,self.xpath_email).send_keys(email)

    def enterContact(self,cnum):
        self.driver.find_element(By.XPATH, self.xpath_contact).send_keys(cnum)

    def enterKeywords(self,key):
        self.driver.find_element(By.XPATH, self.xpath_keywords).send_keys(key)

    def enterDate(self,date):
        a = self.driver.find_element(By.XPATH, self.xpath_date)
        actions = ActionChains(self.driver)
        actions.click(a).key_down(Keys.CONTROL).send_keys('a').key_down(Keys.DELETE).perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.xpath_date).send_keys(date)

    def clickConsent(self):
        self.driver.find_element(By.XPATH,self.xpath_checkbox).click()

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.xpath_save).click()
