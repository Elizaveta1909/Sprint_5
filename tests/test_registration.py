from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HEADER_SIGN_IN_BUTTON, NO_ACCOUNT_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, PASSWORD_REPEAT_INPUT, CREATE_ACCOUNT_BUTTON, USER_AVATAR, EMAIL_ERROR_MESSAGE, USER_NAME_LABEL, REGISTRATION_FORM_TITLE


class TestSignIn:
    def test_sign_in(self, driver, email):
        wait = WebDriverWait(driver, 7)

        wait.until(EC.element_to_be_clickable(HEADER_SIGN_IN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_TITLE))
        
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(email)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("123")
        wait.until(EC.visibility_of_element_located(PASSWORD_REPEAT_INPUT)).send_keys("123")
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(USER_AVATAR))
        
        assert driver.current_url == "https://qa-desk.education-services.ru/regiatration"
        assert driver.find_element(*USER_AVATAR).is_displayed()
        assert driver.find_element(*USER_NAME_LABEL).is_displayed()
        
    def test_error_sign_in(self, driver, wrong_email):
        wait = WebDriverWait(driver, 7)
        
        wait.until(EC.element_to_be_clickable(HEADER_SIGN_IN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_TITLE))
        
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(wrong_email)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("456")
        wait.until(EC.visibility_of_element_located(PASSWORD_REPEAT_INPUT)).send_keys("456")
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()
        error = wait.until(EC.visibility_of_element_located(EMAIL_ERROR_MESSAGE))
        
        assert error.text == "Ошибка"
        
    def test_existing_user(self, driver, login_existing_email):
        wait = WebDriverWait(driver, 7)

        wait.until(EC.element_to_be_clickable(HEADER_SIGN_IN_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(REGISTRATION_FORM_TITLE))
        
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(login_existing_email)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("123")
        wait.until(EC.visibility_of_element_located(PASSWORD_REPEAT_INPUT)).send_keys("123")
        wait.until(EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)).click()
        error = wait.until(EC.visibility_of_element_located(EMAIL_ERROR_MESSAGE))

        assert error.text == "Ошибка"