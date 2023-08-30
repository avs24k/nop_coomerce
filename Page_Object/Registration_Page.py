from selenium.webdriver.common.by import By


class test_regipage:

    def __init__(self, driver):
        self.driver = driver

        self.user_regi_button_linktext = "Register"
        self.user_select_gender_xpath = "//div[@id='gender']//label"
        self.user_first_name = "FirstName"
        self.user_last_name = "LastName"
        self.user_dob_day_name = "DateOfBirthDay"
        self.user_dob_month_name = "DateOfBirthMonth"
        self.user_dob_year_name = "DateOfBirthYear"
        self.user_email = "Email"
        self.company_name = "Company"
        self.Password = "Password"
        self.confpassword = "ConfirmPassword"
        self.click1 = "register-button"
        self.succes_message  = "//div[@class='result']"
        self.failure_msg = "//div[@class='message-error validation-summary-errors']/ul/li"
        self.click2 = "a[class*='button-1']"
        self.click3 = "img[alt='nopCommerce demo store']"


    def user_regi_button(self):
        self.driver.find_element(By.LINK_TEXT,self.user_regi_button_linktext).click()

    # def user_gender(self):
    #     self.driver.find_elements(By.XPATH, self.user_select_gender_xpath)


    def user_first_name_click(self):
        self.driver.find_element(By.ID, self.user_first_name).click()

    def user_first_name_type(self,First_Name):
        self.driver.find_element(By.ID, self.user_first_name).send_keys(First_Name)

    def user_last_name_click(self):
        self.driver.find_element(By.ID,self.user_last_name).click()

    def user_last_name_type(self, Last_name):
        self.driver.find_element(By.ID,self.user_last_name).send_keys(Last_name)

    def user_dob_day(self):
        self.driver.find_element(By.NAME,self.user_dob_day_name).click()

    def user_dob_type_day(self,Day):
        self.driver.find_element(By.NAME,self.user_dob_day_name).send_keys(Day)

    def user_dob_month(self):
        self.driver.find_element(By.NAME,self.user_dob_month_name).click()

    def user_dob_month_type(self,Month):
        self.driver.find_element(By.NAME,self.user_dob_month_name).send_keys(Month)

    def user_dob_year(self):
        self.driver.find_element(By.NAME,self.user_dob_year_name).click()

    def user_dob_year_type(self,Year):
        self.driver.find_element(By.NAME,self.user_dob_year_name).send_keys(Year)

    def user_email_01(self,Email):
        self.driver.find_element(By.ID,self.user_email).send_keys(Email)

    def user_company(self,Company_Name):
        self.driver.find_element(By.ID,self.company_name).send_keys(Company_Name)

    def user_password(self,Password):
        self.driver.find_element(By.ID,self.Password).send_keys(Password)

    def user_Confirm_password(self, ConPassword):
        self.driver.find_element(By.ID,self.confpassword).send_keys(ConPassword)

    def user_regi_button_click(self):
        self.driver.find_element(By.ID,self.click1).click()

    def user_succes_msg(self):
        return self.driver.find_element(By.XPATH,self.succes_message).text

    def user_failure_msg(self):
        return self.driver.find_element(By.XPATH,self.failure_msg).text

    def user_button_click2(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click2).click()

    def user_button_click3(self):
        self.driver.find_element(By.CSS_SELECTOR,self.click3).click()

    def user_gender(self):
        genders_available = self.driver.find_elements(By.XPATH, self.user_select_gender_xpath)
        # Logic to retrieve genders
        if genders_available:
            return genders_available
        else:
            return []  # Return an empty list if no genders are available





