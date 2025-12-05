import pytest
from binaryTree import BinaryTree
from node import Node

def test_repr_node():
    testNode = Node(4)
    assert testNode.__repr__() == "{'value': 4, 'left': None, 'right': None}"
    testNode.left = Node(1)
    testNode.right = Node(2)
    assert testNode.__repr__() == "{'value': 4, 'left': 1, 'right': 2}"
    testNode2 = Node(4)
    testNode2.left = Node(1)
    testNode2.right = Node(2)

def test_eq_node():

    testNode1 = Node(4)
    testNode2 = Node(4)
    assert testNode1 == testNode2
    
    testNode1.left = Node(1)
    testNode2.left = Node(1)
    assert testNode1.left == testNode2.left
    testNode1.right = Node(2)
    assert not testNode1 == testNode2
    
    testNode2.left = Node(1)
    testNode2.right = Node(2)
    assert testNode1 == testNode2

@pytest.mark.parametrize ('addNodes,expected', [
    ([20,5,30,15], [1,1,2,2]),
    ([20,5,30,40,50,60,70], [1,1,2,3,4,5,6]),
    ([20,5,100,25,90,30,80], [1,1,2,3,4,5,6]),
    ([20,5,100,25,90,30,80,22,95,27,85], [1,1,2,3,4,5,6,6,6,6,7]),
    ([20,5,100,25,90,30,80,22,95,27,85,11,12,13,0,19,105,110], [1,1,2,3,4,5,6,6,6,6,7,7,7,7,7,7,7,7]),
    ([5,15,2,7,1,3,12,18], [1,1,2,2,3,3,3,3])
    
])
def test_max_depth_node(addNodes,expected):
    testNode=Node(10)
    assert testNode.maxDepth()==0
    for i in range(len(addNodes)):
        testNode.add(addNodes[i])
        assert testNode.maxDepth()== expected[i]
    testNode.add(20)
    

def test_add():
    tree = BinaryTree()
    tree.add(7)
    assert tree.head.value == 7
    assert tree.head.left == None
    assert tree.head.right == None
    tree.add(9)
    assert tree.head.value == 7
    assert tree.head.right.value == 9
    assert tree.head.left == None
    tree.add(5)
    assert tree.head.value == 7
    assert tree.head.right.value == 9
    assert tree.head.left == Node(5)
    tree.add(1)
    assert tree.head.value == 7
    assert tree.head.right.value == 9
    assert tree.head.left.value == 5
    assert tree.head.left.left.value == 1
    tree.add(3)
    assert tree.head.value == 7
    assert tree.head.right.value == 9
    assert tree.head.left.value == 5
    assert tree.head.left.left.value == 1
    assert tree.head.left.left.right.value == 3
    tree.add(5)
    assert tree.head.value == 7
    assert tree.head.right.value == 9
    assert tree.head.left.value == 5
    assert tree.head.left.left.value == 1
    assert tree.head.left.left.right.value == 3

@pytest.mark.parametrize ('addNodes,expected', [
    ([7,9,5,1,3,5,-12,-13,-1], [7,7,5,1,1,1,-12,-13,-13]),
])
def test_min(addNodes,expected):
    tree=BinaryTree()
    assert tree.min() == None
    for i in range(len(addNodes)):
        tree.add(addNodes[i])
        assert tree.min().value == expected[i]

@pytest.mark.parametrize ('addNodes,expected', [
    ([7,9,5,1,10,5,10,11,12,13,-1], [7,9,9,9,10,10,10,11,12,13,13]), 
])
def test_max(addNodes, expected):
    tree=BinaryTree()
    assert tree.min() == None
    for i in range(len(addNodes)):
        tree.add(addNodes[i])
        assert tree.max().value == expected[i]


