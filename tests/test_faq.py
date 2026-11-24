import allure
import pytest

from data import FAQ_CASES
from pages.main_page import MainPage


@allure.feature('Вопросы о важном')
class TestFaq:
    @pytest.mark.parametrize(
        'index, expected_question, expected_answer',
        [(index, question, answer) for index, (question, answer) in enumerate(FAQ_CASES)],
        ids=[f'faq-{i + 1}' for i in range(len(FAQ_CASES))],
    )
    @allure.title('Вопрос № {index}: отображается правильный ответ')
    def test_faq_answer(self, driver, index, expected_question, expected_answer):
        page = MainPage(driver).open_main_page()
        actual_question, actual_answer = page.open_faq(index)

        assert actual_question == expected_question
        assert actual_answer == expected_answer
