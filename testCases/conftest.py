# from selenium import webdriver
# import pytest
#
# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome()
#     return driver

import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome() #in case if the user donot pass the browser then default browser will be
    return driver
 # to run multiple test in browser parallely we have to pass the command 'pytest -v -s -n=3 testCases/test_login.py --browser chrome'

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# give the cli as 'pytest -v -s testCases/test_login.py --browser chrome'

########### pytest HTML Report ################
# without this we can also generate the html report
# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Gaurav'
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

    # to generte the html report we have to use the folloeing cli command
    # pytest -s -v --html=Reports\report.html testCases/test_login.py