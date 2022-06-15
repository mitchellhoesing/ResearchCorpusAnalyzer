from src.BERT import BERT
from src.HTML import HTML
from src.PDF import PDF
from src.Txt import Txt

bertModel = BERT()
pdf = PDF("", "")
html = HTML()
txt = Txt("", "")


html.downloadPDF("https://dl.acm.org/doi/pdf/10.1145/3025453.3025793")

