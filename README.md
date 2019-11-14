# Create Hashtags
Given a set of documents, find the most common occurring words, and the sentences where
they are used.

## Design
Initial thoughts and assumptions to consider for this exercise are:
- Words are separated by spaces but could by hyphenated
- Words are formed in many different ways and stems (e.g. ing, ed, es, en ic and isation)
- The most common words should exclude stop words (e.g. and, or, is, etc)

The simplest implementation is to iterate through the documents, tokenise the contents
and build up a hashmap (dict) of all the unique words encountered with a count and
reference to the document it was found in. There can be filters applied to either ignore
the word or store it against a different key (i.e. taking = take).

A Natural language Processor (such as NLTK) can help tokenise the documents and identify the unique words.

## Pre-requisites
To install requirements and enable virtual environment in Python 3.7:
`
$ pipenv install
$ pipenv shell
$ python -m nltk.downloader popular
`

## Usage
To run the exercise:
'
$ python exercise.py
'

## Run tests
To run the tests:
`
$ pytest
`

## TODO
- Filter out just nouns with pos_tag or TextBlob
- Output the table to HTML
