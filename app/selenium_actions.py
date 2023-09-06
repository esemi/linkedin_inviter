"""Selenium webdriver actions."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from app.settings import app_settings


def create_browser() -> WebDriver:
    """Create browser."""
    options = [
        f'user-data-dir={app_settings.session_path}',
        'start-maximized',
        'disable-infobars',
        '--disable-extensions',
        '--disable-dev-shm-usage',
        '--no-sandbox',
        '--headless',
    ]
    chrome_options = Options()
    for option in options:
        chrome_options.add_argument(option)

    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    browser.implicitly_wait(app_settings.timeout_default)
    return browser


def highlight(browser: WebDriver, element: WebElement):
    """Highlights a Selenium Webdriver element."""
    browser.execute_script(
        "arguments[0].setAttribute('style', arguments[1]);",
        element,
        'border: 2px solid red;',
    )


def click(browser: WebDriver, element: WebElement):
    """Click on element by javascript."""
    browser.execute_script('arguments[0].click();', element)
