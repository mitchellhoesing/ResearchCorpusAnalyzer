import re
from src.FileUtility import FileUtility


class BibTex:

    def __init__(self, bibFileName):
        self.bibFileName = bibFileName
        self.bibFilesPath = "bibliographies/"
        self.year = None
        self.title = None
        self.doi = None
        self.bibTexContent = self._readBibTexContent(bibFileName)

    def _readBibTexContent(self, bibFileName):
        file = open(self.bibFilesPath + bibFileName)
        bibTexContent = file.read()
        file.close()
        return bibTexContent

    def getYear(self):
        self._extractYear(self.bibTexContent)
        return self.year

    def _extractYear(self, bibTexContent):
        pattern = r'(19|20)\d\d'
        self.year = re.search(pattern, bibTexContent).group(0)
        return self.year

    def getTitle(self):
        self._extractTitle(self.bibTexContent)
        return self.title

    def _extractTitle(self, bibTexContent):
        titleText = self._returnTitleLine(bibTexContent)
        self.title = self._removeExtraneousChars(titleText)

    @staticmethod
    def _returnTitleLine(bibTexContent):
        pattern = r"^title = {[\w*\s*[$&+,:;=?@#|'<>.-^*()%!]*]*},"
        reSearch = re.search(pattern, bibTexContent, re.MULTILINE).group(0)
        return reSearch

    def getDOI(self):
        self._extractDOI(self.bibTexContent)
        return self.doi

    def _extractDOI(self, bibTexContent):
        doiText = self._returnDOILine(bibTexContent)
        self.doi = self._removeExtraneousChars(doiText)
        print(self.doi)

    @staticmethod
    def _returnDOILine(bibTexContent):
        pattern = r"^doi = {[\w*\s*[$&+,:;=?@#|'<>.-^*()%!]*]*},"
        reSearch = re.search(pattern, bibTexContent, re.MULTILINE).group(0)
        return reSearch

    @staticmethod
    def _removeExtraneousChars(text):
        pattern = r'{[\w*\s*[$&+,:;=?@#|\'<>.-^*()%!]*]*'
        prunedLine = re.search(pattern, text).group(0)
        cleanText = re.sub(r'{', '', prunedLine)
        return cleanText



