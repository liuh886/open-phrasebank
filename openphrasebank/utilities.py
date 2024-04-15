import re
import spacy
from typing import List
import json
from collections import defaultdict, Counter
import nltk
from nltk.util import ngrams
nltk.download('punkt')


def smart_join(tokens: list or tuple):
    """Recovery tokens into a phrase with proper spacing.

    Args:
        tokens (list or tuple): The list or tuple of tokens to be joined.

    Returns:
        str: The joined phrase with proper spacing.

    """
    if not tokens:
        return ""

    # Start with the first token
    phrase = tokens[0]

    # Iterate over the remaining tokens
    for token in tokens[1:]:
        # Handling contractions and possessive
        if token in ["'s", "'t", "'re", "'ve", "'d", "'ll", "'m"]:
            phrase += token
        elif phrase[-1].isalnum() and token[0].isalnum():
            # Add a space before joining if both parts are alphanumeric
            phrase += ' ' + token
        elif phrase[-1] not in ',.;!?' and not token[0].isalnum():
            # No space if the next token starts with non-alphanumeric and last is not punctuation
            phrase += token
        else:
            # Default to adding a space unless it's punctuation that typically doesn't follow with a space
            phrase += ' ' + token

    return phrase


def generate_multiple_ngrams(tokens_generator,
                             n_values: List[int] = [2, 3],
                             prune_threshold: int = 3):
    """Generate and prune n-grams based on frequency thresholds.

    Args:
        tokens_generator: A generator that yields tokenized sentences.
        n_values: A list of integers representing the n-gram sizes to generate (default: [2, 3]).
        prune_threshold: An integer representing the frequency threshold for pruning (default: 3).

    Returns:
        ngram_freqs: A defaultdict of Counters, where the keys are the n-gram sizes and the values are the frequency counts.

    """
    ngram_freqs = defaultdict(Counter)
    i = 1
    for tokens in tokens_generator:  # Each tokens is a line of text
        for n in n_values:
            if len(tokens) >= n:
                ngram_freqs[n].update(ngrams(tokens, n))

        # Optionally prune less frequent n-grams to save memory
        if i % 9000 == 0:  # Prune every 9000 lines, adjust based on needs
            prune_ngram_freqs(ngram_freqs, prune_threshold)

        i += 1
    return ngram_freqs


def prune_ngram_freqs(ngram_freqs, prune_threshold):
    """
    Remove less frequent n-grams from the given ngram_freqs dictionary.

    Parameters:
    - ngram_freqs (dict): A dictionary containing n-gram frequencies.
    - prune_threshold (int): The minimum frequency threshold for pruning.

    Returns:
    None
    """
    for n in list(ngram_freqs.keys()):
        for ngram in list(ngram_freqs[n].keys()):
            if ngram_freqs[n][ngram] < prune_threshold:
                del ngram_freqs[n][ngram]


def filter_frequent_ngrams(ngram_counts,
                           most_freq=1000,
                           min_freq=20,
                           exclude_list=None,
                           include_list=None):

    if exclude_list is None:
        exclude_list = ['Table', 'table', 'Fig', 'Figs', 'fig', 'figs', 'Figure', 'figure', 'Appendix', 'Declaration', 'Acknowledgement',
                        'Kim', 'Liu', 'Wang', 'Zhang', 'Li', 'Wu',
                        'Chen', 'Yang', 'Zhao', 'Zhu', 'Xu', 'Sun', 'Ma', 'Hu', 'Guo', 'He', 'Gao', 'Luo', 'Lin', 'Huang', 'Zhou',
                        'Elisabeth', 'Michael', 'Thomas', 'Andreas', 'Stefan', 'Christoph', 'Martin', 'Frank', 'Peter',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100', '&D', '&', 'R',
                        '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33',
                        'and', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
                        '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028',
                        'USA', 'CA', 'UK', 'NY', 'LA', 'DC', 'FL', 'TX', 'IL', 'PA', 'OH', 'GA', 'MI', 'NC', 'NJ', 'VA', 'WA', 'MA', 'AZ', 'CO', 'MD', 'IN',
                        'TN', 'MO', 'MN', 'WI', 'OR', 'SC', 'AL', 'KY', 'OK', 'CT', 'NV', 'KS', 'AR', 'IA', 'UT', 'NM', 'NE', 'ID', 'HI', 'ME', 'NH', 'RI', 'MT', 'DE',
                        'SD', 'ND', 'AK', 'VT', 'WY', 'WV', 'MS', 'PR', 'VI', 'GU', 'AS', 'MP', 'PW', 'MH', 'WHO', '(WHO', '.', ',', ';', '?', '!', '(', ')', '[', ']',
                        '%', 'MHz', ',B', 'B', 'V', 'Hz', 'mV', 'μV', 'nV', 'pV', 'kV', 'MV', 'GV', 'mHz', 'μHz', 'nHz', 'pHz', 'kHz', 'GHz',
                        'THz', 'mΩ', 'μΩ', 'nΩ', 'pΩ', 'kΩ', 'MΩ', 'GΩ', 'TΩ', 'mF', 'μF', 'nF', 'pF', 'kF', 'mH', 'μH', 'nH', 'pH', 'kH', 'mW', 'μW', 'nW',
                        'pW', 'kW', 'MW', 'GW', 'TW', 'mJ', 'μJ', 'nJ', 'pJ', 'kJ', 'MJ', 'GJ', 'TJ', 'mN', 'μN', 'nN', 'pN', 'kN', 'MN', 'GN', 'TN', 'mPa',
                        'μPa', 'nPa', 'pPa', 'kPa', 'MPa', 'GPa', 'TPa', 'mbar', 'μbar', 'nbar', 'pbar', 'kbar', 'Mbar', 'Gbar', 'Tbar', 'mL', 'μL', 'nL',
                        'pL', 'kL', 'm3', 'μ3', 'n3', 'p3', 'k3', 'm2', 'μ2', 'n2', 'p2', 'k2', 'm/s', 'μ/s', 'n/s', 'p/s', 'km/s', 'm/s2',
                        '°C', 'm', 'nm', 'mm', 'cm', 'km', 'kg', 'g', 's', 'h', 'min', 'sec', 'day', 'week', 'month', 'year', 'C', 'F', 'K', 'μL', 'ml']
        exclude_list = set(exclude_list)

    # Filter ngrams which occur at least min_frequency times
    frequent_ngrams = []
    frequent_count = []

    for ngram, count in ngram_counts.items():
        # not to include the common name/unit/number
        ngram_set = set(ngram)

    if (count >= min_freq
        and ngram[0].isalnum()
        and ngram[-1] not in ['a', 'the']
        and ngram[-1].isalnum()
        and not ngram_set.intersection(exclude_list)
            and is_in_includelist(ngram, include_list=include_list)):
        frequent_ngrams.append(smart_join(ngram))
        frequent_count.append(count)

    return frequent_ngrams[:most_freq], frequent_count


