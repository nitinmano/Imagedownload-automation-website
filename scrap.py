# Import necessary libraries
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from bs4 import BeautifulSoup
import requests
chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
# options = [
#     "--headless",
#     "--disable-gpu",
#     "--window-size=1920,1200",
#     "--ignore-certificate-errors",
#     "--disable-extensions",
#     "--no-sandbox",
#     "--disable-dev-shm-usage"
# ]
# for option in options:
#     chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the website
driver.get("https://wallpapercave.com/demon-slayer-4k-mac-wallpapers")

# Wait for the fp-card elements to be present on the page
wait = WebDriverWait(driver, 10000)

images = driver.find_elements(By.TAG_NAME, 'img')

image_urls = []

for image in images:
    if image.get_attribute('class') == 'wimg':
        image_urls.append(image.get_attribute('src'))




folder_path = './images'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)



for url in image_urls:
    driver.get(url)
    image_data = driver.page_source
    soup = BeautifulSoup(image_data, 'html.parser')
    image_element = soup.find('img')
    if image_element:
        image_url = image_element['src']
        response = requests.get(image_url)
        with open(f"{folder_path}/{image_url.split('/')[-1]}", "wb") as f:
            f.write(response.content)



