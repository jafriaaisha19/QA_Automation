# QA Automation Project

This is a Selenium WebDriver automation suite using Python, PyTest, and Pytest-HTML for test reporting.

##  Tech Stack

- **Language**: Python 3.13  
- **Automation Tool**: Selenium WebDriver  
- **Test Runner**: PyTest  
- **Reporting**: Pytest HTML Report  
- **Version Control**: Git + GitHub  

## Folder Structure

```
QA_Automation/
├── tests/               # All test cases (login, logout, add/remove cart)
├── drivers/             # ChromeDriver executable
├── reports/             # HTML test reports
├── conftest.py          # Browser setup
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.8+ installed
- Google Chrome installed
- ChromeDriver downloaded (matching your Chrome version)

### Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Your Tests

### Run All Tests + Generate Report
```bash
pytest --html=reports/report.html
```

### View Report
Open the file: `reports/report.html` in your browser.

## What Was Automated

| Test Case             | Description |
|-----------------------|-------------|
| **Login (valid credentials)** | Navigates to saucedemo.com, enters correct credentials, logs in, and verifies the inventory page. |
| **Logout** | Logs in, opens the sidebar menu, logs out, and confirms the user returns to the login screen. |
| **Add Product to Cart** | Logs in, adds "Sauce Labs Backpack" to the cart, and confirms it's listed with a quantity of 1. |
| **Remove Product from Cart** | Adds the same product, removes it from the cart, and verifies it’s no longer present. |

## Demo Video

https://drive.google.com/file/d/1yVp-rm1yjgMjNH6lcXIMPmBZsfWL3mT_/view?usp=sharing

## Author

Aaisha Jafri
