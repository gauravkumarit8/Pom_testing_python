import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:

    def __init__(self, driver):
        self.driver = driver
        self.lnkCustomers_menu = (By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/i")
        self.lnkCustomers_menuitem = (By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p")
        self.btnAddnew = (By.XPATH, "/html/body/div[3]/div[1]/form[1]/div/div/a")
        self.txtEmail = (By.XPATH, "//input[@id='Email']")
        self.txtPassword = (By.XPATH, "//input[@id='Password']")
        self.txtcustomerRoles = (By.CLASS_NAME, "k-multiselect-wrap k-floatwrap")
        self.lstitemAdministrators = (By.XPATH, "//li[contains(text(),'Administrators')]")
        self.lstitemRegistered = (By.XPATH, "//li[contains(text(),'Registered')]")
        self.lstitemGuests = (By.XPATH, "//li[contains(text(),'Guests')]")
        self.lstitemVendors = (By.XPATH, "//li[contains(text(),'Vendors')]")
        self.drpmgrOfVendor = (By.XPATH, "//*[@id='VendorId']")
        self.rdMaleGender = (By.ID, "Gender_Male")
        self.rdFeMaleGender = (By.ID, "Gender_Female")
        self.txtFirstName = (By.XPATH, "//input[@id='FirstName']")
        self.txtLastName = (By.XPATH, "//input[@id='LastName']")
        self.txtDob = (By.XPATH, "//input[@id='DateOfBirth']")
        self.txtCompanyName = (By.XPATH, "//input[@id='Company']")
        self.txtAdminContent = (By.XPATH, "//textarea[@id='AdminComment']")
        self.btnSave = (By.XPATH, "//button[@name='save']")

    def clickOnCustomersMenu(self):
        self.driver.find_element(*self.lnkCustomers_menu).click()

    def clickOnCustomersMenuItems(self):
        self.driver.find_element(*self.lnkCustomers_menuitem).click()

    def clickOnAddnew(self):
        self.driver.find_element(*self.btnAddnew).click()

    def setEmail(self, email):
        self.driver.find_element(*self.txtEmail).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(*self.txtPassword).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(*self.txtcustomerRoles).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(*self.lstitemRegistered)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(*self.lstitemAdministrators)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(*self.lstitemGuests)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(*self.lstitemRegistered)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(*self.lstitemVendors)
        else:
            self.listitem = self.driver.find_element(*self.lstitemGuests)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", *self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(*self.drpmgrOfVendor))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(*self.rdMaleGender).click()
        elif gender == "Female":
            self.driver.find_element(*self.rdFeMaleGender).click()
        else:
            self.driver.find_element(*self.rdMaleGender).click()

    def setFirstName(self, fname):
        self.driver.find_element(*self.txtFirstName).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*self.txtLastName).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(*self.txtDob).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(*self.txtCompanyName).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(*self.txtAdminContent).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave).click()
