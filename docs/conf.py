# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'open phrasebank'
copyright = '2024, Zhihao'
author = 'Zhihao'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# -- General configuration ---------------------------------------------------
#

extensions = [
    'furo',
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    "furo.sphinxext",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
    # notebook
    'nbsphinx',
]

nbsphinx_execute = 'never'
pygments_style = 'sphinx'
pygments_dark_style = "monokai"

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md', '.ipynb']  # Add '.ipynb'

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = True

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
#

html_theme = "furo"
html_title = "Open Phrasebank"
language = "en"

html_static_path = ["_static"]
html_theme_options = {
    "light_logo": "logo_light.png",
    "dark_logo": "logo_dark.png",
}