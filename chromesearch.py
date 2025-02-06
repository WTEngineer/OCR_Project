from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your ChromeDriver
# chromedriver_path = './chromedriver'  # Update this path

# Initialize the Chrome driver
# driver = webdriver.Chrome(chromedriver_path)

def google_search(search_query):
        
    service = Service()
    # options = webdriver.ChromeOptions()
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1280,768")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.google.com")

    # Locate the search box using its name attribute value
    search_box = driver.find_element(By.NAME, "q")

    search_box.clear()

    # Type the search query
    search_box.send_keys(search_query)

    # Press Enter
    search_box.send_keys(Keys.RETURN)

    # Wait for a few seconds to see the results
    time.sleep(5)

    # Optionally, print the title of the page
    print(driver.title)