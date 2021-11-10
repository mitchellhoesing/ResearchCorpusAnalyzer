import os
import re
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch

os.chdir("../inputTXTs")
filenameList = os.listdir()
if ".DS_Store" in filenameList:
    filenameList.remove(".DS_Store")
if ".gitignore" in filenameList:
    filenameList.remove(".gitignore")
filenameList.sort()

for filename in filenameList:
    print("*************************************************", filename, end="\t")
    with open(filename) as f:
        text = f.read()
        f.close()

    # Remove all non-alphanumeric characters except spaces.
    onlyAlphaNumericText = re.sub(r'[^A-Za-z0-9 \.]+^\s^\.', "", text)

    # Parse text by period delimiter into sentences.
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', onlyAlphaNumericText)

    # Initialize
    # Type of study and source of data.
    # Types of studies: Brainstorming and focus group, interviews, questionnaires, think aloud sessions, instrumenting systems, fly on the wall, analysis of tool use logs, static and dynamic analysis
    # Sources of data: social media, interviews,
    # What are good paraphrases?
    # TODO
    # 1) Store all data results and graph a histogram.
    # Test on couple papers

    paraphrases = ["Using scientific findings to learn design practice is a vital, but complex, task in HCI",
                   "Using scientific findings to learn design practice is a vital, but complex, task in HCI"]

    highestPercent = 0

    for iParaphrases in range(len(paraphrases)):
        # Initialize BERT
        tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
        model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
        classes = ["not paraphrase", "is paraphrase"]

        for iSentences in range(len(sentences)):
            # Tokenize and encode into a tensor.
            paraphrase = tokenizer.encode_plus(paraphrases[iParaphrases], sentences[iSentences], padding=True, return_tensors="pt")

            # Classify the tensor using a logistic regression model.
            paraphraseClassificationLogits = model(**paraphrase)[0]

            # Normalize the result into a probability distribution using softmax.
            paraphraseResults = torch.softmax(paraphraseClassificationLogits, dim=1).tolist()[0]

            # Print sentences and paraphrase probabilities.
            print(f"{sentences[iSentences]}")
            for iResults in range(len(classes)):
                print(f"{classes[iResults]}: {round(paraphraseResults[iResults] * 100)}%")

            # TODO
            # Save all sentences over given threshold
            # Store the sentence with the highest probability of being a paraphrase.
            if round(paraphraseResults[1] * 100) > highestPercent:
                highestPercent = round(paraphraseResults[1] * 100)
                highestProbabilityIsParaphrase = sentences[iSentences]
                print(f"New Highest: {highestPercent}% {highestProbabilityIsParaphrase}")

        print(f"Highest: {highestPercent}% {highestProbabilityIsParaphrase}")