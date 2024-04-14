
[![Documentation Status](https://readthedocs.org/projects/open-phrasebank/badge/?version=latest)](https://open-phrasebank.readthedocs.io/en/latest/?badge=latest)

# Open Phrasebank

Building your own phrasebank.

<!-- start quickstart -->

## Quickstart

```bash
pip install openphrasebank
```

- This lib provides open accessible phrasebank, which is a collection of frequent phrases that can be used for e.g. auto-complement function of IDE (This lib does not provide IDE or auto-complete function but ready-for-used phrasebank)
- This repository also contains features building a phrasebank from a given text or open corpora, so that the users can have personal phrasebank.

<!-- end quickstart -->

<!-- start why-use-phrase-bank -->
## Why Use Phrase Bank
  
### Case 1 - Typing in Flow


Using phrasebank in an IDE. 

gif - Positive phrasebank

### Case 2 - Academic Writing

You can further customized the phrasebank according your needs, e.g. for certain discipline, for certain style (descriptive, analytical, persuasive and critical), for certain sections (abstract, body text).

The difference of word tree between STEM and ...


<!-- end why-use-phrase-bank -->

<!-- start open-phrase-bank -->
## Open Accessible Phrase Bank


| No. | Phrasebank                                                                                                            | Source                                                                                                               | N-gram Length | Lines  | Comments                                                                |
| --- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- | ------ | ----------------------------------------------------------------------- |
| 1   | 📍[academic_phrasebank.txt](https://github.com/liuh886/open_phrasebank/blob/main/academic_phrasebank.txt)               | Book - [Academic Phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/data/Academic_Phrasebank.pdf) 2014 | 2-5           | 2,190  | Extract from pdf (Zhihao, 2024)                                         |
| 2   | 📍elsevier_phrasebank.txt                                                                                               | Corpus - [Elsevier OA CC-BY](https://elsevier.digitalcommonsdata.com/datasets/zm33cdndxs/2) 2020                     | 2-6           | 3792   | Extract by n-gram frequency (Zhihao, 2024)                              |
| 3   | 📍bawe_1000.csv                                                                                                         | Corpus - [British Academic Written English](https://app.sketchengine.eu/#dashboard?corpname=preloaded%2Fbawe2) 2019  | 4-6           | 1,000  | Due to inaccessible, only most frequent  1000 list here. (Zhihao, 2024) |
| 4   | 📍[google-10000-english.txt](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt) | Google Books Corpus                                                                                                  | 1             | 10,000 | The 10,000 most common English words from Google Books Corpus           |
| 5   | 📍academic_word_list                                                                                                    | [Academic Word List Coxhead (2000)](https://www.uefap.com/vocab/select/awl.htm)                                      | 1             | 570    | The 570 word for academic English (exclude frequent 2000 words)         |
| 6   | 📍elsevier_academic_awl                                                                                                 |                                                                                                                      | 2-6           | 994    | The Elsevier phrasebank that contains  AWL (Zhihao, 2024)               |

  
<!-- end open-phrase-bank -->

## How to Get a Self-defined Phrasebank

![](https://i.imgur.com/qssU2VP.png)

``` python
import openphrasebank as opb

opb.get_phrasebank ('academic_phrasebank.md')
```


The notebook phrasebank_pdf.ipynb gave an example to extract phrasebank from pdf.

The notebook phrasebank_pdf.ipynb gave an example to extract phrasebank from pdf.

  
## How to Contribute

You can either contirbute the phrasebank or the code. 

<!-- start issues -->
### Known Issues

### academic_phrasebank
Due to the table in pdf file were not properly handled, many sentence are not well extracted.

### elsevier_phrasebank

<!-- end issues -->