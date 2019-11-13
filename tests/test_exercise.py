import pytest
from exercise import filter_words, get_common_words, tokenize_text


def test_get_common_words():
    assert get_common_words()


def test_tokenize_text():
    text = 'This is a good sentance'
    assert tokenize_text(text) == ['This', 'is', 'a', 'good', 'sentance']


def test_filter_words():
    words = ['This', 'is', 'entertaining']
    assert filter_words(words) == ['this', 'entertain']
