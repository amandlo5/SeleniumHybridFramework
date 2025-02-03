from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Launching Chrome Browser....')
    elif browser == 'edge':
        driver = webdriver.Edge()
        print('Launching Edge Browser....')
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):    #get browser value from command line
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #this will return browser value to setup method
    return request.config.getoption("--browser")

#Environment info to html report

# def pytest_configure(config):
#     config._metadata['Project'] = 'OrangeHRM'
#     config._metadata['Tester'] = 'Amol'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('Plugins',None)