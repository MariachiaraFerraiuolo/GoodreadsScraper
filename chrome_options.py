import sys
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from tqdm.notebook import tqdm
import pandas as pd
import json
import pprint
from chromedriver_py import binary_path


chrome_options = webdriver.ChromeOptions()  # Initialize Chrome options
#chrome_options.add_argument('--headless')  # Run Chrome in headless mode - In our local notebook we can remove the `--headless` option.
chrome_options.add_argument('--no-sandbox')  # Disable Chrome’s default sandboxing behavior
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
chrome_options.add_argument("window-size=1900,800")  # Set the window size for the browser
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")  # Set a custom user agent

service = Service(executable_path=binary_path)  # Create a Service object with the path to the ChromeDriver executable
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Initialize the WebDriver with the specified service and options

wd.get("https://www.goodreads.com/list/best_of_year/2014")

wd.save_screenshot('screenshot.png')