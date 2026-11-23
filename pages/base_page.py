from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import HeaderLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url):
        self.driver.get(url)

    def format_locator(self, locator, **values):
        by, selector = locator
        return by, selector.format(**values)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url_part, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: url_part.lower() in driver.current_url.lower()
        )

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_new_window(self, original_handles):
        self.wait.until(EC.new_window_is_opened(original_handles))
        new_handle = next(
            handle for handle in self.get_window_handles()
            if handle not in original_handles
        )
        self.driver.switch_to.window(new_handle)

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()

    def click_element_near_right_edge(self, element, inset=20):
        self.scroll_to_element(element)
        offset_x = int(element.size['width'] / 2) - inset
        ActionChains(self.driver).move_to_element_with_offset(element, offset_x, 0).click().perform()

    def fill(self, locator, value):
        field = self.find(locator)
        field.clear()
        field.send_keys(value)

    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(HeaderLocators.YANDEX_LOGO)
