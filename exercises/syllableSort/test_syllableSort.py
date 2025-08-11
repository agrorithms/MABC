from syllableSort import syllableSort

def test_empty():
    assert syllableSort([])==[]
    assert syllableSort(['','','','',''])==['','','','','']



def test_all_same_syllable():
    assert syllableSort(['hi','bye','tri','guy','hey']) == ['bye','guy','hey','hi','tri']
    assert syllableSort(['hello','testing','python','mara','question']) == ['hello','mara','python','question','testing']


def test_multiple_syllables():
    assert syllableSort(['hello','hi','','goes','marathon','kayak','two']) == ['','goes','hi','kayak','two','hello','marathon']
    assert syllableSort(['syllable','syllabus','centipede','cricket','stars']) == ['stars','cricket','syllable','syllabus','centipede']


def test_start_with_syllable():
    assert syllableSort(['ello','mat']) == ['mat','ello']
    assert syllableSort(['orangutang','one','twowo','threereeree','fourororor','highfiveiveiveive']) == ['one','twowo','threereeree','fourororor','orangutang','highfiveiveiveive']
