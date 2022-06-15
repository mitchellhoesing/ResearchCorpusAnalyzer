import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class HTML:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--test-type")
        self.prefs = {
            # TODO: download.default_directory is not switching download location. If this is defined at all, download
            #  will fail. Even to default download location. Does not like relative paths? Needs Permissions?
            "download.default_directory": "C:/Users/Mitch/Downloads",  # Change default directory for downloads
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        }
        self.options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(chrome_options=self.options, service=Service(r"C:\chromedriver_win32\chromedriver.exe"))

    def downloadPDF(self, url, downloadDirectory=None):
        # TODO Error check downloadDirectory exists
        if downloadDirectory is not None:
            self.options.add_experimental_option('download.default_directory', downloadDirectory)
            self.driver = webdriver.Chrome(options=self.options, service=Service(r"C:\chromedriver_win32\chromedriver.exe"))
        self.driver.get(url)
        time.sleep(2)

        # Close the window
        self.driver.close()

    def downloadBibtex(self, url, downloadDirectory):
        # TODO Error check downloadDirectory exists
        self.options.add_experimental_option("download.default_directory", downloadDirectory)
        self.driver = webdriver.Chrome(options=self.options, service=Service(r"C:\chromedriver_win32\chromedriver.exe"))
        self.driver.get(url)

        # TODO abstract hard-coded element paths?
        # Navigate to the bibtex button, click it.
        button = self.driver.find_element(By.XPATH, "//*[@id='pb-page-content']/div/main/div[2]/article/div[1]/div[2]/div/div/div[6]/div/div[2]/ul[1]/li[3]/a/i")
        button.click()

        # # Click the download button inside the bibtex.
        button = self.driver.find_element(By.XPATH, "//*[@id='selectedTab']/div/div[2]/ul/li[1]/a/i")
        button.click()
        time.sleep(2)

        # Close the window
        self.driver.close()

