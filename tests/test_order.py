import allure
import pytest

from data import ORDER_CASES
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Оформление заказа')
class TestOrder:
    @allure.title('Успешный заказ через кнопку: {order_data[entry_point]}')
    @pytest.mark.parametrize(
        'order_data',
        ORDER_CASES,
        ids=['top-button', 'bottom-button'],
    )
    def test_successful_order(self, driver, order_data):
        main = MainPage(driver)
        main.open_main_page()
        main.start_order(order_data['entry_point'])
        
        order = OrderPage(driver)
        order.fill_customer_form(order_data)
        order.fill_rental_form(order_data)
        order.submit_order()

        assert 'Заказ оформлен' in order.get_success_message()