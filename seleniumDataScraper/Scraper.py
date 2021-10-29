# Regex the HTML file for the PDF button links to the proceedings and append
# the links to the domain to create proper link.
# Return the links.

import re

class Scraper:

    def getLinks(self,htmlFile):
        # read in file
        path = "./proceedings/" + htmlFile
        with open(path, 'r', encoding='UTF-8') as f:
            text = f.read()
        f.close()

        # regex the links and save to a list, find lines like https://dl.acm.org/doi/pdf/*
        links = re.findall(r'https://dl.acm.org/doi/pdf/[0-9]+\.[0-9]+/[0-9]+\.[0-9]+', text)
        print(htmlFile +', Size = '+str(len(links)))
        print(links)

        return links


