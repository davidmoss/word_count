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
from collections import defaultdict
from pathlib import Path

from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize


class Word():
    def __init__(self):
        self.count = 0
        self.documents = set()

    def __repr__(self):
        return f'count={self.count} documents={self.documents}'


def get_common_words():
    return True


def tokenize_text(text):
    """
    Tokenizes text string into words

    Parameters:
    text (str): Body of text to split into words

    Returns:
    list: Words from text
    """
    return word_tokenize(text)


def filter_words(words):
    """
    Transforms words into their shortend form without any stems and filters out
    stop words

    Parameters:
    words (list): List of words

    Returns:
    list: New list of words after filtering
    """
    stemmer = SnowballStemmer("english")
    stop_words = stopwords.words('english')
    return [stemmer.stem(word) for word in words if word not in stop_words]


def populate_map(words, word_map, filename):
    """
    Populates word_map hashmap with Word objects containing count and occurance
    or each word

    Parameters:
    words (list): List of words
    word_map (dict): Dictionary of unique words
    filename (str): Of document words have come from
    """
    for word in words:
        word_map[word].count += 1
        word_map[word].documents.add(filename)


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

    for file in path.iterdir():
        if file.is_file():
            with file.open() as f:
                words = tokenize_text(f.read())
                words = filter_words(words)
                populate_map(words, word_map, file.name)
    return word_map


if __name__ == '__main__':
    world_map = process_folder('./test_docs')
    import pprint
    pprint.pprint(world_map)
