
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def setup(request):
    obj_service = Service("Driver/chromedriver.exe")
    driver = webdriver.Chrome(service=obj_service)
    driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
    driver.implicitly_wait(20)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()