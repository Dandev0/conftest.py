import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import setup

@pytest.mark.usefixtures('setup')
class TestHomepage:
    def test_homepage(self):
        pass
