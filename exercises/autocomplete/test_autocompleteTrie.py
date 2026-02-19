import pytest, os


def test_autocomplete(monkeypatch,capsys):
    inputs=iter('abcdefghiijklmnopqnrstuvwxnyzxyxy') # put n after 'q' and 'x' to escape the quitting process
    monkeypatch.setattr('builtins.input',lambda _: next(inputs))

    from autocompleteTrie import Autocomplete

    a=Autocomplete('words_alpha.txt')
    out=capsys.readouterr()

    with open('autocompleteTestLog.txt', 'w') as f:
        f.write(out.out)
    assert os.path.exists('autocompleteTestLog.txt')