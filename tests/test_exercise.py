from collections import defaultdict

import pytest
from exercise import (Word, filter_words, get_common_words, populate_map,
                      process_folder, tokenize_text)


def test_get_common_words():
    assert get_common_words()


def test_tokenize_text():
    text = 'This is a good sentance'
    assert tokenize_text(text) == ['This', 'is', 'a', 'good', 'sentance']


def test_filter_words():
    words = ['This', 'is', 'entertaining']
    assert filter_words(words) == ['this', 'entertain']


def test_populate_map():
    word_map = defaultdict(Word)
    populate_map(['test'], word_map, 'test_doc')
    assert 'test' in word_map
    assert word_map['test'].count == 1
    assert 'test_doc' in word_map['test'].documents


def test_process_folder():
    words = process_folder('./tests/empty')
    assert words == {}
