"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the URL to monitor
url = "http://127.0.0.1:8000/"

# Set the attributes of the element to monitor
element_attrs = {"class": "apply-button"}

# Initialize the web driver
driver = webdriver.Chrome()

# Load the initial page
driver.get(url)

# Monitor the page for changes every 5 seconds
while True:
    try:
        # Find the element by the given attributes
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//button[@{element_attrs}]"))
        )

        # Click the element
        element.click()

        # Exit the loop if the element is clicked
        break

    except:
        # Wait for 5 seconds and check again
        time.sleep(5)
        driver.refresh()

# Close the web driver
driver.quit()
"""


import requests
from bs4 import BeautifulSoup
import time

# Set the URL of the website to monitor
url = "http://127.0.0.1:8000/"

# Set the time interval to check the website
time_interval = 5  # seconds

# Set the initial content of the website
initial_content = ""

while True:
    # Send a GET request to the website and get its content
    response = requests.get(url)
    content = response.content

    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")

    # Check if the content has changed
    if str(soup) != initial_content:
        # Update the initial content
        initial_content = str(soup)

        # Do something if the content has changed
        print("The website content has changed!")

    # Wait for the specified time interval before checking again
    time.sleep(time_interval)


import logging

# Set up logging
logging.basicConfig(filename='requests.log', level=logging.DEBUG)

# Make a GET request to your website
url = "http://127.0.0.1:8000/"
response = requests.get(url)

# Log the request and response
logging.debug(f"Request: {response.request.method} {response.request.url}")
logging.debug(f"Request Headers: {response.request.headers}")
logging.debug(f"Request Body: {response.request.body}")
logging.debug(f"Response Status Code: {response.status_code}")
logging.debug(f"Response Headers: {response.headers}")
logging.debug(f"Response Body: {response.text}")
