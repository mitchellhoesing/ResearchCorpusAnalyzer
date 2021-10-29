from selenium import webdriver
import time
from Scraper import Scraper

#Initialize selenium.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")

#NOTES: No proceedings for 1984. 1981 has a part 1 and part 2. Need to save html files as "webpage, complete: html files This will include a files folder, which is needed.
#Proceedings HTML file names.
proceedingsHtmlFiles = [
    "Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2015 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2014 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2013 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2012 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2011 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2010 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2009 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2008 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2007 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2006 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2005 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2004 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2003 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2002 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2001 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 2000 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1999 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1998 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1997 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1996 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1995 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1994 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1993 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1992 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1991 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1990 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1989 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1988 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1987 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1986 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1985 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1983 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1982 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html",
    "Proceedings of the 1981 CHI Conference on Human Factors in Computing Systems _ ACM Conferences Part 2.html",
    "Proceedings of the 1981 CHI Conference on Human Factors in Computing Systems _ ACM Conferences Part 1.html"
]

#Create a Scraper object
htmlScraper = Scraper()

for i in range(len(proceedingsHtmlFiles)):
    #Scrape the links out of the current paper and save in a list.
    proceedingLinks = htmlScraper.getLinks(proceedingsHtmlFiles[i])

#Open the paper and sleep 5 to allow time for page to open.
driver.get(proceedingLinks[0])
time.sleep(5)

