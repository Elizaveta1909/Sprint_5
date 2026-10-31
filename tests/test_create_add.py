from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import CREATE_AD_BUTTON, AUTH_REQUIRED_MODAL_TITLE, EMAIL_INPUT, PASSWORD_INPUT, HEADER_SIGN_IN_BUTTON, LOGIN_SUBMIT_BUTTON, AD_TITLE_INPUT, AD_DESCRIPTION_INPUT, AD_PRICE_INPUT
from locators import  AD_RADIO_ACTIVE, PUBLISH_AD_BUTTON, PUBLISH_AD_BUTTON, MY_ADS_BLOCK, USER_AVATAR, AD_CATEGORY_TECH_OPTION, AD_CITY_MOSCOW_OPTION
from locators import  AD_CATEGORY_ARROW, AD_CITY_ARROW, AD_TITLE_TEXT

class TestPostAdd:
    def test_post_add_new_user(self, driver):
        wait = WebDriverWait(driver, 7)

        wait.until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()
        header = wait.until(EC.visibility_of_element_located(AUTH_REQUIRED_MODAL_TITLE))
                
        assert header.text == "Чтобы разместить объявление, авторизуйтесь"
        
        
    def test_post_add_login_user(self, driver, login_existing_email):
        wait = WebDriverWait(driver, 7)
            
        wait.until(EC.element_to_be_clickable(HEADER_SIGN_IN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(EMAIL_INPUT)).send_keys(login_existing_email)
        wait.until(EC.visibility_of_element_located(PASSWORD_INPUT)).send_keys("123")
        wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(USER_AVATAR))
        
        wait.until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(AD_TITLE_INPUT)).send_keys("наушники")
        wait.until(EC.visibility_of_element_located(AD_DESCRIPTION_INPUT)).send_keys("белые")
        wait.until(EC.visibility_of_element_located(AD_PRICE_INPUT)).send_keys(5000)
        
        wait.until(EC.element_to_be_clickable(AD_CATEGORY_ARROW)).click()
        wait.until(EC.element_to_be_clickable(AD_CATEGORY_TECH_OPTION)).click()
        
        wait.until(EC.element_to_be_clickable(AD_CITY_ARROW)).click()
        wait.until(EC.element_to_be_clickable(AD_CITY_MOSCOW_OPTION)).click()
        wait.until(EC.element_to_be_clickable(AD_RADIO_ACTIVE)).click()
        wait.until(EC.element_to_be_clickable(PUBLISH_AD_BUTTON)).click()
        
        wait.until(EC.invisibility_of_element_located(AD_TITLE_INPUT))
        
        wait.until(EC.element_to_be_clickable(USER_AVATAR)).click()
        my_add = wait.until(EC.visibility_of_element_located(MY_ADS_BLOCK))
        ad = wait.until(EC.visibility_of_element_located(AD_TITLE_TEXT))

        assert my_add.is_displayed()
        assert ad.text == "наушники"