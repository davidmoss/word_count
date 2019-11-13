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


def get_common_words():
    return True


def tokenize_text(text):
    return word_tokenize(text)


def filter_words(words):
    stemmer = SnowballStemmer("english")
    stop_words = set(stopwords.words('english'))
    return [stemmer.stem(word) for word in words if word not in stop_words]


def populate_map(words, word_map):
    for word in words:
        word_map[word] += 1


def process_folder(path):
    word_map = defaultdict(int)

    for file in path.iterdir():
        if file.is_file():
            with file.open() as f:
                words = tokenize_text(f.read())
                words = filter_words(words)
                populate_map(words, word_map)
    return word_map


if __name__ == '__main__':
    path = Path('./test_docs')
    word_map = process_folder(path)
