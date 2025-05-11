

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()  # Add executable_path if needed
    yield driver
    driver.quit()


def test_swag_labs_login(driver):
    driver.get("https://www.saucedemo.com/")

    # Enter username
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # Enter password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # Click login button
    driver.find_element(By.ID, "login-button").click()

    # Assert successful login by checking for a page element only visible after login
    assert "inventory" in driver.current_url
    # Optionally, check for the presence of the inventory container
    assert driver.find_element(By.ID, "inventory_container")