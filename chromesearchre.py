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
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("--window-size=1280,768")
    # chrome_options.add_argument("--disable-background-networking")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-hang-monitor")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-prompt-on-repost")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--disable-translate")
    chrome_options.add_argument("--metrics-recording-only")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--safebrowsing-disable-auto-update")
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
    time.sleep(60)

    # Optionally, print the title of the page
    print(driver.title)