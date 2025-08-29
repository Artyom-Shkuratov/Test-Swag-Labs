import allure
from urls import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage

class TestLogoutPage:
    @allure.title('Проверка успешного выхода из аккаунта')
    def test_successful_logout(self, driver, successful_credentials):
        username, password = successful_credentials
        lp = LoginPage(driver)
        mp = MainPage(driver)

        lp.open_login_page()
        lp.login_user(username, password)
        mp.wait_for_main_page_to_load()      
        mp.logout_user()

        lp.wait_for_login_page_to_load()
        assert lp.get_current_url() == Urls.BASE_URL
        assert lp.is_login_button_displayed()