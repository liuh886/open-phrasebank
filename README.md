
# Open Phrasebank
[![Documentation Status](https://readthedocs.org/projects/open-phrasebank/badge/?version=latest)](https://open-phrasebank.readthedocs.io/en/latest/?badge=latest) ![PyPI - Version](https://img.shields.io/pypi/v/openphrasebank)


Building your own phrasebank.

<!-- start quickstart -->

## Quickstart

This repository provides an openly accessible phrase bank, which is a collection of frequently used phrases that can be utilized, for example, in the auto-complete function of an IDE. (Note: This library does not provide IDE or auto-complete functions but offers a ready-to-use phrase bank)

Moreover, this repository includes features for constructing a phrase bank from a provided text or an open corpus, enabling users to create their own personalized phrase banks.

```bash
pip install openphrasebank
```

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


| No. | Phrasebank                                                                                                                  | Source                                                                                                               | N-gram Length | Lines  | Comments                                                                |
| --- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- | ------ | ----------------------------------------------------------------------- |
| 1   | 📍 [academic_phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/academic_phrasebank.txt)          | Book - [Academic Phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/data/Academic_Phrasebank.pdf) 2014 | 2-5           | 2,190  | Extract from pdf (Zhihao, 2024)                                         |
| 2   | 📍 [elsevier_phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank.txt)          | Corpus - [Elsevier OA CC-BY](https://elsevier.digitalcommonsdata.com/datasets/zm33cdndxs/2) 2020                     | 2-6           | 3792   | Extract by n-gram frequency (Zhihao, 2024)                              |
| 3   | 📍[bawe_1000.csv](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/bawe_ngrams.csv)                         | Corpus - [British Academic Written English](https://app.sketchengine.eu/#dashboard?corpname=preloaded%2Fbawe2) 2019  | 4-6           | 1,000  | Due to inaccessible, only most frequent  1000 list here. (Zhihao, 2024) |
| 4   | 📍[google-10000-english.txt](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt)     | Google Books Corpus                                                                                                  | 1             | 10,000 | The 10,000 most common English words from Google Books Corpus           |
| 5   | 📍academic_word_list                                                                                                        | [Academic Word List Coxhead (2000)](https://www.uefap.com/vocab/select/awl.htm)                                      | 1             | 570    | The 570 word for academic English (exclude frequent 2000 words)         |
| 6   | 📍[elsevier_awl](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank.txt)                  | 2                                                                                                                    | 2-6           | 994    | The Elsevier phrasebank that contains  AWL (Zhihao, 2024)               |
| 7   | 📍 [elsevier_ENVI_EART](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank_ENVI_EART.txt) | 2                                                                                                                    | 2-7           | 3700   | Environment & Earth Science 3700 collection (Zhihao 2024)               |
| 8   | 📍[elsevier_PSYC_SOCI](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank_PSYC_SOCI.txt)  | 2                                                                                                                    | 2-7           | 3700   | Social Science & Psychology 3700 collection (Zhihao 2024)               |


  
<!-- end open-phrase-bank -->

<!-- start custom -->

## How to Get a Self-defined Phrasebank

![](https://i.imgur.com/qssU2VP.png)


Below is an example based on n-gram frequency. More example avvailable in [documents](https://open-phrasebank.readthedocs.io/en/latest/customisation/index.html).

### Step 1 - Load and tokenize the data
``` python
import openphrasebank as opb

tokens_gen = opb.load_and_tokenize_data (dataset_name="orieg/elsevier-oa-cc-by", 
                                         subject_areas=['ENVI','EART'],
                                         keys=['title', 'abstract','body_text'],
                                         save_cache=True,
                                         cache_file='temp_tokens.json')
```

### Step 2 - Gnerate n-grams

``` python
import openphrasebank as opb
n_values = [1,2,3,4,5,6,7,8]
opb.generate_multiple_ngrams(tokens_gen, n_values)
```

### Step 3 - Filter and save

``` python
# Define the top limits for each n-gram length
top_limits = {1: 2000, 2: 2000, 3: 1000, 4: 300, 5: 200, 6: 200, 7: 200, 8: 200}

# Filter the frequent n-grams and store the results in a dictionary
phrases = {}
freqs = {}
for n, limit in top_limits.items():
    phrases[n], freqs[n] = filter_frequent_ngrams(ngram_freqs[n], limit,min_freq=20)

# Combine and sort the phrases from n-gram lengths 2 to 6
sorted_phrases = sorted(sum((phrases[n] for n in range(2, 7)), []))

# Write the sorted phrases to a Markdown file
with open('../elsevier_phrasebank_PSYC_SOCI.txt', 'w') as file:
    for line in sorted_phrases:
        file.write(line + '\n')
```
<!-- end custom -->

## How to Contribute

You can either contirbute the phrasebank or the code. 

<!-- start issues -->
### Known Issues

### academic_phrasebank
Due to the table in pdf file were not properly handled, many sentence are not well extracted.

### elsevier_phrasebank

<!-- end issues -->