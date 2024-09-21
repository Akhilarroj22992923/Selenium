from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

chrome_driver_path = r"C:\Users\rasika sikaMANI\Downloads\Selenium\chromedriver-win64\chromedriver.exe"  # Specify the path to chromedriver
download_dir = r"C:\Users\rasika sikaMANI\Downloads\Selenium\PDFs"

# Create directory if it does not exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Set Chrome options to download files automatically to the specified directory
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,  
    "plugins.always_open_pdf_externally": True,  
    "download.prompt_for_download": False,  
})

# Create a new instance of Chrome
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.screener.in/company/INDIGO/")
button_element = driver.find_element(By.LINK_TEXT, 'All')
href_link = button_element.get_attribute("href")

# Open the BSE page
driver.get(href_link)

# Pause to allow the page to load
time.sleep(5)

tablebluelink_elements = driver.find_elements(By.CLASS_NAME, 'tablebluelink')

# Extract the href attribute from each link and filter valid URLs
pdf_links = []
for element in tablebluelink_elements:
    href = element.get_attribute('href')
    if href and href != "#":  # Filter out invalid or incomplete links
        # If the link starts with "/xml-data/", prepend the base URL
        if href.startswith("/xml-data/"):
            href = f'https://www.bseindia.com{href}'
        pdf_links.append(href)

# Print the extracted PDF links
print("Extracted PDF Links:")
for link in pdf_links:
    print(link)

# Open each PDF link, click the cr-icon, and trigger the download
for link in pdf_links:
    driver.get(link)  # Open the link in the current tab
    
    # Wait for the page to load
    time.sleep(3)
    
    try:
        cr_icon = driver.find_element(By.TAG_NAME, 'cr-icon')
        cr_icon.click()
        time.sleep(5)
        
    except Exception as e:
        print(f"Error clicking on cr-icon for link {link}: {e}")
    
time.sleep(10)

driver.quit()
