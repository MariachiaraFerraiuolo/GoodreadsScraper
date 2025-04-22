import sys
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium import webdriver


class CustomChromeOptions():
    def __init__(self,headless=True, window_size="1900,800", 
                 user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"):
        self.headless = headless
        self.window_size = window_size
        self.user_agent = user_agent

    def get_chrome_options(self):
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"window-size={self.window_size}")

        if self.user_agent:
            options.add_argument(f"user-agent={self.user_agent}")

        return options

    def create_driver(self):
        service = Service(ChromeDriverManager().install())  # Create a Service object with the path to the ChromeDriver executable
        options = self.get_chrome_options()
        wd = webdriver.Chrome(service=service, options=options)  # Initialize the WebDriver with the specified service and options
        return wd

