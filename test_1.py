# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

PATH = 'D:\Selenium'
driver = webdriver.Chrome(PATH)

# # Create ChromeOptions instance
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Example option for headless mode

# # Set the path to your WebDriver (replace with your WebDriver's actual path)
# service = Service(PATH)

# # Create the WebDriver instance
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Use the WebDriver
# print(driver.capabilities)

# Quit the driver after use
driver.quit()
