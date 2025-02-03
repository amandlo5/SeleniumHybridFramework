import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class SearchCustomer:

    xpath_name = "//div[@class='oxd-autocomplete-wrapper']/div/input"
    xpath_search = "//div[@class='oxd-form-actions']/button[2]"
    table_xpath = "//div[@class='orangehrm-container']/div"
    table_row = "//div[@class='oxd-table-body']/div"
    column_xpath = "//div[@class='oxd-table-body']/div[4]/div/div"


    def __init__(self,driver):
        self.driver = driver

    def setName(self,name):
        a = self.driver.find_element(By.XPATH,self.xpath_name)
        time.sleep(4)
        actions = ActionChains(self.driver)
        actions.click(a).send_keys(name).pause(5).key_down(Keys.DOWN).key_down(Keys.ENTER).perform()

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.xpath_search).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_row))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.column_xpath))

    def searchCanditateByName(self,name):
        flag = False
        print(self.getNoOfRows())
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            nameid = table.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+str(r)+"]/div/div[3]").text
            if name in nameid:
                flag=True
                break
        return flag


