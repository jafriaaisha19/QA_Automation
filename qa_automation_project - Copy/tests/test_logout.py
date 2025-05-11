import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_logout_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url

    # Open the menu
    menu_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_btn.click()

    # Wait for the sidebar menu to be present in the DOM
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "menu_button_container"))
    )

    # Wait for the sidebar (menu) to be visible (it uses a class "bm-menu-wrap" when open)
    sidebar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap"))
    )

    # Wait for the logout link to be visible and clickable
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    # Assert we're back on the login page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-button"))
    )
    assert "saucedemo.com" in driver.current_url
