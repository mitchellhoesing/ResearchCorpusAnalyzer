import os
import tika
from tika import parser
tika.initVM()

# TODO Error check all paths on construction.


class PDF:
    def __init__(self, readDirectory, writeDirectory):
        self.readDirectory = readDirectory
        self.fileNameList = None
        self.writeDirectory = writeDirectory

    def setPDFReadDirectory(self, readDirectory):
        self.readDirectory = readDirectory
        os.chdir(self.readDirectory)

    def readPDFFileNames(self):
        # TODO: this method is duplication. Also, it is sanitizing the list,
        #  sorting and returning. It does too many things, refactor.

        self.fileNameList = os.listdir()
        if ".DS_Store" in self.fileNameList:
            self.fileNameList.remove(".DS_Store")
        if ".gitignore" in self.fileNameList:
            self.fileNameList.remove(".gitignore")
        self.fileNameList.sort()

    def setPDFWriteDirectory(self, writeDirectory):
        self.writeDirectory = writeDirectory

    def convertPDFToTxt(self, pdfFile):
        print("*************************************************", pdfFile,
              "*************************************************", end="\t")
        raw = parser.from_file(self.readDirectory + pdfFile)
        outFile = open(self.writeDirectory + pdfFile[:-4] + ".txt", "w")
        encodedText = raw['content'].encode("ascii", "ignore")
        decodedText = encodedText.decode()
        outFile.write(decodedText)
        outFile.close()

        return decodedText


