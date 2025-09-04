from recentCounter import RecentCounter

def test_two_users():
    counter=RecentCounter(3)
    assert counter.ping('alice',1)==1       #first ping
    assert counter.ping('alice',200)==2     #second ping user1
    assert counter.ping('bob',250)==1       #first ping user2
    assert counter.ping('alice',3000)==3    #third ping user1
    assert counter.ping('alice',3200) == 3  #fourth ping , but 3rd within specified duration user1
    assert counter.ping('bob',4000) == 1    #second ping user2 , outide specified duration
     
    assert counter.get_all('alice') == [1,200,3000,3200]    # get all user1
    assert counter.get_all('bob') == [250,4000]             # get all user2
