import os
import tika
from tika import parser
tika.initVM()


class PDF:
    def __init__(self, inPath, outPath):
        self.inputPath = inPath
        self.fileNameList = None
        self.outputDirectory = outPath

    def setReadDirectory(self, path):
        self.inputPath = path
        # TODO Error check path exists
        os.chdir(self.inputPath)

    def readFileNames(self):
        # TODO Error check if os.directory exists. Instantiate with setDirectory()
        self.fileNameList = os.listdir()
        if ".DS_Store" in self.fileNameList:
            self.fileNameList.remove(".DS_Store")
        if ".gitignore" in self.fileNameList:
            self.fileNameList.remove(".gitignore")
        self.fileNameList.sort()

    def setOutputDirectory(self, path):
        # TODO Error check path exists
        self.outputDirectory = path

    def convertToTxt(self, fileName):
        print("*************************************************", fileName,
              "*************************************************", end="\t")

        # Extract plain text from pdf
        raw = parser.from_file(self.inputPath + fileName)
        outFile = open(self.outputDirectory + fileName[:-4] + ".txt", "w")
        encodedText = raw['content'].encode("ascii", "ignore")
        decodedText = encodedText.decode()
        outFile.write(decodedText)
        outFile.close()

        return decodedText