def is_in_includelist(ngram, include_list):
    """
    Check if any element in the include_list is present in the given ngram.

    Parameters:
    ngram (str): The ngram to check.
    include_list (list): The list of elements to search for in the ngram.

    Returns:
    bool: True if any element in the include_list is found in the ngram, False otherwise.
    """
    if include_list is None:
        return True
    else:
        for i in include_list:
            if i in ngram:
                return True
        return False

# Define a function to apply multiple filters


def is_valid_phrase(phrase):
    # Check for digits
    if any(char.isdigit() for char in phrase):
        return False
    # Check for specific special characters
    if any(char in phrase for char in ['(', ')', '-', '*', '/', '?', '=', '!', '@', '→', ':', 'et al',
                                       '#', '$', '%', '^', '&', '<', '>', '[', ']', '  ', '\'',
                                       '{', '}', '|', '\\', '~', '`', '+', '_', '•', ',', '/',
                                       '‘', '’', '“', '”', '.', '—', '…', '°', '€', '£', '¥']):
        return False

    # remove normal phrases
    words_to_match = ['women', 'man', 'to do', 'grammar', 'icv',
                      'noun', 'dog', 'cat', 'v', 'c', 'p', 'd', 'P', 're']
    if any(re.search(r'\b' + re.escape(word) + r'\b', phrase) for word in words_to_match):
        return False

    # Check for uppercase letters not at the start
    if re.search(r'\s[A-Z]', phrase):
        return False
    return True


def extract_verb_phrases(doc):
    """Extract verb phrases from a SpaCy document."""
    verb_phrases = [' '.join([tok.lower_ for tok in token.subtree]).replace(
        ' ,', ',') for token in doc if token.pos_ == 'VERB']
    return verb_phrases


def extract_expanded_noun_phrases(doc):
    """Extract expanded noun phrases from a SpaCy document."""
    expanded_noun_phrases = []
    for chunk in doc.noun_chunks:
        start = chunk.start
        while start > 0 and doc[start - 1].pos_ in ['ADJ', 'ADV']:
            start -= 1
        end = chunk.end
        if end < len(doc) and doc[end].pos_ == 'ADP':
            while end < len(doc) and doc[end].pos_ != 'PUNCT':
                end += 1
        expanded_noun_phrases.append(doc[start:end].text)
    return expanded_noun_phrases


def display_word_tree(phrases, keyword):
    json_phrases = json.dumps([["Phrases"]] + [[phrase] for phrase in phrases])
    js_code = f"""
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
    console.log('Loading charts...');
    google.charts.load('current', {{packages:['wordtree']}});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {{
        console.log('Drawing chart...');
        var data = google.visualization.arrayToDataTable({json_phrases});
        var options = {{
            wordtree: {{
                type: 'double',
                format: 'implicit',
                word: '{keyword}'
            }}
        }};
        var chart = new google.visualization.WordTree(document.getElementById('wordtree_basic'));
        chart.draw(data, options);
    }}
    </script>
    <div id="wordtree_basic" style="width: 100%; height: 500px;"></div>
    """
    return js_code
