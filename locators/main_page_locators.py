from selenium.webdriver.common.by import By

class MainPageLocators:
   
    ITEM_CARD = (By.CSS_SELECTOR, "div[data-test='inventory-item']")
    ITEM_IMAGE = (By.CSS_SELECTOR, "a[data-test='item-4-img-link'] img")
    ITEM_NAME = (By.CSS_SELECTOR, "div[data-test='inventory-item-name']")
    ITEM_DESC = (By.CSS_SELECTOR, "div[data-test='inventory-item-desc']")
    ITEM_PRICE = (By.CSS_SELECTOR, "div[data-test='inventory-item-price']")
   
    
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    ALL_ITEMS_BUTTON = (By.CSS_SELECTOR, "a[data-test='inventory-sidebar-link']")
    ABOUT_BUTTON = (By.CSS_SELECTOR, "a[data-test='about-sidebar-link']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[data-test='logout-sidebar-link']")
    RESET_APPBUTTON = (By.CSS_SELECTOR, "a[data-test='reset-sidebar-link']")
    
    