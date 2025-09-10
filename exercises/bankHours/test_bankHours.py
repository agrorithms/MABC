import pytest
from bankHours import BankHours
from bankHours import isInRange


test1= BankHours([[9,10],[9.5,12],[10,11],[19,24],[3,8],[3,7],[4,7],[2,3],[18,4],[20,6],[21,2]])

@pytest.mark.parametrize ('hours,expected', [
    ([4,8], True),
    ([4,9], False),
    ([9,1], False),
    ([18,8], True),

])
def test_covered_order(hours,expected):
    assert test1.isCovered(hours) == expected

def test_bank_hours():
    assert test1.hours = [0, 8], [9, 12], [18, 24]