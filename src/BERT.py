import os
import re

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch


class BERT:
    def __init__(self):
        self.classes = None
        self.model = None
        self.tokenizer = None
        self.txtFileNames = None
        self.txtFilesPath = None
        self.bibFilesPath = None
        self.bibFileNames = None

    def setTxtFilesPath(self, path):
        # TODO Error check if path exists.
        self.txtFilesPath = path

    def getTxtFileNames(self):
        os.chdir(self.txtFilesPath)
        # Return directory list of file names
        self.txtFileNames = os.listdir()
        # TODO Error check if txtFileNames is empty.
        # Ignore .DS_Store and .gitignore files
        if ".DS_Store" in self.txtFileNames:
            self.txtFileNames.remove(".DS_Store")
        if ".gitignore" in self.txtFileNames:
            self.txtFileNames.remove(".gitignore")
        self.txtFileNames.sort()
        
        return self.txtFileNames

    def setBibFilesPath(self, path):
        # TODO Error check if path exists.
        self.bibFilesPath = path

    def getBibFileNames(self):
        os.chdir(self.bibFilesPath)
        # Return directory list of bibliography names
        self.bibFileNames = os.listdir()
        # TODO Error check if bibFileNames is empty.
        # Ignore .DS_Store and .gitignore files
        if ".DS_Store" in self.bibFileNames:
            self.bibFileNames.remove(".DS_Store")
        if ".gitignore" in self.bibFileNames:
            self.bibFileNames.remove(".gitignore")
        self.bibFileNames.sort()

        return self.bibFileNames

    # TODO Should this just be done in __init__() or a class method?
    def initializeBERT(self):
        # Initialize BERT
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
        self.classes = ["not paraphrase", "is paraphrase"]
        if torch.cuda.is_available():
            self.model.cuda()
        else:
            print("You are not using Cuda Cores.")

    # TODO Should this be in BERT?
    def sanitizeTxtFile(self, filename):

        print("*************************************************", filename,
              "*************************************************", end="\t")
        filePath = self.txtFilesPath + filename
        # TODO Error check if file exists at path
        with open(filePath) as f:
            text = f.read()
            f.close()

        # Remove all non-alphanumeric characters except spaces and periods.
        onlyAlphaNumericText = re.sub(r'[^A-Za-z0-9\s\.]+', "", text)
        # Replace all newlines with spaces.
        sanitizedPaper = onlyAlphaNumericText.replace("\n", " ")

        return sanitizedPaper

    @classmethod
    def predictParaphrase(self):
        results = "placeholder"
        return results
# Predict paraphrase
# Print results
