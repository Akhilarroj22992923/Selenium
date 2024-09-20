import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open ChromeDriver and navigate to the URL
driver = webdriver.Chrome()
driver.get("https://www.screener.in/company/INDIGO/")

# Wait for the page to load and the "All" button to appear
try:
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "All")))
    print("Initial page loaded successfully.")
except Exception as e:
    print("Failed to load the initial page:", e)
    driver.quit()
    exit()

# Step 2: Click on "ALL" button and wait for navigation to the new page
try:
    all_button = driver.find_element(By.LINK_TEXT, "All")
    all_button.click()
    WebDriverWait(driver, 20).until(
        lambda d: d.execute_script('return document.readyState') == 'complete' and 
                   d.find_elements(By.CSS_SELECTOR, "a.tablebluelink")
    )
    print("Page fully loaded.")
except Exception as e:
    driver.quit()
    exit()


driver.quit()
exit()
