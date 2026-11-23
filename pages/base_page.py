from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import HeaderLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        element.click()

    def fill(self, locator, value):
        field = self.find(locator)
        field.clear()
        field.send_keys(value)

    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(HeaderLocators.YANDEX_LOGO)