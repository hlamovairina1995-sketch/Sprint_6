import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--headless', action='store_true', default=False,
        help='Запуск Firefox без графического интерфейса',
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        item.rep_call = report


@pytest.fixture
def driver(request):
    options = Options()
    if request.config.getoption('--headless'):
        options.add_argument('-headless')

    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)
    try:
        yield browser
    finally:
        if getattr(request.node, 'rep_call', None) and request.node.rep_call.failed:
            allure.attach(
                browser.get_screenshot_as_png(),
                name='Скриншот при падении теста',
                attachment_type=allure.attachment_type.PNG,
            )
        browser.quit()