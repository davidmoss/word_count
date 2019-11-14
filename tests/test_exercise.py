from collections import defaultdict

from exercise import (Word, filter_words, get_common_words, populate_map,
                      process_folder, tokenize_text)


def test_get_common_words():
    test_word = Word()
    test_word.count = 1
    test_word.documents.add('test_doc')

    test_word5 = Word()
    test_word5.count = 5
    test_word5.documents.add('test_doc5')

    word_map = {'test': test_word, 'test5': test_word5}
    words = get_common_words(word_map, 1)
    assert 'test' in words
    assert 'test5' not in words


def test_tokenize_text():
    text = 'This is a good sentance. This is another one'
    assert tokenize_text(text) == [
        (
            'This is a good sentance.',
            ['This', 'is', 'a', 'good', 'sentance', '.'],
        ),
        (
            'This is another one',
            ['This', 'is', 'another', 'one'],
        ),
    ]


def test_filter_words():
    words = ['This', 'is', 'entertaining', '.']
    assert filter_words(words) == ['this', 'entertain']


def test_populate_map():
    word_map = defaultdict(Word)
    populate_map(['test'], word_map, doc_idx=0, sent_idx=5)
    assert 'test' in word_map
    assert word_map['test'].count == 1
    assert 0 in word_map['test'].documents
    assert 5 in word_map['test'].sentances


def test_process_folder():
    words, __, __ = process_folder('./tests/empty')
    assert words == {}