def test_contains():
    tree=BinaryTree()
    assert not tree.contains(5)
    assert not tree.contains(7)
    tree.add(7)
    assert not tree.contains(5)
    assert tree.contains(7)

    tree.add(9)
    assert not tree.contains(5)
    tree.add(5)
    assert not tree.contains(1)
    tree.add(1)
    tree.add(10)
    tree.add(5)
    tree.add(10)
    tree.add(11)
    tree.add(12)
    tree.add(13)

    assert not tree.contains(-1)
    tree.add(-1)
    assert tree.contains(7)
    assert tree.contains(5)
    assert tree.contains(9)
    assert tree.contains(1)
    assert tree.contains(10)
    assert tree.contains(11)
    assert tree.contains(12)
    assert tree.contains(13)
    assert tree.contains(-1)
    assert not tree.contains(79)


def test_remove():
    tree=BinaryTree()
    
    tree.add(7)
    assert tree.head == Node(7)
    tree.remove(7)
    assert tree.head == None #remove lone node
    tree.add(7)
    assert tree.head == Node(7)
    tree.add(6)
    assert tree.head.value == 7
    head1 = Node(7)
    head1.left=Node(6)
    assert tree.head == head1
    tree.remove(7)
    assert tree.head == Node(6) # remove head with only left child
    tree.remove(6)
    assert tree.head == None
    tree.add(7)
    tree.add(8)
    tree.remove(7)
    assert tree.head == Node(8) # remove head with only right child
    tree.add(7)
    assert tree.head.value == 8
    assert tree.head.left.value == 7
    tree.add(6)
    assert tree.head.value == 8
    assert tree.head.left.value == 7
    assert tree.head.left == head1
    tree.remove(7)
    assert tree.head.value == 8 # remove left child with only left child ,test head remain
    assert tree.head.left == Node(6) # # remove left child with only left child test leaf child remains attached to head
    
    tree.add(9)
    assert tree.head.value == 8
    assert tree.head.left == Node(6)
    assert tree.head.right == Node(9)
    tree.add(10)
    tree.add(7)
    tree.add(11)
    tree.remove(8)
    assert tree.head.value == 7
    assert tree.head.left.value == 6
    assert tree.head.right.value==9
    assert tree.head.right.right.value==10
    assert tree.head.right.right.right.value==11 # test remove head with left and right children

    tree.add(3)
    tree.add(5)
    tree.add(2)
    tree.add(4)
    assert tree.head.left.left.value == 3
    assert tree.head.left.left.right.value == 5
    assert tree.head.left.left.left.value == 2
    assert tree.head.left.left.right.left.value == 4
    
    tree.remove(3) # remove depth 1 left child with left and right children
    assert tree.head.left.left.value == 2 #test remove left child with left and right children
    assert tree.head.left.left.right.value == 5 #test remove left child with left and right children
    assert tree.head.left.left.right.left.value == 4 #test remove left child with left and right children

    tree.remove(10)
    assert tree.head.right.right.value==11 # test remove right child with only right child

    tree.add(10)
    tree.add(15)
    tree.remove(11)
    assert tree.head.right.right.value==10 # test remove  right child with left and right children
    assert tree.head.right.right.right.value==15 # remove  right child with left and right children
    assert tree.head.right.right.left==None
    newTree = BinaryTree()
    newTree.add(10)
    newTree.add(5)
    newTree.add(7)
    newTree.add(6)
    newTree.remove(5)

    assert newTree.head.left.value==6 # test remove left child with right child
    assert newTree.head.left.right.value==7


    newTree.add(15)
    newTree.add(12)
    newTree.add(13)
    newTree.remove(15)
    assert newTree.head.right.value==13 # test remove right child with left child
    assert newTree.head.right.left.value==12
    newTree.remove(200)
    assert newTree.head.right.value==13 # test remove right child with left child
    assert newTree.head.right.left.value==12


