import allure
from urls import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLoginPage:
    
    @allure.title('Проверка успешного логина стандартного пользователя с рандомным выбором')
    def test_successful_login_standard_user_with_random_username_data(self, driver, get_random_login,get_password):
        page = LoginPage(driver)
        page.open_login_page()
        page.login_user(get_random_login, get_password)
        assert page.get_current_url() == Urls.INVENTORY_URL, "Не произошел переход на страницу товаров"
    
    
    @allure.title("Успешный логин стандартного пользователя")
    def test_successful_login_standard_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login_standard_user()

        assert login_page.get_current_url() == Urls.INVENTORY_URL, "Не открылась страница с товарами"
        