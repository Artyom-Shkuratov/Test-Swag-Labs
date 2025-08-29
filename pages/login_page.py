import allure
from pages.base_page import BasePage
from urls import Urls
from locators.login_page_locator import LoginPageLocators as LPL


class LoginPage(BasePage):
    
    @allure.step('Открыть страницу логина')
    def open_login_page(self):
        self.open_url(Urls.BASE_URL)
    
    @allure.step('Заполнить поле username')
    def fill_username(self, username):  
        self.fill_placeholder(LPL.INPUT_USERNAME, username)
        
    @allure.step('Заполнить поле password')
    def fill_password(self, password):  
        self.fill_placeholder(LPL.INPUT_PASSWORD, password)
        
    @allure.step('Клик по кнопке логина')
    def click_login_button(self):
        self.find_element(LPL.LOGIN_BUTTON).click()

    @allure.step('Проверка отображения кнопки логина')
    def should_be_login_button(self):
       self.wait_for_element(LPL.LOGIN_BUTTON)
    
    @allure.step("Проверить отображение кнопки Login")
    def is_login_button_displayed(self):
        return self.check_displaying_of_element(LPL.LOGIN_BUTTON)
    
    @allure.step('Логин рандомного пользователя')
    def login_user(self, username, password):
        self.open_login_page()
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
    @allure.step('Логин  пользователя')
    def login_standard_user(self):
        self.open_login_page()
        self.fill_username("standard_user")
        self.fill_password("secret_sauce")
        self.click_login_button()
        
    @allure.step('Ожидание загрузки страницы логина')
    def wait_for_login_page_to_load(self):
        self.wait_for_element(LPL.LOGIN_BUTTON)
        self.check_element_is_clickable(LPL.LOGIN_BUTTON)
    
   