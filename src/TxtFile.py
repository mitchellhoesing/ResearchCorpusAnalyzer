import re
from FileUtility import FileUtility


class TxtFile(FileUtility):
    def __init__(self):
        super().__init__()
        self.txtFileNames = None
        self.sanitizedTxt = None
        self.txtFiles = None

    # TODO FIX ME
    def sanitizeFilesAtPath(self, path):
        self.txtFiles = FileUtility.createFileListFromPath(path)
        FileUtility.removeGitFiles(self.txtFiles)
        FileUtility.sortFiles(self.txtFiles)
        sanitizedFilePath = r"C:\Users\Mitch\PycharmProjects\ResearchCorpusAnalyzer\TXTs\\"
        for txtFile in self.txtFiles:
            file = open(path + txtFile, "r")
            fileContents = file.read()
            # Remove all non-alphanumeric characters except spaces and periods.
            fileContents = re.sub(r'[^A-Za-z0-9\s\.]+', "", fileContents)
            # Replace all newlines with spaces.
            fileContents = fileContents.replace(r"\n", " ")
            f = open(sanitizedFilePath + "Sanitized." + txtFile, "w")
            f.write(fileContents)
            f.close()
            file.close()
        self.txtFiles = FileUtility.createFileListFromPath(sanitizedFilePath)
        FileUtility.removeGitFiles(self.txtFiles)
        FileUtility.sortFiles(self.txtFiles)

        return self.txtFiles


