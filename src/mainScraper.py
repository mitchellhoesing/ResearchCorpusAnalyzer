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
from selenium import webdriver
import tika
tika.initVM()
from tika import parser




#Year, link to the first paper in year, count of papers in that year.
# 1981 Part 1, https://dl.acm.org/doi/pdf/10.1145/800275.810922, ???
# 1981 Part 2, https://dl.acm.org/doi/pdf/10.1145/800276.810953, ???
# 1982, https://dl.acm.org/doi/pdf/10.1145/800049.801744, 75
# 1983, https://dl.acm.org/doi/pdf/10.1145/800045.801571, 59
# 1984 MISSING YEAR?
# 1985, https://dl.acm.org/doi/pdf/10.1145/317456.317457, 35
# 1986, https://dl.acm.org/doi/pdf/10.1145/22627.22340, 47
# 1987, https://dl.acm.org/doi/pdf/10.1145/29933.30852, 46
# 1988, https://dl.acm.org/doi/pdf/10.1145/57167.57168, 39
# 1989, https://dl.acm.org/doi/pdf/10.1145/67449.67451, 54
# 1990, https://dl.acm.org/doi/pdf/10.1145/97243.97244, 47
# 1991, https://dl.acm.org/doi/pdf/10.1145/108844.108845, 56
# 1992, https://dl.acm.org/doi/pdf/10.1145/142750.142751, 67
# 1993, https://dl.acm.org/doi/pdf/10.1145/169059.169060, 62
# 1994, https://dl.acm.org/doi/pdf/10.1145/191666.191673, 70
# 1995, https://dl.acm.org/doi/pdf/10.1145/223904.223905, 66
# 1996, https://dl.acm.org/doi/pdf/10.1145/238386.238387, 55
# 1997, https://dl.acm.org/doi/pdf/10.1145/258549.258558, 55
# 1998, https://dl.acm.org/doi/pdf/10.1145/274644.274645, 81
# 1999, https://dl.acm.org/doi/pdf/10.1145/302979.302980, 78
# 2000, https://dl.acm.org/doi/pdf/10.1145/332040.332042, 72
# 2001, https://dl.acm.org/doi/pdf/10.1145/365024.365027, 69
# 2002, https://dl.acm.org/doi/pdf/10.1145/503376.503378, 61
# 2003, https://dl.acm.org/doi/pdf/10.1145/503376.503378, 75
# 2004, https://dl.acm.org/doi/pdf/10.1145/985692.985693, 93
# 2005, https://dl.acm.org/doi/pdf/10.1145/1054972.1054974, 93
# 2006, https://dl.acm.org/doi/pdf/10.1145/1124772.1124774, 151
# 2007, https://dl.acm.org/doi/pdf/10.1145/1240624.1240626, 182
# 2008, https://dl.acm.org/doi/pdf/10.1145/1357054.1357056, 157
# 2009, https://dl.acm.org/doi/pdf/10.1145/1518701.1518703, 277
# 2010, https://dl.acm.org/doi/pdf/10.1145/1753326.1753328, 302
# 2011, https://dl.acm.org/doi/pdf/10.1145/1978942.1978944, 410
# 2012, https://dl.acm.org/doi/pdf/10.1145/2207676.2207678, 370
# 2013, https://dl.acm.org/doi/pdf/10.1145/2470654.2470656, 392
# 2014, https://dl.acm.org/doi/pdf/10.1145/2556288.2557152, 465
# 2015, https://dl.acm.org/doi/pdf/10.1145/2702123.2702611, 486
# 2016, https://dl.acm.org/doi/pdf/10.1145/2858036.2858272, 565
# 2017, https://dl.acm.org/doi/pdf/10.1145/3025453.3025842, 600
# 2018, Wouldn't load, 666
# 2019, Already Downloaded, 703
# 2020, https://dl.acm.org/doi/pdf/10.1145/3313831.3376128, ???
# 2021, https://dl.acm.org/doi/pdf/10.1145/3411764.3445565, ???



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

# download = Scraper()
# link = download.buildLink("3025453.3025793")
# download.getLinks("Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems _ ACM Conferences.html")
# Open the paper and immediately download.
# driver.get(link)

# Extract plain text from pdf
raw = parser.from_file('../PDFs/paper001.pdf')
# print(raw['content'])
f = open("../TXTs/test2019.txt", "w")
encodedText = raw['content'].encode("ascii", "ignore")
print(encodedText.decode())
f.write(encodedText.decode())
f.close()