@pytest.mark.parametrize ('addNodes,expected', [
    ([], None),
    ([100], 0),
    ([100,200], 1),
    ([100,50],1),
    ([100,200,300], 2),
    ([100,200,150], 2),
    ([100,50,25], 2),
    ([100,50,75], 2),
    ([100,200,300,50], 2),
    ([100,200,300,50,0], 2),
    ([100,200,300,50,0,75], 2),
    ([100,200,300,50,0,75,87], 3),
    ([100,200,300,50,0,75,62], 3),
    ([100,200,300,50,0,150,175], 3),
    ([100,200,300,50,0,150,125], 3),
    ([100,200,300,50,0,150,125,75], 3),
    ([100,200,300,50,0,150,125,75,25], 3),
    ([100,200,300,50,0,150,125,75,25,-25], 3),
    ([100,200,300,50,0,150,125,75,25,-25,101], 4),

])
def test_maxdepth(addNodes: list[int], expected: int):
    depthTree = BinaryTree()
    for n in addNodes:
        depthTree.add(n)
    assert depthTree.maxDepth() == expected


def test_maxdepth_old():
    depthTree = BinaryTree()
    assert depthTree.maxDepth() == None
    depthTree.add(100)
    assert depthTree.maxDepth() == 0
    depthTree.add(150)
    assert depthTree.maxDepth() == 1
    depthTree.add(50)
    assert depthTree.maxDepth() == 1
    depthTree.add(25)
    assert depthTree.maxDepth() == 2
    depthTree.add(200)
    assert depthTree.maxDepth() == 2
    depthTree.add(175)
    assert depthTree.maxDepth() == 3


def test_nodeAdd():
    start = Node(100)
    start.add(10)
    assert start.left.value == 10
    start.add(2)
    assert start.left.left.value == 2
    start.add(200)
    start.add(150)
    assert start.right.value == 200
    assert start.right.left.value == 150
    start.add(7)
    start.add(15)
    assert start.left.left.right.value == 7
    assert start.left.right.value == 15



@pytest.mark.parametrize ('addNodes,expected', [
    ([100], 100),
    ([100,50,20], 20),
    ([100,200,300], 100),
    ([100,200,1], 1),
    ([100,50,400,2,1,-1],-1),
    ([100,200,300,5000,0], 0),
    ([100,200,150,-1000], -1000),
    ([100,50,25,75,87,23,56,12,873,536,65], 12)

])
def test_nodemin(addNodes, expected):
    if addNodes:
        start = Node(addNodes[0])
    for n in addNodes:
        start.add(n)
    assert start.min().value == expected    


@pytest.mark.parametrize ('addNodes,expected', [
    ([100], 100),
    ([100,50,20], 100),
    ([100,200,300], 300),
    ([100,200,1], 200),
    ([100,50,400,2,1,-1],400),
    ([100,200,300,5000,0], 5000),
    ([100,200,150,-1000], 200),
    ([100,50,25,75,87,23,56,12,873,536,65], 873)

])
def test_nodemax(addNodes, expected):
    if addNodes:
        start = Node(addNodes[0])
    for n in addNodes:
        start.add(n)
    assert start.max().value == expected


@pytest.mark.parametrize ('addNodes,value,expected', [
    ([100], 100, True),
    ([100,50,20], 100, True),
    ([100,200,300], 300, True),
    ([100,200,1], 200, True),
    ([100,50,400,2,1,-1], 1, True),
    ([100,200,300,5000,0], 200, True),
    ([100,200,150,-1000,0,50], 0, True),
    ([100,50,25,75,87,23,56,12,873,536,65], 65, True),
    ([100], 0, False),
    ([100,50,20], 101, False),
    ([100,200,300], 0, False),
    ([100,200,1], 2, False),
    ([100,50,400,2,1,-1], 0, False)

])
def test_nodeContains(addNodes, value, expected):
    
    start = Node(addNodes[0])
    for n in addNodes:
        start.add(n)
    assert start.contains(value) == expected

