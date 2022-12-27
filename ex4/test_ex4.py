from hangman import *


def test_update_word_pattern():
    assert update_word_pattern('apple', '___l_', 'p') == '_ppl_'
    assert update_word_pattern('peace', '_____', 'e') == '_e__e'
    assert update_word_pattern('pie', '___', 'p') == 'p__'
