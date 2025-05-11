import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_remove_from_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # The product you want to add and then remove
    product_name = "Sauce Labs Backpack"

    # Add the product to cart
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        if name.strip() == product_name:
            add_button = product.find_element(By.TAG_NAME, "button")
            add_button.click()
            break
    else:
        pytest.fail(f"Product '{product_name}' not found.")

    # Go to the cart page
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Wait for cart page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )

    # Remove the product from cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    for item in cart_items:
        name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        if name.strip() == product_name:
            remove_button = item.find_element(By.TAG_NAME, "button")
            remove_button.click()
            break
    else:
        pytest.fail(f"Product '{product_name}' not found in cart to remove.")

    # Verify the product is no longer in the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert not any(product_name in item.text for item in cart_items), f"{product_name} was not removed from cart."
