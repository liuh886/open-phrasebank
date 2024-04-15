
Academic phrasebank is an excellent 

# Open Phrasebank

<!-- start why-use-phrase-bank -->

[![Documentation Status](https://readthedocs.org/projects/open-phrasebank/badge/?version=latest)](https://open-phrasebank.readthedocs.io/en/latest/?badge=latest) ![PyPI - Version](https://img.shields.io/pypi/v/openphrasebank)

Building your own phrasebank.

This repository provides an accessible **phrase bank**, which is a collection of frequently used phrases that can be utilized, for example, in the auto-complete function of an IDE. (Note: This library does not provide IDE or auto-complete functions but offers a ready-to-use phrase bank)

Moreover, this repository includes features for constructing a phrase bank from a provided text or an open corpus.

## Why Use Phrase Bank
  
### Case 1 - Typing in Flow

![](https://i.imgur.com/MGDIqly.gif)

Boosting typing experience with phrasebank.🚀

### Case 2 - Academic Writing

You can further customized the phrasebank according to your needs, e.g. for certain discipline, for certain style (descriptive, analytical, persuasive and critical), for certain sections (abstract, body text), as long as you can find good ingredients.

<!-- end why-use-phrase-bank -->

## Open Phrasebanks

<!-- start open-phrase-bank -->
### Academic Phrasebank

Elsevier OA CC-BY contains 40k articles from Elsevier's journals, including from Arts, Business, STEM to Social Sciences[^1]. 

| No. | Phrasebank                                                                                                                 | Source                                                                                                               | N-gram Length | Lines | Comments                                                                |
| --- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ----------------------------------------------------------------------- |
| 1   | 📍[academic_phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/academic_phrasebank.txt)          | Book - [Academic Phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/data/Academic_Phrasebank.pdf) 2014 | 2-5           | 2,190 | Extract from pdf (Zhihao, 2024)                                         |
| 2   | 📍[elsevier_phrasebank](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank.txt)          | Corpus - [Elsevier OA CC-BY](https://elsevier.digitalcommonsdata.com/datasets/zm33cdndxs/2) 2020                     | 2-6           | 3,792 | Extract by n-gram frequency (Zhihao, 2024)                              |
| 3   | 📍[bawe_1000.csv](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/bawe_ngrams.csv)                        | Corpus - [British Academic Written English](https://app.sketchengine.eu/#dashboard?corpname=preloaded%2Fbawe2) 2019  | 4-6           | 1,000 | Due to inaccessible, only most frequent  1000 list here. (Zhihao, 2024) |
| 4   | 📍academic_word_list                                                                                                       | [Academic Word List Coxhead (2000)](https://www.uefap.com/vocab/select/awl.htm)                                      | 1             | 570   | The 570 word for academic English (exclude frequent 2000 words)         |
| 5   | 📍[elsevier_awl](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank.txt)                 | 2                                                                                                                    | 2-6           | 994   | The Elsevier phrasebank that contains  AWL (Zhihao, 2024)               |
| 6   | 📍[elsevier_ENVI_EART](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank_ENVI_EART.txt) | 2                                                                                                                    | 2-7           | 3,700 | Environment & Earth Science 3700 collection (Zhihao 2024)               |
| 7   | 📍[elsevier_PSYC_SOCI](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank_PSYC_SOCI.txt) | 2                                                                                                                    | 2-7           | 3,700 | Social Science & Psychology 3700 collection (Zhihao 2024)               |
| 8   | 📍 [elsevier_MEDI](https://github.com/liuh886/open_phrasebank/blob/main/phrasebanks/elsevier_phrasebank_MEDI.txt)          | 2                                                                                                                    | 2-7           | 3700  | Medicine 3700 collection (Zhihao 2024)                                  |



[^1]:Over 20 disciplines are available [orieg/elsevier-oa-cc-by · Datasets at Hugging Face](https://huggingface.co/datasets/orieg/elsevier-oa-cc-by)


### English Frequent Phrasebank

| No. | Phrasebank                                                                                                                              | Source              | N-gram Length | Lines  | Comments                                                      |
| --- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- | ------ | ------------------------------------------------------------- |
| 1   | 📍[google-10000-english.txt](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english.txt)                 | Google Books Corpus | 1             | 10,000 | The 10,000 most common English words from Google Books Corpus |
| 2   | 📍[Wordlist 1200.txt](https://raw.githubusercontent.com/ManiacDC/TypingAid/master/Wordlists/Wordlist%201200%20frequency%20weighted.txt) | Internet            | 1             | 2,000  | The 2,000 most common English words                           |

<!-- end open-phrase-bank -->


## Quickstart

<!-- start quickstart -->

```bash

pip install openphrasebank

```

<!-- end quickstart -->


<!-- start custom -->
## Get a Self-defined Phrasebank in 3 Steps

![](https://i.imgur.com/qssU2VP.png)

Below is an example based on n-gram frequency. More example available in [documents](https://open-phrasebank.readthedocs.io/en/latest/customisation/index.html).

### Step 1 - Load and Tokenize the Data
``` python
import openphrasebank as opb

tokens_gen = opb.load_and_tokenize_data (dataset_name="orieg/elsevier-oa-cc-by", 
                                         subject_areas=['PSYC','SOCI'],
                                         keys=['title', 'abstract','body_text'],
                                         save_cache=True,
                                         cache_file='temp_tokens.json')
```

### Step 2 - Generate N-grams

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

You can either contribute the phrasebank or [the code](https://open-phrasebank.readthedocs.io/en/latest/contributing.html). 

<!-- start issues -->
### Known Issues

### academic_phrasebank


Due to the table in the PDF file not being properly handled, many sentences were not extracted correctly. 

### elsevier_phrasebank


<!-- end issues -->