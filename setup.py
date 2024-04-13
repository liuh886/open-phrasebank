from setuptools import setup, find_packages

setup(
    name="openphrasebank",
    version="0.1.0",
    author="Zhihao",
    author_email="your.email@example.com",
    description="A utility to build custom phrasebanks from text or corpus",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/liuh886/openphrasebank",
    packages=find_packages(),
    install_requires=[
        'nltk',  # Example dependency, replace with actual dependencies
        'spacy',
        'pymupdf',  
        'datasets', # Huggingface datasets
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'openphrasebank=openphrasebank.cli:main',  # Adjust according to your package structure
        ],
    },
)
