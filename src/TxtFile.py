import re
import os
from FileUtility import FileUtility


class TxtFile:
    # TODO Make factory for this class.
    def __init__(self, inputPath):
        self.txtFileNames = None
        self.sanitizedTxt = None
        self.inputPath = inputPath

    def getTxtFileNames(self):
        FileUtility.changeWorkingDirectory(self.inputPath)
        self.txtFileNames = FileUtility.createFileList()
        FileUtility.removeGitFiles(self.txtFileNames)
        self.txtFileNames = FileUtility.sortFiles(self.txtFileNames)

        return self.txtFileNames

    def sanitizeTxtFile(self, fileName):
        filePath = os.path.abspath(self.inputPath + fileName)
        with open(filePath) as f:
            text = f.read()
            f.close()

        # Remove all non-alphanumeric characters except spaces and periods.
        onlyAlphaNumericText = re.sub(r'[^A-Za-z0-9\s\.]+', "", text)
        # Replace all newlines with spaces.
        onlyAlphaNumericText = onlyAlphaNumericText.replace("\n", " ")
        self.sanitizedTxt = re.split(r'\.', onlyAlphaNumericText)

        return self.sanitizedTxt



