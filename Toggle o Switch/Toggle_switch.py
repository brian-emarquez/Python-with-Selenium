# Boton On/Off


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Automatizacion\driverchrome\chromedriver.exe")

    def test_usando_toggle(self):
        driver = self.driver #llamda al driver
        driver.get("https://www.google.com")
        