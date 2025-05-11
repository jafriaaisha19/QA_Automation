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

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for inventory page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # The product you want to add
    product_name = "Sauce Labs Backpack"

    # Find the product card by name and click its "Add to cart" button
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        if name.strip() == product_name:
            add_button = product.find_element(By.TAG_NAME, "button")
            add_button.click()
            break
    else:
        pytest.fail(f"Product '{product_name}' not found.")

    # Check the cart badge shows 1 item
    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1", "Cart badge does not show 1 item."

    # Go to the cart page
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify the product is in the cart
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert any(product_name in item.text for item in cart_items), f"{product_name} not found in cart."
