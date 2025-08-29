from selenium.webdriver.common.by import By
class LoginPageLocators:
    INPUT_USERNAME = (By.XPATH, ".//input[@placeholder='Username']")
    INPUT_PASSWORD = (By.XPATH, ".//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, ".//input[@data-test='login-button']")