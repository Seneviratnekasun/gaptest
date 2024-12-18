from selenium.webdriver.common.by import By

class homePage():

    def __init__(self, driver):
        self.driver = driver

        self.inputs_link_xpath = "//div[@id='content']/ul/li/a[contains(text(), 'Inputs')]"
        self.checkboxes_link_xpath = "//div[@id='content']/ul/li/a[contains(text(), 'Checkboxes')]"
        self.dropdown_link_xpath = "//div[@id='content']/ul/li/a[contains(text(), 'Dropdown')]"
        self.window_link_css = "#content > ul > li:nth-child(33) > a"
        self.form_auth_link_xpath = "//div[@id='content']/ul/li/a[contains(text(), 'Form Authentication')]"


    def click_input_link(self):
        self.driver.find_element(By.XPATH, self.inputs_link_xpath).click()

    def click_checkbox_link(self):
        self.driver.find_element(By.XPATH, self.checkboxes_link_xpath).click()

    def click_dropdown_link(self):
        self.driver.find_element(By.XPATH, self.dropdown_link_xpath).click()

    def click_window_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.window_link_css).click()

    def click_form_link(self):
        self.driver.find_element(By.XPATH, self.form_auth_link_xpath).click()