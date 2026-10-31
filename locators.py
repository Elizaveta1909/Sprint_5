from selenium.webdriver.common.by import By

# ---------- Кнопки ----------
HEADER_SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()= 'Нет аккаунта']")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
SIGN_OUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выйти']")
CREATE_AD_BUTTON = (By.XPATH, "//button[normalize-space()='Разместить объявление']")
PUBLISH_AD_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")

# ---------- Поля: регистрация и логин ----------
EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[1]")
PASSWORD_REPEAT_INPUT = (By.XPATH, "(//input[@type='password'])[2]")

# ---------- Поля: создание объявления ----------
AD_TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Название']")
AD_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
AD_PRICE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Стоимость']")
AD_CATEGORY_ARROW = (By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrow')])[1]")
AD_CITY_ARROW = (By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrow')])[2]")
AD_RADIO_ACTIVE = (By.CSS_SELECTOR, "div[class*='radioUnput_inputActive']")
AD_CONDITION_RADIO_USED = (By.XPATH, "//input[@type='radio'][2]")
AD_TITLE_TEXT = (By.CSS_SELECTOR, "div.card div.about h2.h2")

# ---------- Элементы для проверок (assert) ----------
USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
USER_NAME_LABEL = (By.CSS_SELECTOR, "h3.profileText.name")
EMAIL_ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'input_span') and normalize-space()='Ошибка']")
AUTH_REQUIRED_MODAL_TITLE = (By.XPATH, "//*[normalize-space()='Чтобы разместить объявление, авторизуйтесь']")
MY_ADS_BLOCK = (By.XPATH, "//h1[normalize-space()='Мои объявления']")


AD_CATEGORY_TECH_OPTION = (By.XPATH, "//span[contains(@class, 'dropDownMenu_textColor') and normalize-space()='Технологии']")
AD_CITY_MOSCOW_OPTION = (By.XPATH, "//span[contains(@class, 'dropDownMenu_textColor') and normalize-space()='Москва']")

REGISTRATION_FORM_TITLE = (By.XPATH, "//h1[normalize-space()='Зарегистрироваться']")

