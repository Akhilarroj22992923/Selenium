# Selenium Automation Script README

This project is a Python automation script using Selenium to interact with the web page of the company "INDIGO" on the website "Screener.in". The script navigates to the page, waits for it to load, clicks the "All" button, and verifies the successful loading of the page content.

## Prerequisites

1. **Python 3.x** installed on your system.
2. **Google Chrome** installed.
3. **ChromeDriver** that matches the installed version of Google Chrome.

## Installation Instructions

### Step 1: Install Selenium
Before running the script, install Selenium by executing the following command in your terminal:

```bash
pip install selenium
```

### Step 2: Set up ChromeDriver
Ensure that the `ChromeDriver` executable is available in your system's PATH or placed in the project directory.

You can download the appropriate version of ChromeDriver for your system from the following link:  
[ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Ensure the downloaded `ChromeDriver` version matches your installed Chrome browser version.

### Step 3: Clone the Repository

Clone or download the code into your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

### Step 4: Run the Script

Open a terminal in the project directory and execute the Python script:

```bash
python auto.py
```

This script will:
1. Open a Chrome browser window.
2. Navigate to the page for the company **INDIGO** on Screener.in.
3. Wait for the page to load and locate the **"All"** button.
4. Click the **"All"** button and wait for the page to load fully.
5. Close the browser.

### Script Explanation

1. **Dependencies**:  
   The script imports the following modules:
   - `os`: For potential OS-level operations.
   - `requests`: (Not used, can be removed unless required for future additions).
   - `selenium.webdriver`: For automating the Chrome browser.
   - `selenium.webdriver.support.ui.WebDriverWait`: For handling waiting conditions.
   - `selenium.webdriver.support.expected_conditions`: To manage conditions while waiting for elements to load.

2. **Browser Automation**:  
   - **Step 1**: The script opens Chrome using `webdriver.Chrome()` and navigates to the company page on Screener.in.
   - **Step 2**: It waits for the **"All"** button to appear on the page.
   - **Step 3**: After clicking the "All" button, it waits for the page to finish loading.
   - **Final Step**: The browser is closed and the script terminates.

## Troubleshooting

1. **ChromeDriver version mismatch**: Ensure that your ChromeDriver version matches your Chrome browser version. If there is a version mismatch, you will encounter errors.
   
2. **Timeout errors**: If the page does not load within the timeout period of 20 seconds, the script will throw an error. You can increase the wait time by modifying the `WebDriverWait` in the script.

3. **Script fails to find elements**: If the website's structure changes (e.g., the **"All"** button is removed or renamed), the script might fail. Ensure the element exists with the correct name or update the code accordingly.

## Notes

- Ensure your internet connection is stable to avoid timeouts.
- This script can be extended by adding more functionality, such as scraping data or automating further interactions with the web page.

## License

This project is licensed under the MIT License.
