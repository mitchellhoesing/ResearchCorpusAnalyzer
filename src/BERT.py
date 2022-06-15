import os
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch


class BERT:
    def __init__(self):
        self.classes = ["not paraphrase", "is paraphrase"]
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
        self.txtFileNames = None
        self.txtFilesPath = None
        self.bibFilesPath = None
        self.bibFileNames = None
        if torch.cuda.is_available():
            self.model.cuda()
        else:
            print("You are not using Cuda Cores.")

    def setTxtFilesPath(self, path):
        # TODO Error check if path exists.
        self.txtFilesPath = path

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


    @classmethod
    def predictParaphrase(self):
        results = "placeholder"
        return results
# Predict paraphrase
# Print results
