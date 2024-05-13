
# Open Phrasebank

![](https://i.imgur.com/82CMc9w.png)

<!-- start why-use-phrase-bank -->

Building your own phrasebank. ✨

![Documentation Status](https://readthedocs.org/projects/open-phrasebank/badge/?version=latest) ![PyPI - Version](https://img.shields.io/pypi/v/openphrasebank) [![GitHub Action](https://github.com/liuh886/open-phrasebank/actions/workflows/lint.yml/badge.svg)](https://github.com/liuh886/open-phrasebank/actions/workflows/lint.yml) ![GitHub License](https://img.shields.io/github/license/liuh886/open-phrasebank) ![Docker Pulls](https://img.shields.io/docker/pulls/liuh886/open-phrasebank)


This repository provides an accessible **phrase bank**, which is a collection of frequently used phrases that can be utilized, for example, in the auto-complete function of an IDE. (Note: This library does not provide IDE or auto-complete functions but offers ready-to-use phrasebanks)

Moreover, this repository includes features for constructing a phrase bank from a provided text or an open corpus.

## Why Use Phrase Bank
  
### Boosting Typing Experience with Phrasebank 🚀

![](https://i.imgur.com/MGDIqly.gif)

### Academic Writing 🕵️‍♀

You can further customize the phrasebank according to your needs, e.g. for certain disciplines, for certain styles (descriptive, analytical, persuasive and critical), for certain sections (abstract, body text), as long as you can find good ingredients.


<!-- end why-use-phrase-bank -->

## Open Phrasebanks
<!-- start open-phrase-bank -->

### Academic Phrasebank

Elsevier OA CC-BY contains 40k articles from Elsevier's journals, including from Arts, Business, STEM to Social Sciences[^1]. 

| No. | Phrasebank                                                                                                                          | Source                                                                                                                                                                  | N of grams | Lines | Comments                                                                |
| --- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ----- | ----------------------------------------------------------------------- |
| 1   | 📍[academic_phrasebank](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/academic_phrasebank.txt)          | Book [Academic Phrasebank](https://github.com/liuh886/open-phrasebank/blob/main/data/Academic_Phrasebank.pdf) 2014                                                      | 2-5        | 2,190 | Extract from pdf (Zhihao, 2024)                                         |
| 2   | 📍[elsevier_phrasebank](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/elsevier_phrasebank.txt)          | Corpus [Elsevier OA CC-BY](https://elsevier.digitalcommonsdata.com/datasets/zm33cdndxs/2) 2020                                                                          | 2-6        | 3,792 | Extract by n-gram (Zhihao 2024)                                         |
| 3   | 📍[bawe_1000.csv](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/bawe_ngrams.csv)                        | Corpus [British Academic Written English](https://www.coventry.ac.uk/research/research-directories/current-projects/2015/british-academic-written-english-corpus-bawe/) | 4-6        | 1,000 | Due to inaccessible, only most frequent  1000 list here. (Zhihao, 2024) |
| 4   | 📍academic_word_list                                                                                                                 | [Academic Word List Coxhead (2000)](https://www.uefap.com/vocab/select/awl.htm)                                                                                         | 1          | 570   | The 570 word for academic English (exclude frequent 2000 words)         |
| 5   | 📍[elsevier_awl](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/elsevier_phrasebank.txt)                 | 2,4                                                                                                                                                                     | 2-6        | 994   | The Elsevier phrasebank that contains  AWL (Zhihao, 2024)               |
| 6   | 📍[elsevier_ENVI_EART](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/elsevier_phrasebank_ENVI_EART.txt) | 2                                                                                                                                                                       | 2-7        | 3,700 | Environment & Earth Science 3700 collection (Zhihao 2024)               |
| 7   | 📍[elsevier_PSYC_SOCI](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/elsevier_phrasebank_PSYC_SOCI.txt) | 2                                                                                                                                                                       | 2-7        | 3,700 | Social Science & Psychology 3700 collection (Zhihao 2024)               |
| 8   | 📍[elsevier_MEDI](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/elsevier_phrasebank_MEDI.txt)           | 2                                                                                                                                                                       | 2-7        | 3,700 | Medicine 3700 collection (Zhihao 2024)                                  |



[^1]:Over 20 disciplines [orieg/elsevier-oa-cc-by · Datasets at Hugging Face](https://huggingface.co/datasets/orieg/elsevier-oa-cc-by)


### English Frequent Phrasebank

| No. | Phrasebank                                                                                                                             | Source              | N-gram Length | Lines  | Comments                                                      |
| --- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- | ------ | ------------------------------------------------------------- |
| 1   | 📍[google-10000-english](https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt) | Google Books Corpus | 1             | 10,000 | The 10,000 most common English words from Google Books Corpus |
| 2   | 📍[Wordlist 1200.txt](https://raw.githubusercontent.com/ManiacDC/TypingAid/master/Wordlists/Wordlist%201200%20frequency%20weighted.txt) | Internet            | 1             | 2,000  | The 2,000 most common English words                           |

### Other Phrasebank

| No. | Phrasebank                                                                                     | Source | N-gram Length | Lines | Comments      |
| --- | ---------------------------------------------------------------------------------------------- | ------ | ------------- | ----- | ------------- |
| 1   | 📍[emoji](https://raw.githubusercontent.com/liuh886/open-phrasebank/main/phrasebanks/emoji.txt) |        | 1             | 745   | (Zhihao 2024) |

<!-- end open-phrase-bank -->


## Quickstart

<!-- start quickstart -->

You can download the pre-made phrasebank from the table. If you do require a custom one, go forward.

```bash
pip install openphrasebank
```

<!-- end quickstart -->


<!-- start custom -->
## Get a Self-defined Phrasebank in 3 Steps

![](https://i.imgur.com/qssU2VP.png)

Below is an example based on n-gram frequency. [More examples, e.g. extract from PDF, are available in documents](https://open-phrasebank.readthedocs.io/en/latest/quickstart/index.html).

### 1️⃣ Load and Tokenize the Data
``` python
import openphrasebank as opb

tokens_gen = opb.load_and_tokenize_data (dataset_name="orieg/elsevier-oa-cc-by", 
                                         subject_areas=['PSYC','SOCI'],
                                         keys=['title', 'abstract','body_text'],
                                         save_cache=True,
                                         cache_file='temp_tokens.json')
```

### 2️⃣ Generate N-grams

``` python
n_values = [1,2,3,4,5,6,7,8]
opb.generate_multiple_ngrams(tokens_gen, n_values)
```

### 3️⃣ Filter and save

``` python
# Define the top limits for each n-gram length
top_limits = {1: 2000, 2: 2000, 3: 1000, 4: 300, 5: 200, 6: 200, 7: 200, 8: 200}

# Filter the frequent n-grams and store the results in a dictionary
phrases = {}
freqs = {}
for n, limit in top_limits.items():
    phrases[n], freqs[n] = opb.filter_frequent_ngrams(ngram_freqs[n], limit,min_freq=20)

# Combine and sort the phrases from n-gram lengths 2 to 6
sorted_phrases = sorted(sum((phrases[n] for n in range(2, 7)), []))

# Write the sorted phrases to a Markdown file
with open('../elsevier_phrasebank_PSYC_SOCI.txt', 'w') as file:
    for line in sorted_phrases:
        file.write(line + '\n')
```

<!-- end custom -->

## How to Contribute

You can either contribute the phrasebank or the code. Check out our [contributing](https://open-phrasebank.readthedocs.io/en/latest/contributing.html). 

<!-- start issues -->
### Known Issues

| Phrasebank          | Issues                                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| academic_phrasebank | Due to the table in the PDF file not being properly handled, many sentences were not extracted correctly. (zhihao) |
| elsevier_phrasebank |                                                                                                                    |

<!-- end issues -->

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F7WYJ6B)
