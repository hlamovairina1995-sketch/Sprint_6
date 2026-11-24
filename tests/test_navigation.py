import allure

from config import BASE_URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Переходы по логотипам')
class TestNavigation:
    @allure.title('Логотип Самоката возвращает на главную страницу')
    def test_scooter_logo_opens_home(self, driver):
        page = MainPage(driver).open_main_page()
        page.start_order('top')
        OrderPage(driver).click_scooter_logo()

        assert page.get_current_url().rstrip('/') == BASE_URL.rstrip('/')
        assert page.is_home_page_open()

    @allure.title('Логотип Яндекса открывает Дзен в новой вкладке')
    def test_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver).open_main_page()
        original_handles = page.get_window_handles()
        page.click_yandex_logo()

        page.switch_to_new_window(original_handles)

        page.wait_for_url('dzen.ru', timeout=25)
        assert 'dzen.ru' in page.get_current_url().lower()
