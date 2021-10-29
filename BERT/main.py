#TODO
#Loop to compare sentences with paraphrase
#Save best matching sentence and top 5 sentences.
#If time is an issue, truncate documents.
#GitHub dodgej

#Document Classification.
#Clusters
#Twitter
#Facebook
#Amazon Mechanical Turk
#Twitch
#Survey
#Interview
#In lab
#Instagram

#Is sentence in X cluster?
#Calculated by calculating paraphrase percentage.
#Should we compare paraphrase percentage with multiple corpus identifying sentences and average
#the percentage for confidence?

import re
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch

#Use Cuda Cores, put input on gpu and model on gpu then possibly output back to cpu
# do the forward pass
        #if torch.cuda.is_available():
        #    nnOutput = self.forward(Variable(boardTensor.cuda()))
        #else:
         #   nnOutput = self.forward(Variable(boardTensor))

        #return nnOutput

highestPercent = 0
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc")

classes = ["not paraphrase", "is paraphrase"]

with open(".\ResearchPapers\Venous Materials Text.txt") as f:
    text = f.read()

f.close()
# Remove all non-alphanumeric characters except spaces.
onlyAlphaNumericText = re.sub(r'[^A-Za-z0-9 \.]+^\s^\.', "", text)

# Parse text by period delimiter into sentences.
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', onlyAlphaNumericText)

# Initialize
sequence_0 = "Venous Materials: at Interactive Fluid Machines."

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