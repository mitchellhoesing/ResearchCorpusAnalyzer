import os
import re

import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from src.Txt import Txt


class BERT:

    def __init__(self, paraphrases):
        self.classes = ["not paraphrase", "is paraphrase"]
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
        # TODO set default values if reasonable
        # TODO Create bib class
        self.bibFilesPath = None
        self.bibFileNames = None
        self.paraphrases = paraphrases
        self.results = []
        self.txt = Txt("..\\inputTXTs\\")
        self._highestProbabilityParaphrase = ""
        if torch.cuda.is_available():
            self.model.cuda()
        else:
            print("You are not using Cuda Cores.")

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

    def setParaphrases(self, paraphraseList):
        # TODO Error check if paraphraseList is empty
        self.paraphrases = paraphraseList

    def getParaphrases(self):
        return self.paraphrases

    # TODO REFACTOR
    def analyze(self):
        txtFiles = self.txt.getTxtFileNames()
        for txtFile in txtFiles:
            sanitizedTxt = self.txt.sanitizeTxtFile(txtFile)
            self.results.append("year")
            self.results.append("title")
            self.results.append("DOI")
            highestPercent = 0
            for paraphrase in self.paraphrases:
                paraphrasePercents = []
                self.results.append(paraphrase)
                for sentence in sanitizedTxt:
                    # Tokenize and encode into a tensor.
                    tensor = self.tokenizer.encode_plus(paraphrase, sentence, padding=True, return_tensors="pt")

                    if torch.cuda.is_available():
                        tensor = tensor.to('cuda')

                    # Classify the tensor using a logistic regression model.
                    paraphraseClassificationLogits = self.model(**tensor)[0]

                    # Normalize the result into a probability distribution using softmax.
                    paraphraseResults = torch.softmax(paraphraseClassificationLogits, dim=1).tolist()[0]

                    # Append the isParaphrase % onto results.
                    paraphrasePercents.append(round(paraphraseResults[1] * 100))

                    # Print sentences and paraphrase probabilities.
                    print(f"{sentence}")
                    for i in range(len(self.classes)):
                        print(f"{self.classes[i]}: {round(paraphraseResults[i] * 100)}%")

                    # TODO
                    # Save all sentences over given threshold
                    # Store the sentence with the highest probability of being a paraphrase.
                    if round(paraphraseResults[1] * 100) > highestPercent:
                        highestPercent = round(paraphraseResults[1] * 100)
                        _highestProbabilityParaphrase = sentence

                print("Results:")
                self.results.append(self._highestProbabilityParaphrase + ": " + str(highestPercent) + "%")
                self.results.append(paraphrasePercents)
                print(*self.results, end="\t")

# Print results
