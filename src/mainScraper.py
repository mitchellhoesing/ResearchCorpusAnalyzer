# TODO
# Iterate through links.
# How many 404s?
# If any break, we know not iterable in this fashion.
# One script to download pdfs
# Check if have data, if not build links, else don't.

# One script to parse out text
# One script to analyze text
# Break extraction into a class
# Merge BERT folder and seleniumDataScraper under 1 folder.
# Can change main executes in top right, edit configs.

# Will want to break apart and get partial results because of large amount of data.
# To pull a specific commit
# Git fetch,
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Scraper import Scraper

# Initialize selenium.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_experimental_option('prefs', {
    'download.default_directory': '..\bibliographies',  # Change default directory for downloads
    'download.prompt_for_download': False,  # To auto download the file
    'download.directory_upgrade': True,
    'plugins.always_open_pdf_externally': True  # It will not show PDF directly in chrome
})
driver = webdriver.Chrome(service=Service(r"C:\chromedriver_win32\chromedriver.exe"))

scraper = Scraper()
pdfLink, bibtexLink = scraper.buildLinks("3025453.3025793")
# FIXME this access is broken, do we need some more meta data floating around?, perhaps inputHTMLs?
# download.getLinks("Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html")

# Open the paper and immediately download.
driver.get(pdfLink)

# Switch to bibtex page
driver.get(bibtexLink)

# Navigate to the bibtex button, click it.
button = driver.find_element(By.XPATH, '//*[@id="pb-page-content"]/div/main/div[2]/article/div[1]/div[2]/div/div/div[6]/div/div[2]/ul[1]/li[3]/a/i')
button.click()

# Click the download button inside the bibtex.
button = driver.find_element(By.XPATH, '//*[@id="selectedTab"]/div/div[2]/ul/li[1]/a/i')
button.click()
time.sleep(2)

# Close the window
driver.close()
