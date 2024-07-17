import time
from selenium import webdriver

import pytest


@pytest.fixture()
def init_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com")
    # driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    driver.maximize_window()
    time.sleep(2)
    print("setup method")
    request.cls.driver = driver

    yield
    driver.close()
    print("teardown")
