import os
import re

from torch.autograd import Variable
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

# Initialize BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
classes = ["not paraphrase", "is paraphrase"]
if torch.cuda.is_available():
    model.cuda()
else:
    print("You are not using Cuda Cores.")

# Per file
for filename in filenameList:
    print("*************************************************", filename, end="\t")
    with open(filename) as f:
        text = f.read()
        f.close()

    # Remove all non-alphanumeric characters except spaces and periods.
    onlyAlphaNumericText = re.sub(r'[^A-Za-z0-9\s\.]+', "", text)
    # Replace all newlines with spaces.
    onlyAlphaNumericText = onlyAlphaNumericText.replace("\n", " ")
    # Parse text by period delimiter into sentences.
    #OLD: sentences = re.split(r' *[\.\?!][\'"\)\]]* *', onlyAlphaNumericText)
    sentences = re.split(r'\.', onlyAlphaNumericText)
    # Initialize
    results = []
    results = ["year", "title", "DOI"]
    # Type of study and source of data.
    # Types of studies: Brainstorming and focus group, interviews, questionnaires, think aloud sessions, instrumenting systems, fly on the wall, analysis of tool use logs, static and dynamic analysis
    # Sources of data: social media, interviews,
    # What are good paraphrases?

    # TODO
    # 0) add newlines to regex to break on. This is being a pain in the ass, do we care? Relevant sentences should be delimited by a "."
    # 1) Store all data results and graph a histogram.
    # 2) list: year, title ,doi ,max , argmax,list of scores
    # Results:
    # Only print results after each paper, not each sentence.
    # List containing: Year, Title, DOI, result list
    # result list: Type of study, paraphrase, Sentence yielding max, %s
    # store paraphraseResults (%s) in list
    # highest pct and sentence that gave highest %
    # Output results as tab separated and copy paste into excel.

    paraphrases = [#"Using scientific findings to learn design practice is a vital, but complex, task in HCI",
                   "Gender and Digital Harassment in Southern Asia"
                   ]

    highestPercent = 0

    # Per paraphrase
    for iParaphrases in range(len(paraphrases)):

        results.append(paraphrases[iParaphrases])
        # Per sentence in a paper
        for iSentences in range(len(sentences)):
            # Tokenize and encode into a tensor.
            paraphrase = tokenizer.encode_plus(paraphrases[iParaphrases], sentences[iSentences], padding=True, return_tensors="pt")

            if torch.cuda.is_available():
                paraphrase = paraphrase.to('cuda')

            # Classify the tensor using a logistic regression model.
            paraphraseClassificationLogits = model(**paraphrase)[0]

            # Normalize the result into a probability distribution using softmax.
            paraphraseResults = torch.softmax(paraphraseClassificationLogits, dim=1).tolist()[0]

            # Append the isParaphrase % onto results.
            results.append(round(paraphraseResults[1] * 100))

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
                #print(f"New Highest: {highestPercent}% {highestProbabilityIsParaphrase}")

        print(f"Highest: {highestPercent}% {highestProbabilityIsParaphrase}")

        results.append(highestProbabilityIsParaphrase + ": " + str(highestPercent) +"%")

    for i in range(len(results)):
        print(results[i], end="\t")
