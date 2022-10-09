import re
from FileUtility import FileUtility


class TxtFile(FileUtility):
    def __init__(self):
        super().__init__()
        self.txtFileNames = None
        self.sanitizedTxt = None
        self.txtFiles = None

    def createTxtFileListFromPath(self, path):
        self.txtFiles = FileUtility.createFileListFromPath(path)
        FileUtility.removeGitFiles(self.txtFiles)
        FileUtility.sortFiles(self.txtFiles)
        self.sanitizeTxtFiles(path)

        return self.txtFiles

    # TODO FIX ME
    def sanitizeTxtFiles(self, path):
        tempList = []
        for txtFile in self.txtFiles:
            file = open(path + txtFile, "r")
            fileContents = file.read()
            # Remove all non-alphanumeric characters except spaces and periods.
            fileContents = re.sub(r'[^A-Za-z0-9\s\.]+', "", fileContents)
            # Replace all newlines with spaces.
            fileContents = fileContents.replace(r"\n", " ")
            fileContents = re.split(r'\.', fileContents)
            f = open(r"C:\Users\Mitch\PycharmProjects\ResearchCorpusAnalyzer\TXTs\\" + txtFile, "w")
            f.write(fileContents[0])
            f.close()
            file.close()


