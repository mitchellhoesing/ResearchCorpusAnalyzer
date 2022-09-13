import re
import os


class TxtFile:

    # TODO Error check all paths on construction.

    def __init__(self, inPath):
        self.txtFileNames = None
        self.inputPath = inPath
        self.sanitizedTxt = None

    def getTxtFileNames(self):
        os.chdir(self.inputPath)
        # Return directory list of file names
        self.txtFileNames = os.listdir()
        # Ignore .DS_Store and .gitignore files
        if ".DS_Store" in self.txtFileNames:
            self.txtFileNames.remove(".DS_Store")
        if ".gitignore" in self.txtFileNames:
            self.txtFileNames.remove(".gitignore")
        self.txtFileNames.sort()

        return self.txtFileNames

    def sanitizeTxtFile(self, filename):
        print("*************************************************", filename,
              "*************************************************", end="\n")
        filePath = os.path.abspath(self.inputPath + filename)
        with open(filePath) as f:
            text = f.read()
            f.close()

        # Remove all non-alphanumeric characters except spaces and periods.
        onlyAlphaNumericText = re.sub(r'[^A-Za-z0-9\s\.]+', "", text)
        # Replace all newlines with spaces.
        onlyAlphaNumericText = onlyAlphaNumericText.replace("\n", " ")
        self.sanitizedTxt = re.split(r'\.', onlyAlphaNumericText)

        return self.sanitizedTxt

