# Deprecate for PDF.py

import os
import tika
tika.initVM()
from tika import parser

inputPath = "../inputPDFs/"
os.chdir(inputPath)
filenameList = os.listdir()
if ".DS_Store" in filenameList:
    filenameList.remove(".DS_Store")
if ".gitignore" in filenameList:
    filenameList.remove(".gitignore")
filenameList.sort()

outputPath = "../inputTXTs/"
for filename in filenameList:
    print("*************************************************", filename, "*************************************************", end="\t")

    # Extract plain text from pdf
    raw = parser.from_file(inputPath + filename)
    # print(raw['content'])

    outFile = open(outputPath + filename[:-4] + ".txt", "w")
    encodedText = raw['content'].encode("ascii", "ignore")
    decodedText = encodedText.decode()
    print(decodedText)
    outFile.write(decodedText)
    outFile.close()