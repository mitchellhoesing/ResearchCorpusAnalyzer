import os


class FileUtility:

    def __init__(self):
        pass

    @staticmethod
    def doesFileExist(path):
        return os.path.exists(path)

    @staticmethod
    def createFileListFromPath(path):
        fileList = os.listdir(path)
        fileList = FileUtility.removeGitFiles(fileList)
        return fileList

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

    
