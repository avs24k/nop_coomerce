import time
from Page_Object.Registration_Page import test_regipage
from Testing_Files.basefile import Base_class
from Utilities.Logg_file import classname
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


class Test_Regi001(Base_class, classname):
    def test_001(self):
        rp = test_regipage(self.driver)
        log = self.getlogs()

        rp.user_regi_button()
        log.info("click on registration page")

        self.select_genders(rp.user_gender(), "Male")
        log.info("select gender")
        time.sleep(3)

        rp.user_first_name_click()
        log.info("click on first name button")
        time.sleep(2)

        rp.user_first_name_type(config.get("User_Info", "First_name"))
        log.info("type first name successfully")

        rp.user_last_name_click()
        log.info("click on last name button")
        time.sleep(2)

        rp.user_last_name_type(config.get("User_Info", "Last_Name"))
        log.info("type last name successfully")

        rp.user_dob_day()
        log.info("click on day")

        rp.user_dob_type_day(config.get("User_Info", "Day"))
        log.info(" type day Successfully")

        rp.user_dob_month()
        log.info(" click on month")

        rp.user_dob_month_type(config.get("User_Info", "Month"))
        log.info(" type on month Successfully")

        rp.user_dob_year()
        log.info(" click on year")

        rp.user_dob_year_type(config.get("User_Info", "Year"))
        log.info(" type on year Successfully")

        rp.user_email_01(config.get("User_Info", "Email"))
        log.info(" type Email Successfully")

        rp.user_company(config.get("User_Info", "Company_name"))
        log.info(" type Company Name Successfully")

        rp.user_password(config.get("User_Info", "Password"))
        log.info(" type Password Successfully")

        rp.user_Confirm_password(config.get("User_Info", "Conf_pass"))
        log.info(" type Conf-Password Successfully")

        rp.user_regi_button_click()
        log.info(" click on reg-button")
        time.sleep(3)

        try:
            failure = rp.user_failure_msg()
            if "The specified email already exists" in failure:
                print("True")
                log.info("User Already Exist msg")
            else:
                print(False)
                log.info("User not Exist msg")
        except :
            succesfull = rp.user_succes_msg()
            if "Your registration completed" in succesfull:
                print("true")
                log.info("User login successfully msg")
            else:
                print("false")
                log.info("User login Fail msg")
            time.sleep(3)
            rp.user_button_click2()
            log.info("User click on Continue msg")

            rp.user_button_click3()
            log.info("User click on Home Logo")

# driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()
# time.sleep(2)
# driver.find_element(By.ID,"Email").click()
# driver.find_element(By.ID,"Email").send_keys("avinash@gmail.com")
# driver.find_element(By.ID,"Password").click()
# driver.find_element(By.ID,"Password").send_keys("Avinash123")
