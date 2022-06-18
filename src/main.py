from src.BERT import BERT
from src.HTML import HTML
from src.PDF import PDF
from src.Txt import Txt


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

paraphrases = ["We showcase Group Touch, a method for identifying among multiple users at the same time interacting with "
               "a desktop computer using only the touch information supplied by the computer.",
               "Gender and Digital Harassment in Southern Asia",
               ]


bertModel = BERT(paraphrases)
bertModel.analyze()



