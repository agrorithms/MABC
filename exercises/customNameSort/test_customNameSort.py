from customNameSort import customNameSort

def test_only_length():
    assert customNameSort(['a','aa','aaa','aaaa','aaaaa'])==['a','aa','aaa','aaaa','aaaaa'] #already in order
    assert customNameSort(['aaaaa','aaaa','aaa','aa','a'])==['a','aa','aaa','aaaa','aaaaa'] #backwards
    assert customNameSort(['aaaa','aaaaa','a','aaa','aa'])==['a','aa','aaa','aaaa','aaaaa'] # mixed


def test_only_reverse_alphabetical():
    assert customNameSort(['a','b','c','d','e']) == ['e','d','c','b','a'] # reversed
    assert customNameSort(['e','d','c','b','a']) == ['e','d','c','b','a'] # already in order
    assert customNameSort(['c','e','a','d','b']) == ['e','d','c','b','a'] # mixed

def test_bros_and_hoes():
    assert customNameSort(['bros','hoes','toes','goes','joes','aoes','coes']) == ['toes','joes','bros','hoes','goes','coes','aoes'] # bros and hoes
    assert customNameSort(['hoes','toes','goes','joes','aoes','coes']) == ['toes','joes','hoes','goes','coes','aoes'] # hoes no bros
    assert customNameSort(['bros','toes','goes','joes','aoes','coes']) == ['toes','joes','goes','coes','bros','aoes'] # bros no hoes


def test_length_and_rev_alphabetical():
    assert customNameSort(['nir','louis','miguel','reuben','shoran','juntoku','james','tobias'])==['nir','louis','james','tobias','shoran','reuben','miguel','juntoku']

def test_bros_hoes_others():
    assert customNameSort(['OMEGA', 'AL', 'BROS', 'HOES', 'BOB', 'ZED', 'AA'])==['AL','AA','ZED','BOB','BROS','HOES','OMEGA']
    assert customNameSort(['OMEGA', 'AL', 'BROS', 'HOES', 'BOB', 'ZED', 'FFFF','LLLL'])==['AL','ZED','BOB','LLLL','BROS','HOES','FFFF','OMEGA']

def test_case_insensitive():
    assert customNameSort(['a','B','c','D','e']) == ['e','D','c','B','a'] # reversed
    assert customNameSort(['E','d','C','b','a']) == ['E','d','C','b','a'] # already in order
    assert customNameSort(['c','e','A','d','b']) == ['e','d','c','b','A'] # mixed

def test_duplicate_strings():
    assert customNameSort(['bros', 'hoes', 'hoes', 'bros', 'ww', 'ww', 'aa', 'aa', 'goes', 'goes', 'joes', 'joes']) == ['ww', 'ww', 'aa', 'aa', 'joes', 'joes', 'bros', 'bros', 'hoes', 'hoes', 'goes', 'goes']
    assert customNameSort(['bros','hoes','bros','hoes','bros']) == ['bros','bros','bros','hoes','hoes'] # mixed
