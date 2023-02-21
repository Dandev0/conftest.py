import selenium
from selenium import webdriver
import pytest

driver= webdriver.Chrome()
url = 'https://bms.ujin.tech/auth'
driver.get(url)