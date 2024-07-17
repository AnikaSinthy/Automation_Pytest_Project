import time
from selenium import webdriver
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
