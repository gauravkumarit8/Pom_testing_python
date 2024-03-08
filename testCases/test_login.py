from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:
    # baseURL="https://admin-demo.nopcommerce.com/"
    # username="admin@yourstore.com"
    # password="admin"
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger= LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************* Test_001_Login *******")
        self.logger.info("************* Verifying Home Page *******")
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        if actual_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home page title Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************* Home page title failed *******")
            assert False

    def test_login(self,setup):
        self.logger.info("************* Verifying Login test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce adminstration":
            assert True
            self.driver.close()
            self.logger.info("************* Login test case Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_page.png")
            self.driver.close()
            self.logger.info("************* Login test case failed *******")
            assert False

