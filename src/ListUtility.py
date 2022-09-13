import logging
import os


class ListUtility:

    @staticmethod
    def createFileListFromPath(path):
        fileList = os.listdir(path)
        if len(fileList) != 0:
            return fileList
        else:
            logging.error("No files found in " + path)


