from selenium import webdriver
from Scraper import Scraper

#Initialize selenium.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_experimental_option('prefs', {
"download.default_directory": r"./papers", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
driver = webdriver.Chrome(executable_path=r"C:/chromedriver_win32/chromedriver.exe", options=options)

#Open the paper and immediately download.
#driver.get('https://dl.acm.org/doi/pdf/10.1145/3313831.3376131')

download = Scraper()
link = download.buildLink("3025453.3025793")
#FIXME this access is broken, do we need some more meta data floating around?, perhaps inputHTMLs?
download.getLinks("Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html")
#Open the paper and immediately download.
driver.get(link)