def test_nodeRemove():
    headNode=Node(100)
    headNode.add(200)
    headNode.remove(200)
    assert headNode == Node(100) #remove only child (right)
    headNode.add(200)
    headNode.remove(100)
    assert headNode == Node(200) #remove only child (left)
    headNode.add(100)
    headNode.add(300)
    headNode.remove(100)
    assert headNode.value == 200 # remove leaf node / left child
    assert headNode.right.value == 300 # # remove leaf node / left child
    headNode.add(100)
    headNode.add(50)
    headNode.add(150)
    headNode.remove(100)
    assert headNode.value == 200 # remove a left child with two children
    assert headNode.right.value == 300 # remove a left child with two children
    assert headNode.left.value == 50 # remove a left child with two children
    assert headNode.left.right.value == 150 # remove a left child with two children
    headNode.remove(50)
    assert headNode.value == 200 # remove a left child with only right child
    assert headNode.right.value == 300 # remove a left child with only right child
    assert headNode.left.value == 150 # remove a left child with only right child
    headNode.add(100)
    headNode.remove(150)
    assert headNode.value == 200 # remove a left child with only left child
    assert headNode.right.value == 300 # remove a left child with only left child
    assert headNode.left.value == 100 # remove a left child with only left child
    headNode.add(250)
    headNode.remove(300)
    assert headNode.value == 200 # remove a right child with only left child
    assert headNode.right.value == 250 # remove a right child with only left child
    assert headNode.left.value == 100 # remove a right child with only left child
    headNode.add(400)
    headNode.remove(250)
    assert headNode.value == 200 # remove a right child with only right child
    assert headNode.right.value == 400 # remove a right child with only right child
    assert headNode.left.value == 100 # remove a right child with only right child
    
    headNode.remove(250)
    assert headNode.value == 200 # remove a right child with only right child
    assert headNode.right.value == 400 # remove a right child with only right child
    assert headNode.left.value == 100 # remove a right child with only right child
    headNode.add(500)
    headNode.add(275)
    headNode.remove(400)
    assert headNode.value == 200 # remove a right child with both child
    assert headNode.right.value == 275 # remove a right child with both child
    assert headNode.right.right.value == 500 # remove a right child with both child
    assert headNode.left.value == 100 # remove a right child with both child
    headNode.add(251)
    headNode.add(255)
    headNode.add(254)
    headNode.add(257)
    headNode.remove(275)
    assert headNode.value == 200 # remove a right child with a long route tothe in order predecessor
    assert headNode.right.value == 257 # remove a right child with a long route tothe in order predecessor
    assert headNode.right.right.value == 500 # remove a right child with a long route tothe in order predecessor
    assert headNode.left.value == 100 # remove a right child with a long route tothe in order predecessor
    assert headNode.right.left.value == 251 # remove a right child with a long route tothe in order predecessor
    assert headNode.right.left.right.value == 255 # remove a right child with a long route tothe in order predecessor
    assert headNode.right.left.right.left.value == 254 # remove a right child with a long route tothe in order predecessor
    assert headNode.right.left.right.right == None # remove a right child with a long route tothe in order predecessor
    headNode.add(253)
    headNode.remove(251)
    assert headNode.value == 200 # remove a right child with no left child and a long route tothe in order successor
    assert headNode.right.value == 257 # remove a right child with no left child and a long route tothe in order successor
    assert headNode.right.right.value == 500 # remove a right child with no left child and a long route tothe in order successor
    assert headNode.left.value == 100 # remove a right child with no left child and a long route tothe in order successor
    assert headNode.right.left.value == 253 # remove a right child with no left child and a long route tothe in order successor
    assert headNode.right.left.right.value == 255 # remove a right child with no left child and a long route tothe in order successor
    assert headNode.right.left.right.left.value == 254 # remove a right child with no left child and a long route tothe in order successor
    assert headNode.right.left.right.left.left == None # remove a right child with no left child and a long route tothe in order successor
    assert headNode.right.left.right.right == None # remove a right child with no left child and a long route tothe in order successor


