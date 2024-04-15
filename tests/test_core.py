import unittest
from unittest.mock import patch
from io import StringIO
from collections import defaultdict, Counter
from openphrasebank import tokens_generator, generate_multiple_ngrams

class TokensGeneratorTestCase(unittest.TestCase):
    def test_tokens_generator(self):
        # Create a mock file with sample data
        file_data = [
            '[1, 2, 3]',
            '[4, 5, 6]',
            '[7, 8, 9]',
            '[10, 11, 12]'
        ]
        mock_file = StringIO('\n'.join(file_data))

        # Patch the built-in open function to return the mock file
        with patch('builtins.open', return_value=mock_file):
            # Call the tokens_generator function
            generator = tokens_generator('/path/to/file', chunk_size=2)

            # Iterate over the generator and collect the yielded chunks
            chunks = [chunk for chunk in generator]

        # Assert the correctness of the yielded chunks
        expected_chunks = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12]
        ]
        self.assertEqual(chunks, expected_chunks)

class UtilitiesTestCase(unittest.TestCase):
    def test_generate_multiple_ngrams(self):
        # Define a mock tokens generator
        def mock_tokens_generator():
            yield ['I', 'love', 'GitHub']
            yield ['GitHub', 'is', 'awesome']

        # Call the generate_multiple_ngrams function with the mock tokens generator
        ngram_freqs = generate_multiple_ngrams(mock_tokens_generator(), n_values=[2, 3], prune_threshold=3)
        
        # Assert the correctness of the generated n-gram frequencies
        expected_ngram_freqs = defaultdict(Counter)
        expected_ngram_freqs[2].update({('I', 'love'): 1, ('love', 'GitHub'): 1, ('GitHub', 'is'): 1, ('is', 'awesome'): 1})
        expected_ngram_freqs[3].update({('I', 'love', 'GitHub'): 1, ('GitHub', 'is', 'awesome'): 1})
        self.assertEqual(ngram_freqs, expected_ngram_freqs)

if __name__ == '__main__':
    unittest.main()