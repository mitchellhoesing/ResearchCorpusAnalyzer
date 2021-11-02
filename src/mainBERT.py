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
    sequence_0 = "Venous Materials: at Interactive Fluid Machines."

    highestPercent = 0
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")
    classes = ["not paraphrase", "is paraphrase"]

    for i in range(len(sentences)):
        # Tokenize and encode into a tensor.
        paraphrase = tokenizer.encode_plus(sequence_0, sentences[i], padding=True, return_tensors="pt")

        # Classify the tensor using a logistic regression model.
        paraphrase_classification_logits = model(**paraphrase)[0]

        # Normalize the result into a probability distribution using softmax.
        paraphrase_results = torch.softmax(paraphrase_classification_logits, dim=1).tolist()[0]

        # Print sentences and paraphrase probabilities.
        print(f"{sentences[i]}")
        for ind in range(len(classes)):
            print(f"{classes[ind]}: {round(paraphrase_results[ind] * 100)}%")

        # TODO
        # Save all sentences over given threshold
        # Store the sentence with the highest probability of being a paraphrase.
        if round(paraphrase_results[1] * 100) > highestPercent:
            highestPercent = round(paraphrase_results[1] * 100)
            highestProbabilityIsParaphrase = sentences[i]
            print(f"New Highest: {highestPercent}% {highestProbabilityIsParaphrase}")