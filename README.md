# Open Phrasebank

```bash
pip install openphrasebank
import openphrasebank as opb
opb.get_phrasebank('academic_phrasebank.md')
```

Building your own phrasebank. 

- The phrasebank is a collection of sentences that can be used for e.g. auto-complement funciton of IDE. 
- This repository also contains script that collects sentences from a given text and builds a phrasebank. 



## Available Phrase Bank

| No. | Phrasebank                                                                                                           | Source                                                                                                          | N-gram Length | Lines | Comments                                                                      |
|-----|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|-------|-------------------------------------------------------------------------------|
| 1   | [academic_phrasebank.md](https://github.com/liuh886/open_phrasebank/blob/main/academic_phrasebank.txt)               | Book - [Academic Phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/data/Academic_Phrasebank.pdf) | 2-5           | 2190  | Extract from pdf and token by spaCy                                           |
| 2   | elsevier_phrasebank.md                                                                                               |                                                                                                                 | 2-5           |       | Extract by n-gram frequency                                                   |
| 3   | bawe_1000.md                                                                                                         | Corpus - [British Academic Written English](https://app.sketchengine.eu/#dashboard?corpname=preloaded%2Fbawe2)  | 2-6           | 1000  | Due to inaccessible, only most frequent used 1000 n-grams (n: 2-6) list here. |
| 4   | [google-1000-english.txt](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt) |                                                                                                                 | 1             | 10000 |                                                                               |
| 5   | academic_word_list                                                                                                   | [Academic Word List Coxhead (2000)](https://www.uefap.com/vocab/select/awl.htm)                                 | 1             | 570   | 570 headwords                                                                 |
| 6   | elsevier_academic_word_list                                                                                          |                                                                                                                 | 1-5           |       |                                                                               |


## Use Cases

Using Phrasebank in an IDE

asd

## Phrasebank Generator

The notebook phrasebank_pdf.ipynb gave an example to extract phrasebank from pdf.

The notebook phrasebank_pdf.ipynb gave an example to extract phrasebank from pdf.

can be further customized the phrasebank according your needs, e.g. for certain discipline, for certain style (descriptive, analytical, persuasive and critical), for certain sections (abstract, body text).






