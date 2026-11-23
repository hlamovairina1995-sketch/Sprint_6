import allure

from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Заполнить данные получателя заказа')
    def fill_customer_form(self, data):
        self.fill(OrderPageLocators.FIRST_NAME, data['first_name'])
        self.fill(OrderPageLocators.LAST_NAME, data['last_name'])
        self.fill(OrderPageLocators.ADDRESS, data['address'])
        self.click(OrderPageLocators.METRO)
        self.click(self.format_locator(OrderPageLocators.METRO_OPTION, station=data['metro']))
        self.fill(OrderPageLocators.PHONE, data['phone'])
        self.click(OrderPageLocators.NEXT_BUTTON)
        self.find(OrderPageLocators.DELIVERY_DATE)

    @allure.step('Заполнить срок аренды, цвет и комментарий')
    def fill_rental_form(self, data):
        self.click(OrderPageLocators.DELIVERY_DATE)
        self.click(OrderPageLocators.CALENDAR_NEXT_MONTH)
        self.click(OrderPageLocators.CALENDAR_FIRST_DAY)
        self.click(OrderPageLocators.RENTAL_DROPDOWN)
        self.click(self.format_locator(OrderPageLocators.RENTAL_OPTION, duration=data['duration']))
        self.click(self.format_locator(OrderPageLocators.SCOOTER_COLOR, color=data['color']))
        self.fill(OrderPageLocators.COMMENT, data['comment'])

    @allure.step('Подтвердить оформление заказа')
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Прочитать сообщение об успешном заказе')
    def get_success_message(self):
        return self.find(OrderPageLocators.SUCCESS_MESSAGE).text
