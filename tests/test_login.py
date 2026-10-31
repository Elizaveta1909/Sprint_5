from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HEADER_SIGN_IN_BUTTON, LOGIN_SUBMIT_BUTTON, EMAIL_INPUT, PASSWORD_INPUT, SIGN_OUT_BUTTON, USER_AVATAR, USER_NAME_LABEL

class TestLogin:
    def test_login(self, driver, login_existing_email):
        wait = WebDriverWait(driver, 7)

        wait.until(EC.element_to_be_clickable(HEADER_SIGN_IN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(login_existing_email)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("123")
        wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()
        
        wait.until(EC.visibility_of_element_located(USER_AVATAR))
        assert driver.find_element(*USER_AVATAR).is_displayed()
        assert driver.find_element(*USER_NAME_LABEL).is_displayed()
        
    def test_logout(self, driver, login_existing_email):
            wait = WebDriverWait(driver, 7)
    
            wait.until(EC.element_to_be_clickable(HEADER_SIGN_IN_BUTTON)).click()
            wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(login_existing_email)
            wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("123")
            wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()
            wait.until(EC.visibility_of_element_located(USER_AVATAR))
            
            wait.until(EC.element_to_be_clickable(SIGN_OUT_BUTTON)).click()
            
            assert wait.until(EC.visibility_of_element_located(HEADER_SIGN_IN_BUTTON)).is_displayed()
            
            
    