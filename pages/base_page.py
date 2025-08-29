import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть страницу {url}")
    def open_url(self, url):
        self.driver.get(url)
        
    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Проверить кликабельность элемента")
    def check_element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        try:
            self.check_element_is_clickable(locator).click()
        except ElementClickInterceptedException:
            element = self.wait_for_visible_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получение текущей страницы')    
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Проверка наличия элемента')
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step('Клик по элементу в chrome')
    def click_in_chrome(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
            
    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Ожидание кликабельности элемента и клик по нему')
    def wait_clikable_with_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    @allure.step('Ожидание кликабельности элемента') 
    def wait_clikable_without_click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
   
    @allure.step('Поиск элемента')   
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step('Поиск элементов')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    @allure.step('Заполнение поля ')
    def fill_placeholder(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
        
    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()
    
    @allure.step('Кликнуть по элементу через JavaScript')
    def click_element_by_js(self, locator):
        element = self.wait_for_visible_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        
    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))    
    
    @allure.step('Ожидание видимости элемента')
    def wait_until_visible(self, locator, timeout=5):
        wait = WebDriverWait(self.driver, timeout=timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
   
        
    