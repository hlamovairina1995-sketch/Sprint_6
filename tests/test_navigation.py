import allure
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Переходы по логотипам')
class TestNavigation:
    @allure.title('Логотип Самоката возвращает на главную страницу')
    def test_scooter_logo_opens_home(self, driver):
        MainPage(driver).open().start_order('top')
        OrderPage(driver).click_scooter_logo()

        assert driver.current_url.rstrip('/') == BASE_URL.rstrip('/')
        assert MainPage(driver).is_home_page_open()

    @allure.title('Логотип Яндекса открывает Дзен в новой вкладке')
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver).open()
        original_window = driver.current_window_handle
        page.click_yandex_logo()

        WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) == 2)
        handles = driver.window_handles
        handles.remove(original_window)
        driver.switch_to.window(handles[0])

        WebDriverWait(driver, 25).until(lambda d: 'dzen.ru' in d.current_url.lower())
        assert 'dzen.ru' in driver.current_url.lower()