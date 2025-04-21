import sys
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import pprint
from chromedriver_py import binary_path


from selenium import webdriver

def get_chrome_options(headless=True, window_size="1900,800", user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"window-size={window_size}")

    if user_agent:
        options.add_argument(f"user-agent={user_agent}")

    return options

def create_driver(headless=True, window_size="1900,800", user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"):
    options = get_chrome_options(headless, window_size, user_agent)
    service = Service(ChromeDriverManager().install())  # Create a Service object with the path to the ChromeDriver executable
    wd = webdriver.Chrome(service=service, options=options)  # Initialize the WebDriver with the specified service and options
    return wd

