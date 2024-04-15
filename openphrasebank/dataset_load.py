import json
from nltk.tokenize import word_tokenize
from datasets import load_dataset
from tqdm import tqdm

def flatten(nested_list):
    """Flatten nested list structure.

    Args:
        nested_list (list): A nested list structure.

    Yields:
        object: The flattened elements of the nested list.

    """
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

def tokens_generator(file_path, chunk_size=500):
    """ 
    Generator function to yield chunks of tokens from a file.

    Parameters:
    file_path (str): The path to the file containing the tokens.
    chunk_size (int, optional): The size of each chunk of tokens to yield. Defaults to 500.

    Yields:
    list: A chunk of tokens from the file.

    """
    tokens = []
    with open(file_path, 'r') as f:
        for line in f:
            new_tokens = json.loads(line)
            tokens.extend(new_tokens)

            # Yield the tokens in chunks
            while len(tokens) >= chunk_size:
                yield tokens[:chunk_size]
                tokens = tokens[chunk_size:]

        # Yield any remaining tokens after the loop
        if tokens:
            yield tokens

def load_and_tokenize_data(dataset_name, 
                           subject_areas: list =None,
                           keys: list =['title','abstract', 'body_text'],
                           save_cache: bool =False, 
                           cache_file='temp_tokens.json'):
    '''
    Load a dataset, filter by subject area if specified, and tokenize the sentences in the specified keys.

    Args:
    dataset_name (str): The name of the dataset to load.
    subject_area (str): The subject area to filter by, optional. By defualt (None) it contains following.
                        ['AGRI','ARTS','BIOC','BUSI','CENG','CHEM','COMP','DECI',
                        'DENT','EART','ECON','ENER','ENGI','ENVI','HEAL','IMMU',
                        'MATE','MATH','MEDI','MULT','NEUR', 'NURS', 'PHAR', 'PHYS',
                        'PSYC','SOCI','VETE']
    keys (list): List of keys from which to extract and tokenize text. it contains:
                        ['title', 'abstract', 'subjareas', 'keywords', 'asjc',
                          'body_text', 'author_highlights']
    save_cache (bool): Whether to use a temporary file for storing tokens.
    cache_file (str): Path to the temporary file for token storage.

    Returns:
    A generator that yields tokens from the dataset.
    '''
    # Load the dataset from hugging face 
    # Note: hugging face automatically split the dataset into 'train', 'test' and 'validation'
    dataset = load_dataset(dataset_name, trust_remote_code=True)
    
    # Filter the dataset by subject area if specified
    if subject_areas:
        dataset = dataset.filter(lambda x: any(sa in x['subjareas'] for sa in subject_areas))

    if save_cache:
        # Open a temporary file in write mode to store tokens
        with open(cache_file, 'w') as f:
            for key in keys:
                print('Now')
                for sentences in tqdm(list(flatten(dataset['train'][key])), desc=f"Processing {key}"):
                    tokens = word_tokenize(sentences)
                    json.dump(tokens, f)
                    f.write('\n')  # Write each list of tokens on a new line
        return tokens_generator(cache_file)  # Return the path to the cached file
    else:
        # Process all tokens in memory (for small datasets)
        tokens = []
        for key in keys:
            for sentences in tqdm(list(flatten(dataset['train'][key])), desc=f"Processing {key}"):
                tokens.extend(word_tokenize(sentences))
        return tokens


import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, skip_first=1, skip_last=2):
    """
    Extract text from specified pages of a PDF.

    Args:
        pdf_path (str): The path to the PDF file.
        skip_first (int, optional): The number of pages to skip from the beginning. Defaults to 1.
        skip_last (int, optional): The number of pages to skip from the end. Defaults to 2.

    Returns:
        str: The extracted text from the specified pages of the PDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    start_page = skip_first if skip_first else 0
    end_page = len(doc) - skip_last

    for page_number in range(start_page, end_page):
        page = doc.load_page(page_number)
        text += page.get_text("text")

    doc.close()
    return text

import re

def clean_text(text):
    """Clean and preprocess extracted text."""
    text = re.sub(r'Page \d+ of \d+', '', text)
    text = re.sub(r'[\r\n]+', ' ', text)
    return text.strip()
