import os


class FileUtility:

    def __init__(self):
        pass

    @staticmethod
    def doesFileExist(path):
        return os.path.exists(path)

    @staticmethod
    def changeWorkingDirectory(path):
        os.chdir(path)

    @staticmethod
    def createFileList():
        return os.listdir()

    @staticmethod
    def sortFiles(fileList):
        return fileList.sort()
    
    @staticmethod
    def removeGitFiles(fileList):
        if ".DS_Store" in fileList:
            fileList.remove(".DS_Store")
        if ".gitignore" in fileList:
            fileList.remove(".gitignore")
            
        return fileList
    