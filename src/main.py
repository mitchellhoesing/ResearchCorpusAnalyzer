from src.BERT import BERT


paraphrases = ["Data corpus is Facebook",
               "Data corpus is Crowd Workers",
               "Data corpus is Twitter",
               "Data corpus is Amazon",
               "We conducted a lab study",
               "We conducted an interview",
               "We conducted a survey",
               "We conducted a think aloud",
               "We conducted an empirical quantitative study",
               "Data corpus origin is human participants in meat space",
               ]


bertModel = BERT(paraphrases)
bertModel.analyze()



