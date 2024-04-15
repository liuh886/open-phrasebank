from setuptools import setup, find_packages 

setup(
    name="openphrasebank",
    version="0.1.0",
    author="Zhihao",
    author_email="liuzhihao109@foxmial.com",
    description="PhraseBank is a utility designed to help users build customized phrasebanks from various texts or corpora.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/liuh886/open_phrasebank",
    packages=find_packages(),
    install_requires=[
        'nltk', 
        'spacy',
        'pymupdf',
        'tqdm',  
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
    package_dir={"": "openphrasebank"},
    packages=find_packages(where="openphrasebank"),
    include_package_data=True,  # This tells setuptools to check MANIFEST.in
    package_data={
        "": ["data/*", "phrasebanks/*"],  # include all files in the data and phrasebanks directories
    },
)