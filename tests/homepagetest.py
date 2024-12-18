from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.homePage import homePage


class homepageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)


    def load_url(self):
        self.driver.get("https://the-internet.herokuapp.com/")


    def test_input(self):
        driver = self.driver
        self.load_url()
        home = homePage(driver)
        home.click_input_link()
        driver.find_element(By.XPATH, "//input").send_keys(10)
        time.sleep(3)


    def test_checkbox(self):
        driver = self.driver
        self.load_url()
        home = homePage(driver)
        home.click_checkbox_link()
        driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]").click()  
        time.sleep(3)


    def test_dropdown(self):
        driver = self.driver
        self.load_url()
        home = homePage(driver)
        home.click_dropdown_link()

        dropdown = self.driver.find_element(By.TAG_NAME, "select")
        select = Select(dropdown)
        select.select_by_visible_text("Option 1")
        time.sleep(3)


    def test_window(self):
        driver = self.driver
        self.load_url()
        home = homePage(driver)
        home.click_window_link()
        time.sleep(3)
        label = driver.find_element(By.CSS_SELECTOR, "h3").text
        assert label == "Opening a new window"

        driver.find_element(By.XPATH, "//div[@id='content']//a").click()
        time.sleep(4)
        tab = driver.window_handles
        driver.switch_to.window(tab[1])
        title = driver.find_element(By.CSS_SELECTOR, "body > div > h3").text
        assert title == "New Window"
        driver.switch_to.window(tab[0])


    def test_form(self):
        driver = self.driver
        self.load_url()
        home = homePage(driver)
        home.click_form_link()
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "#login > button > i").click()

        successmessage = driver.find_element(By.CSS_SELECTOR, "#content > div > h4").text
        assert successmessage == "Welcome to the Secure Area. When you are done click logout below."

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")