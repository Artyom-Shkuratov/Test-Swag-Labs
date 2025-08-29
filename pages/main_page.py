import allure
from pages.base_page import BasePage
from urls import Urls
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators as MPL


class MainPage(BasePage):
    
    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_url(Urls.INVENTORY_URL)    
        
    @allure.step('Ожидания загрузки главной страницы')
    def wait_for_main_page_to_load(self, timeout: int = 15):
        self.wait.until(EC.url_contains("/inventory.html"))
        self.wait_for_element(MPL.ITEM_CARD)
    
    @allure.step('Клик по кнопке меню')
    def click_menu_button(self):
        self.wait_for_element(MPL.MENU_BUTTON)
        self.click_element(MPL.MENU_BUTTON)
        self.wait_for_element(MPL.MENU_BUTTON)

    @allure.step('Клик по кнопке Logout')
    def click_logout_button(self):
        self.wait_for_element(MPL.LOGOUT_BUTTON)
        self.click_element(MPL.LOGOUT_BUTTON)

    @allure.step('Выйти из аккаунта')
    def logout_user(self):
        self.click_menu_button()
        self.click_logout_button()
        