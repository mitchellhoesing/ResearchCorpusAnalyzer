import os
import re

import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from src.TxtFile import TxtFile


class BERT:

    def __init__(self, paraphrases):
        # TODO Refactor to class level
        self.classes = ["not paraphrase", "is paraphrase"]
        self.model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
        # TODO set default values if reasonable
        # TODO Create bib class
        self.paraphrases = paraphrases
        self._results = ['BERT: Results: ']
        self.txtFile = TxtFile("..\\inputTXTs\\")
        self._highestProbabilityParaphrase = ""
        self._paraphrasePercents = []
        self._highestPercent = 0
        if torch.cuda.is_available():
            self.model.cuda()
        else:
            print("You are not using Cuda Cores.")

    # TODO Refactor to Paraphrase class
    def setParaphrases(self, paraphraseList):
        # TODO Error check if paraphraseList is empty
        self.paraphrases = paraphraseList

    def getParaphrases(self):
        return self.paraphrases

    # TODO REFACTOR. Break into multiple methods. Rename to be more descriptive.
    def analyze(self):
        txtFiles = self.txtFile.getTxtFileNames()
        for txtFile in txtFiles:
            sanitizedTxt = self.txtFile.sanitizeTxtFile(txtFile)
            self._results.append("year")
            self._results.append("title")
            self._results.append("DOI")
            for paraphrase in self.paraphrases:
                self._paraphrasePercents = []
                self._results.append(paraphrase)
                print("BERT: Analyzing phrase: \"" + paraphrase + "\"\nBERT: IN FILE: \"" + txtFile + "\"", end="\n")
                for sentence in sanitizedTxt:
                    # Tokenize and encode into a tensor.
                    tensor = self.tokenizer.encode_plus(paraphrase, sentence, truncation=True, return_tensors="pt")

                    if torch.cuda.is_available():
                        tensor = tensor.to('cuda')

                    paraphraseClassificationLogits = self.model(**tensor)[0]
                    paraphraseResults = torch.softmax(paraphraseClassificationLogits, dim=1).tolist()[0]
                    self._paraphrasePercents.append(round(paraphraseResults[1] * 100))

                    # TODO
                    # Save all sentences over given threshold
                    # Store the sentence with the highest probability of being a paraphrase.
                    if round(paraphraseResults[1] * 100) > self._highestPercent:
                        self._highestPercent = round(paraphraseResults[1] * 100)
                        self._highestProbabilityParaphrase = sentence
                        
                self._printResults()
                self._clearResults()

    # TODO Refactor to new class. What type of results are these?
    def _printResults(self):
        self._results.append("\nBERT: Best Paraphrase: \"" + self._highestProbabilityParaphrase + "\" WITH CONFIDENCE: " + str(self._highestPercent) + "%")
        self._results.append("\nBERT: Full Analysis: " + str(self._paraphrasePercents))
        self._results.append('\n')
        print(*self._results)
    
    def _clearResults(self):
        self._highestProbabilityParaphrase = ""
        self._highestPercent = 0
        self._paraphrasePercents = []
        self._results = ['BERT: Results: ']
