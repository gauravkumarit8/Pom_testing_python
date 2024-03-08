import string

from pageObjects.AddCustomer import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random


def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_003_AddCustomer:
    baseURL= ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("********** Test_003_AddCustomer ********")
        self.driver=setup
        self.driver.get(self.baseURL)

        # first login to the website to update the data
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********* Login successful *********")

        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItems()

        self.addCust.clickOnAddnew()
        self.logger.info("******** Providing the customer info ********")
        # generate the random email
        self.email= random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("Gaurav")
        self.addCust.setLastName("Kumar")
        self.addCust.setDob("8/02/2001")
        self.addCust.setCompanyName("Busy QA")
        self.addCust.setAdminContent("This is for testing")
        self.addCust.clickOnSave()

        self.logger.info("*********** Saving customer info *********")
        self.logger.info("******** Add customer validation info *******")

        self.msg= self.driver.find_element("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("******* Add customer Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_src.png")
            self.logger.error("********* Add customer Test failed *******")
            assert False

        self.driver.close()
        self.logger.info("******** Ending Add customer test ********")
