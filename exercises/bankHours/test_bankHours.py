import pytest
from bankHours import TimeRange, BankHours


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

def test_bankhours_isCovered_deterministic_with_boundaries():
    # Fixed input schedule with overlaps and wrap-around
    bank_hours = [
        TimeRange(0, 3),      # early morning
        TimeRange(2, 6),      # overlap with 0–3 → merges into 0–6
        TimeRange(8, 12),     # morning
        TimeRange(13, 17),    # afternoon
        TimeRange(20, 23),    # evening
        TimeRange(22, 2),     # wrap-around
    ]
    bh = BankHours(bank_hours)

    # Verify merge and order
    for i in range(1, len(bh.hours)):
        assert bh.hours[i].open > bh.hours[i-1].close, "Merged ranges overlap or unsorted"

    # Deterministic coverage expectations (True = should be covered)
    cases = [
        # --- standard and overlapping ranges ---
        (TimeRange(0, 1),  True),   # within merged 0–6
        (TimeRange(2, 5),  True),   # within merged 0–6
        (TimeRange(5, 8),  False),  # between 6–8 gap
        (TimeRange(8, 10), True),   # within 8–12
        (TimeRange(10, 12), True),  # boundary inclusive
        (TimeRange(12, 13), False), # closed gap
        (TimeRange(13, 17), True),  # full afternoon
        (TimeRange(15, 16), True),  # inside afternoon
        (TimeRange(17, 20), False), # closed gap
        (TimeRange(21, 23), True),  # within 20–23
        (TimeRange(23, 1),  True),  # within overnight wrap (22–2)
        (TimeRange(22, 2),  True),  # full wrap-around
        (TimeRange(0, 24),  False), # not full 24h coverage
        (TimeRange(11, 14), False), # crosses open and closed
        # --- boundary inclusivity tests ---
        (TimeRange(6, 8),   False), # between merged 0–6 and 8–12
        (TimeRange(0, 6),   True),  # exactly full merged range
        (TimeRange(6, 6),   True), # at boundary (end of open range)
        (TimeRange(8, 8),   True), # zero-length on start boundary
        (TimeRange(8, 12),  True),  # exactly full morning range
        (TimeRange(12, 12), True), # closed point boundary
        (TimeRange(20, 23), True),  # exact evening hours
        (TimeRange(23, 0),  True), # invalid reverse no-wrap
        (TimeRange(22, 24), True),  # end overlaps midnight (wrap range covers)
        # --- degenerate / edge cases ---
        (TimeRange(3, 3),   True),
        (TimeRange(0, 0),   True),
    ]

    for tr, expected in cases:
        result = bh.isCovered(tr)
        assert result == expected, f"{tr}: expected {expected}, got {result}"

    # Optional: check that wrap-around merge worked correctly
    # Expect hours to include the overnight continuation (22–2)
    assert any(h.open == 22 and h.close == 2 for h in bank_hours) or any(
        h.open <= 22 and h.close >= 2 for h in bh.hours
    )




