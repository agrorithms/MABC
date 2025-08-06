from minimumBorders import minBordersAB

def test_vertical_line_both_Sides():
    assert minBordersAB(1,+5j,[-2+4j, -4-8j],[3,1])==1 #from negative
    assert minBordersAB(0, 6j,[2+4j, -4-8j],[3,1])==1 # from positive
    assert minBordersAB(0, 6j,[2+2j, -4+3j],[2,4])==2    #from both sides


def test_horizontal_line_both_sides():
    assert minBordersAB(0, 6,[2+2j],[3]) == 1 # from positive
    assert minBordersAB(0, 6,[2-1j],[1]) == 1 # from negative
    assert minBordersAB(0, 6,[2+1j,2-1j],[2,2]) == 2 # from both sides

def test_out_of_bounds_city():
    assert minBordersAB(0, 3+6j,[-3-6j],[1]) == 0 # before A
    assert minBordersAB(0, 3+6j,[4+7j],[1]) == 0 # after B

def test_within_one_city():
    assert minBordersAB(10-6j, 5+2j,[-24+44j],[100])==0
    assert minBordersAB(10-6j, 5+2j,[-24+44j, 7-1j],[100,2])==1

def test_tangent_intersection():
    assert minBordersAB(1+1j,10+10j,[4+5j],[1])==1

def test_city_on_line():
    assert minBordersAB(1+1j,10+10j,[5+5j],[1])==1

def test_one_point_Within_city():
    assert minBordersAB(1+1j,10+10j,[0],[2])==1 #point a within
    assert minBordersAB(1+1j,10+10j,[10+11j],[2])==1 #point b within
