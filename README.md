# PDF Downloader Using Selenium

This script automates the process of downloading PDF files from a specified webpage using Selenium WebDriver. It specifically targets the "All" button on the Screener.in website for the Indigo company, retrieves links from a BSE page, and downloads the associated PDF files.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium package
- Chrome browser
- ChromeDriver (matching your Chrome version)

### Installation

1. **Install Selenium:**
   ```bash
   pip install selenium
   ```

2. **Download ChromeDriver:**
   Download the appropriate version of ChromeDriver from [here](https://chromedriver.chromium.org/downloads) and place it in a known directory.

## Configuration

1. **Set Up ChromeDriver Path:**
   Update the `chrome_driver_path` variable in the script to point to your ChromeDriver executable location.

   ```python
   chrome_driver_path = r"C:\path\to\chromedriver.exe"
   ```

2. **Set Up Download Directory:**
   The script will download PDFs to the specified `download_dir`. Update this path if needed.

   ```python
   download_dir = r"C:\path\to\download\directory"
   ```

## Usage

1. **Run the Script:**
   Execute the script using Python. Open your command line interface and run:
   ```bash
   python your_script_name.py
   ```

2. **Functionality:**
   - The script opens the specified URL (`https://www.screener.in/company/INDIGO/`).
   - It clicks on the "All" button to navigate to the BSE announcements page.
   - It extracts links to PDF files listed on the page.
   - For each PDF link, it opens the link and clicks on the `cr-icon` to trigger the download.

## Error Handling

The script includes basic error handling. If the `cr-icon` cannot be found or clicked, an error message will be printed to the console.

## Notes

- Ensure that the webpage structure does not change, as this may require updating the element selectors in the script.
- Be aware of the site's terms of use regarding automated downloads.

## License

This project is licensed under the MIT License.
