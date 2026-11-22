from selenium.webdriver.common.by import By


class HeaderLocators:
    SCOOTER_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoScooter"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a[class*="Header_LogoYandex"]')


class MainPageLocators:
    FAQ_TITLE = (By.XPATH, '//*[normalize-space()="Вопросы о важном"]')
    FAQ_QUESTIONS = (By.CSS_SELECTOR, '[id^="accordion__heading-"]')
    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, 'button[class*="Button_Button"]')
    BOTTOM_ORDER_BUTTON = (By.CSS_SELECTOR, 'button[class*="Button_Middle"]')
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    @staticmethod
    def faq_answer(panel_id):
        return By.ID, panel_id


class OrderPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    METRO = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    PHONE = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[normalize-space()="Далее"]')

    DELIVERY_DATE = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    CALENDAR_NEXT_MONTH = (By.CSS_SELECTOR, '.react-datepicker__navigation--next')
    CALENDAR_FIRST_DAY = (By.CSS_SELECTOR,'.react-datepicker__day--001:not(.react-datepicker__day--outside-month)',)
    RENTAL_DROPDOWN = (By.CSS_SELECTOR, '.Dropdown-control')
    COMMENT = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[contains(@class,"Order_Buttons")]/button[normalize-space()="Заказать"]',)
    CONFIRM_BUTTON = (By.XPATH, '//button[normalize-space()="Да"]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[contains(text(), "Заказ оформлен")]')

    @staticmethod
    def metro_option(station):
        return (
            By.XPATH,
            f'//button[contains(@class,"select-search__option")][.//*[normalize-space()="{station}"]]',
        )

    @staticmethod
    def rental_option(duration):
        return (
            By.XPATH,
            f'//div[contains(@class,"Dropdown-option") and normalize-space()="{duration}"]',
        )

    @staticmethod
    def scooter_color(color):
        return By.ID, color