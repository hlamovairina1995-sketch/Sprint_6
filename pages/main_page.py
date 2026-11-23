import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import BASE_URL
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Открыть главную страницу Самоката')
    def open(self):
        self.driver.get(BASE_URL)
        self.find(MainPageLocators.FAQ_TITLE)
        self.accept_cookies()
        return self

    def accept_cookies(self):
        buttons = self.driver.find_elements(*MainPageLocators.COOKIE_BUTTON)
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
        self.wait.until(EC.url_contains('/order'))

    @allure.step('Раскрыть вопрос № {index} и получить его ответ')
    def open_faq(self, index):
        questions = self.wait.until(
            EC.visibility_of_all_elements_located(MainPageLocators.FAQ_QUESTIONS)
        )
        question = questions[index]
        question_text = question.text
        panel_id = question.get_attribute('aria-controls')
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', question)
        offset_x = int(question.size['width'] / 2) - 20
        ActionChains(self.driver).move_to_element_with_offset(question, offset_x, 0).click().perform()
        answer = self.find(MainPageLocators.faq_answer(panel_id))
        return question_text, answer.text

    def is_home_page_open(self):
        return self.find(MainPageLocators.FAQ_TITLE).is_displayed()