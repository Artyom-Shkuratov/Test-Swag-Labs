import pytest
from helpers import GeneratorData as GD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data.users import UsersLogin, UsersPassword

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--incognito")
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")
    opts.add_argument("--disable-search-engine-choice-screen")
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False,
    })
    opts.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerOnboarding,PasswordCheck,PasswordImport,AutofillServerCommunication")

    drv = webdriver.Chrome(options=opts)
    yield drv
    drv.quit()
    
@pytest.fixture 
def get_random_login():
    return GD.get_random_login()


@pytest.fixture
def get_password():
    return GD.get_password()

@pytest.fixture
def successful_credentials():
    return UsersLogin.STANDARD, UsersPassword.PASSWORD