import pytest
from bankHours import TimeRange
from bankHours import BankHours
from bankHours import isInRange



test1= BankHours([TimeRange(9,10),TimeRange(9.5,12),TimeRange(10,11),TimeRange(19,24),TimeRange(3,8),TimeRange(3,7),TimeRange(4,7),TimeRange(2,3),TimeRange(18,4),TimeRange(20,6),TimeRange(21,2)])

@pytest.mark.parametrize ('hours,expected', [
    (TimeRange(4,8), True),
    (TimeRange(4,9), False),
    (TimeRange(9,1), False),
    (TimeRange(18,8), True),

])
def test_covered_order(hours,expected):
    assert test1.isCovered(hours) == expected

def test_bank_hours():
    assert test1.hours ==[TimeRange(0, 8), TimeRange(9, 12), TimeRange(18, 24)]