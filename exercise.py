"""
Find the most common occurring words, and the sentences where they are used to
create the following table:

Word(#)    | Documents | Sentences containing the word
---------------------------------------------------
philosophy | x, y, z   | I don't have time for *philosophy*
           |           | Surely this was a touch of fine *philosophy*; though
                         no doubt he had never heard there was such a thing as
                         that.
           |           | Still, her pay-as-you-go *philosophy* implied she
                         didn't take money for granted.
---------------------------------------------------
---        | ---       | ---
"""
import string
from collections import OrderedDict, defaultdict
from itertools import islice
from pathlib import Path

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from spacy.lang.en.stop_words import STOP_WORDS


class Word():
    def __init__(self):
        self.count = 0
        self.documents = set()
        self.sentances = set()

    def add_occurance(self, doc_idx, sent_idx):
        self.count += 1
        self.documents.add(doc_idx)
        self.sentances.add(sent_idx)

    def __repr__(self):
        return f'count={self.count} documents={self.documents} sentances={self.sentances}'


def output_table(common_words, documents, sentances):
    import pprint
    pprint.pprint(common_words)


def get_common_words(word_map, count=10):
    """
    Get the most common words given a count of how many to return

    Parameters:
    word_map (dict): Dictionary of unique words

    Returns:
    list: Shortened list of common words matching length of count

    """
    # order by the word count
    words = OrderedDict(
        sorted(word_map.items(), key=lambda word: word[1].count, reverse=True)
    )
    # return the first count of common words
    return dict(islice(words.items(), count))


def tokenize_text(text):
    """
    Tokenizes text string into sentances and their words

    Parameters:
    text (str): Body of text to split into sentances and words

    Returns:
    list: List of tuples containing sentances and the words within it from the
          original text
    """
    # split by sentence
    sentances = sent_tokenize(text)
    # split each sentence by words
    return [(sentance, word_tokenize(sentance)) for sentance in sentances]


def filter_words(words):
    """
    Transforms words into their shortend form without any stems and filters out
    stop words and puncuation

    Parameters:
    words (list): List of words

    Returns:
    list: New list of words after filtering
    """
    # Remove stems
    lemmatizer = WordNetLemmatizer()
    # remove stop words and punctuation
    stop_words = list(STOP_WORDS) + list(string.punctuation) + stopwords.words('english')
    return [
        lemmatizer.lemmatize(word).lower()
        for word in words if word not in stop_words
    ]


def populate_map(words, word_map, doc_idx, sent_idx):
    """
    Populates word_map hashmap with Word objects containing count and occurance
    or each word

    Parameters:
    words (list): List of words
    word_map (dict): Dictionary of unique words
    doc_idx (int): Index of document name in global list
    sent_idx (int): Index of sentance in global list
    """
    for word in words:
        word_map[word].add_occurance(doc_idx, sent_idx)


def get_idx(l):
    return len(l) - 1


def process_folder(folder_path):
    """
    Get count of words and their occurance from a folder of text documents

    Parameters:
    path (str): Path to folder of documents

    Returns:
    dict: Unique words with their count and occurances
    """
    path = Path(folder_path)
    word_map = defaultdict(Word)
    documents = []
    sentances = []

    # iterate through folder to get files
    for file in path.iterdir():
        if file.is_file():
            with file.open() as f:
                text = f.read()
                if not text:
                    # Skip empty files
                    continue
                # build up list of document names
                documents.append(file.name)
                # get sentances and words from text
                doc_sentances = tokenize_text(text)
                for sentance, words in doc_sentances:
                    # build up list of sentances
                    sentances.append(sentance)
                    # filter out the puncuation, stems and stops words
                    words = filter_words(words)
                    # populate hashmap of words and occurances
                    populate_map(
                        words=words,
                        word_map=word_map,
                        doc_idx=get_idx(documents),
                        sent_idx=get_idx(sentances),
                    )
    return word_map, documents, sentances


if __name__ == '__main__':
    word_map, documents, sentances = process_folder('./test_docs')
    common_words = get_common_words(word_map)
    output_table(common_words, documents, sentances)
