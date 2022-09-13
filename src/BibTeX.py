from src.ListUtility import ListUtility


class BibTeX:

    def __init__(self):
        self.bibFilesPath = "../bibliographies/"
        self.bibFileNames = None

    def setPathToBibFiles(self, bibFilesPath):
        self.bibFilesPath = bibFilesPath

    def readBibFileNamesFromDir(self):
        self.bibFileNames = ListUtility.createFileListFromPath(self.bibFilesPath)
        self._removeNonBibFiles()
        self.bibFileNames.sort()

        return self.bibFileNames

    def _removeNonBibFiles(self):
        for file in self.bibFileNames:
            if not file.endswith(".bib"):
                self.bibFileNames.remove(file)


