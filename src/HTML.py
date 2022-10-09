import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os


class HTML:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--test-type")
        self.prefs = {
            "download.default_directory": os.path.abspath(r"..\inputPDFs"),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }
        self.options.add_experimental_option("prefs", self.prefs)
        # TODO Make chromedriver.exe exist in venv or denote in a relative path.
        self.driver = webdriver.Chrome(chrome_options=self.options, service=Service(r"C:\chromedriver_win32\chromedriver.exe"))

    # TODO Refactor to PDF class?
    def downloadPDF(self, url):
        self.driver.get(url)
        time.sleep(2)
        self.driver.close()

    # TODO Refactor to BibTex class
    def downloadBibtex(self, url):
        self.driver.get(url)

        # TODO generalize the hard-coded element paths?
        button = self.driver.find_element(By.XPATH, "//*[@id='pb-page-content']/div/main/div[2]/article/div[1]/div[2]/div/div/div[6]/div/div[2]/ul[1]/li[3]/a/i")
        button.click()

        button = self.driver.find_element(By.XPATH, "//*[@id='selectedTab']/div/div[2]/ul/li[1]/a/i")
        button.click()
        time.sleep(2)
        self.driver.close()

