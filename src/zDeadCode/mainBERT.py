import os
import re

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch

# Get txt file names.
os.chdir("../inputTXTs")
txtFileNameList = os.listdir()
if ".DS_Store" in txtFileNameList:
    txtFileNameList.remove(".DS_Store")
if ".gitignore" in txtFileNameList:
    txtFileNameList.remove(".gitignore")
txtFileNameList.sort()
print(txtFileNameList)

# Get bib file names
os.chdir("../bibliographies")
bibFileNameList = os.listdir()
if ".DS_Store" in bibFileNameList:
    bibFileNameList.remove(".DS_Store")
if ".gitignore" in bibFileNameList:
    bibFileNameList.remove(".gitignore")
bibFileNameList.sort()
print(bibFileNameList)

# Initialize BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
classes = ["not paraphrase", "is paraphrase"]
if torch.cuda.is_available():
    model.cuda()
else:
    print("You are not using Cuda Cores.")
# Initialize
results = []
# Per paper
for filename in txtFileNameList:
    print("*************************************************", filename, "*************************************************", end="\t")
    filePath = r"../InputTXTs/" + filename
    with open(filePath) as f:
        text = f.read()
        f.close()

    # Remove all non-alphanumeric characters except spaces and periods.
    onlyAlphaNumericText = re.sub(r'[^A-Za-z0-9\s\.]+', "", text)
    # Replace all newlines with spaces.
    onlyAlphaNumericText = onlyAlphaNumericText.replace("\n", " ")
    # Parse text by period delimiter into sentences.
    sentences = re.split(r'\.', onlyAlphaNumericText)

    # Extract/scrape year title and doi
    results.append("year")
    results.append("title")
    results.append("DOI")
    # Type of study and source of data.
    # Types of studies: Brainstorming and focus group, interviews, questionnaires, think aloud sessions, instrumenting systems, fly on the wall, analysis of tool use logs, static and dynamic analysis
    # Sources of data: social media, interviews,
    # What are good paraphrases?

    # TODO

    # 1) list: year, title ,doi ,max , argmax?, list of scores
    # 2) Store all data results and graph a histogram.
    # Results:
    # Only print results after each paper, not each sentence.
    # List containing: Year, Title, DOI, result list
    # result list: Type of study, paraphrase, Sentence yielding max, %'s

    paraphrases = ["Using scientific findings to learn design practice is a vital, but complex, task in HCI",
                   "Gender and Digital Harassment in Southern Asia",
                   ]
    """
    Consider method and sources.
    
    potential paraphrases list:
    
    Data corpus origin is Twitter.
    Data corpus origin is Facebook.
    Data corpus origin is Crowd Workers.
    Data corpus origin is human participants in meat space.
    
    We conducted a lab study.
    we conducted an interview.
    we conducted a survey.
    We conducted is a think aloud.
    We conducted an empirical quantitative study.
    
    """

    highestPercent = 0

    # Per paraphrase
    for iParaphrases in range(len(paraphrases)):
        paraphrasePercents = []
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
            paraphrasePercents.append(round(paraphraseResults[1] * 100))

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

        #print(f"Highest: {highestPercent}% {highestProbabilityIsParaphrase}")
        print("Results:")
        results.append(highestProbabilityIsParaphrase + ": " + str(highestPercent) +"%")
        results.append(paraphrasePercents)
        print(*results, end="\t")