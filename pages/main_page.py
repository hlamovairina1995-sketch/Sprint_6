import allure

from config import BASE_URL
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Открыть главную страницу Самоката')
    def open_main_page(self):
        self.open(BASE_URL)
        self.find(MainPageLocators.FAQ_TITLE)
        self.accept_cookies()
        return self

    def accept_cookies(self):
        buttons = self.find_elements(MainPageLocators.COOKIE_BUTTON)
        if buttons and buttons[0].is_displayed():
            buttons[0].click()

    @allure.step('Открыть оформление заказа через кнопку: {entry_point}')
    def start_order(self, entry_point):
        if entry_point == 'top':
            self.click(MainPageLocators.TOP_ORDER_BUTTON)
        elif entry_point == 'bottom':
            self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)
        else:
            raise ValueError(f'Неизвестная точка входа: {entry_point}')
        self.wait_for_url('/order')

    @allure.step('Раскрыть вопрос № {index} и получить его ответ')
    def open_faq(self, index):
        questions = self.find_all(MainPageLocators.FAQ_QUESTIONS)
        question = questions[index]
        question_text = question.text
        panel_id = question.get_attribute('aria-controls')
        self.click_element_near_right_edge(question)
        answer = self.find(MainPageLocators.faq_answer(panel_id))
        return question_text, answer.text

    def is_home_page_open(self):
        return self.find(MainPageLocators.FAQ_TITLE).is_displayed()
