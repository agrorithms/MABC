import pytest
from random import randint, seed
from bankHours import TimeRange, BankHours, isInRange




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



#AI Test Case

def generate_random_timeranges(n=1000, wrap_chance=0.2):
    """Generate n random TimeRanges, some wrapping around midnight."""
    seed(42)
    ranges = []
    for _ in range(n):
        start = randint(0, 23)
        end = randint(0, 23)
        if randint(0, 100) < wrap_chance * 100:
            # force wrap-around
            if end >= start:
                end = (start - 1) % 24
        ranges.append(TimeRange(start, end))
    return ranges

def test_bankhours_stress():
    # Create many overlapping + wrapping hours
    bank_ranges = generate_random_timeranges(2000, wrap_chance=0.3)
    bh = BankHours(bank_ranges)

    # Hours should be merged and sorted
    for i in range(1, len(bh.hours)):
        assert bh.hours[i].open >= bh.hours[i-1].open
        assert bh.hours[i].open > bh.hours[i-1].close

    # Spot check coverage
    # Full 24h coverage if ranges cover midnight wrap
    full_day = TimeRange(0, 24)
    covered_any = any(isInRange(openHours, full_day) for openHours in bh.hours)
    if covered_any:
        assert bh.isCovered(full_day)

    # Random samples
    samples = [
        TimeRange(9, 12),
        TimeRange(22, 23),
        TimeRange(23, 2),   # wrap-around trade
        TimeRange(15, 18),
    ]
    for s in samples:
        # isCovered must agree with manual check
        manual = any(isInRange(openHours, s) for openHours in bh.hours) or \
                 (s.close < s.open and
                  any(isInRange(openHours, TimeRange(0, s.close)) for openHours in bh.hours) and
                  any(isInRange(openHours, TimeRange(s.open, 24)) for openHours in bh.hours))
        assert bh.isCovered(s) == manual



def manual_isCovered(hours: list[TimeRange], tr: TimeRange) -> bool:
    if tr.close >= tr.open:
        return any(isInRange(openHours, tr) for openHours in hours)
    else:
        wrap1 = TimeRange(tr.open, 24)
        wrap2 = TimeRange(0, tr.close)
        wrap1_ok = any(isInRange(openHours, wrap1) for openHours in hours)
        wrap2_ok = any(isInRange(openHours, wrap2) for openHours in hours)
        return wrap1_ok and wrap2_ok

def random_timerange():
    start = randint(0, 23)
    end = randint(0, 23)
    return TimeRange(start, end)

def test_bankhours_isCovered_stress():
    seed(123)
   
    bank_ranges = [random_timerange() for _ in range(5)]
    bh = BankHours(bank_ranges)

    # stress check isCovered on many random trade ranges
    for _ in range(1000):
        trade = random_timerange()
        assert bh.isCovered(trade) == manual_isCovered(bh.hours, trade)

    # also spot check edge conditions
    edge_cases = [
        TimeRange(0, 0),    # zero-length
        TimeRange(0, 24),   # full day
        TimeRange(23, 1),   # overnight wrap
        TimeRange(12, 12),  # zero-length midday
    ]
    for tr in edge_cases:
        assert bh.isCovered(tr) == manual_isCovered(bh.hours, tr)