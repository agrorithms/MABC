import pytest
from LRUCacheDict import LRUCacheDict


def test_value_set_item():
    testLRU =  LRUCacheDict(5)
    assert len(testLRU)==0  # initial length 0
    testLRU['key']='value' 
    assert testLRU['key'] == 'value' # test set item and get item
    assert len(testLRU)==1 # new length is 1
    assert 'key' in testLRU # finds existing key in cache
    assert 'key1' not in testLRU # non existent key not found in cache
    testLRU['testkey2'] = 'testvalue2'
    assert len(testLRU) == 2
    assert testLRU['testkey2'] == 'testvalue2'
    assert testLRU['key'] == 'value' #adding another value doesnt change existing
    
def test_get_item_error():
    testLRU =  LRUCacheDict(5)
    testLRU['key1']='value1'
    testLRU['key2'] = 'value2'
    with pytest.raises(KeyError): #__get__ keyerror
        _ = testLRU['key3'] #__get__ keyerror

def test_value_get():
    testLRU =  LRUCacheDict(5)
    testLRU['key'] = 'value'
    assert testLRU.get('key') == 'value' #existing key returns key's value
    assert testLRU.get('key2','default_val')=='default_val' #.get default
    assert testLRU.get('key2')==None #.get default w/o provided default -> None

def test_order():
    testLRU =  LRUCacheDict(5)
    testLRU['a'] = 1
    testLRU['b'] = 2
    testLRU['c'] = 3
    assert [key for key in testLRU] == ['c','b','a'] #test iteration order
    assert [key for key in testLRU] == ['c','b','a'] # ensure iter doesnt change recency

def test_stretch():
    testLRU =  LRUCacheDict(5)
    testLRU['a'] = 1
    testLRU['b'] = 2
    testLRU['c'] = 3
    expected_repr = "{c : 3, b : 2, a : 1}"
    assert repr(testLRU) == expected_repr #test repr accuracy
    assert repr(testLRU) == expected_repr # ensure repr doesnt change recency

def test_pop():
    testLRU =  LRUCacheDict(5)
    testLRU['a'] = 1
    testLRU['b'] = 2
    testLRU['c'] = 3
    assert testLRU.pop('b') == 2 #test pop returns value
    assert len(testLRU) == 2 #test pop changed length
    assert [key for key in testLRU] == ['c','a'] # test pop removed item from dict
    assert testLRU.pop('b','NO!') == 'NO!' # test pop default val
    assert testLRU.pop('b',None) == None # test pop default val works as None
    with pytest.raises(KeyError): # test pop noneexistent item without default raises error
        _ = testLRU.pop('b') # test pop noneexistent item without default raises error


def test_eviction():
    lilLRU = LRUCacheDict(3)
    for i in range(lilLRU.capacity+1):
        lilLRU[i]=f'test_val_{i}'
    assert [key for key in lilLRU] == [3,2,1] # test eviction of one key
    assert [key for key in lilLRU] == [3,2,1] # ensure iter doesnt change recency

    bigLRU = LRUCacheDict(100)
    expected = []
    for i in range(bigLRU.capacity*2):
        bigLRU[i]=f'test_val_{i}'
    for i in range(bigLRU.capacity*2-1,bigLRU.capacity-1,-1):
        expected.append(i)
    assert [key for key in bigLRU] == expected # test eviction of many keys
    assert [key for key in bigLRU] == expected # test iter doesnt change recency
    
def test_order_changes():
    lilLRU = LRUCacheDict(3)
    for i in range(lilLRU.capacity+1):
        lilLRU[i]=f'test_val_{i}'    
    assert lilLRU.get(1) =='test_val_1' #test .get
    assert [key for key in lilLRU] == [1,3,2] #test __get__ changes recency
    lilLRU[3]='LRU'
    assert [key for key in lilLRU] == [3,1,2] #test __set__ changes recency
    assert lilLRU[3]=='LRU' #test __set__ sets value
    lilLRU[4]='newLRU'
    assert lilLRU[4]=='newLRU' #test __set__ sets value
    assert [key for key in lilLRU] == [4,3,1] #test __set__ changes recency and evicts LRU
    assert lilLRU.get(2,None) == None # test.get default None
    assert [key for key in lilLRU] == [4,3,1] #ensure failed get does not change recency