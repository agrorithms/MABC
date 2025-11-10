import pytest
from binaryTree import Node, BinaryTree

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

def test_min():
    tree=BinaryTree()
    assert tree.min() == None
    tree.add(7)
    assert tree.min() == 7
    
    tree.add(9)
    assert tree.min() == 7
    
    tree.add(5)
    assert tree.min() == 5
    
    tree.add(1)
    assert tree.min() == 1
   
    tree.add(3)
    assert tree.min() == 1
    
    tree.add(5)
    assert tree.min() == 1
    tree.add(-12)
    tree.add(-13)
    tree.add(-1)
    assert tree.min() == -13


def test_max():
    tree=BinaryTree()
    assert tree.max() == None
    tree.add(7)
    assert tree.max() == 7
    
    tree.add(9)
    assert tree.max() == 9
    
    tree.add(5)
    assert tree.max() == 9
    
    tree.add(1)
    assert tree.max() == 9
   
    tree.add(10)
    assert tree.max() == 10
    
    tree.add(5)
    assert tree.max() == 10
    tree.add(10)
    assert tree.max() == 10
    tree.add(11)
    assert tree.max() == 11
    tree.add(12)
    tree.add(13)
    tree.add(-1)
    assert tree.max() == 13

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
    testCompare = Node(7)
    testCompare.right = Node(9)
    assert tree.head.value == 6
    assert tree.head.left == None
    assert tree.head.right == testCompare
    assert tree.head.right.right.value==9
    assert tree.head.right.right.right.value==10
    assert tree.head.right.right.right.right.value==(11) # test remove head with left and right children

    tree.add(3)
    tree.add(5)
    tree.add(2)
    tree.add(4)
    assert tree.head.left.value == 3
    assert tree.head.left.right.value == 5
    assert tree.head.left.left.value == 2
    assert tree.head.left.right.left.value == 4
    
    tree.remove(3) # remove depth 1 left child with left and right children
    assert tree.head.left.value == 5 #test remove left child with left and right children
    assert tree.head.left.left.value == 4 #test remove left child with left and right children
    assert tree.head.left.left.left.value == 2 #test remove left child with left and right children

    tree.remove(10)
    assert tree.head.right.right.right.value==11 # test remove right child with only right child

    tree.add(10)
    tree.add(15)
    tree.remove(11)
    assert tree.head.right.right.right.value==10 # test remove  right child with left and right children
    assert tree.head.right.right.right.right.value==15 # remove  right child with left and right children
    newTree = BinaryTree()
    newTree.add(10)
    newTree.add(5)
    newTree.add(7)
    newTree.add(6)
    newTree.remove(5)

    assert newTree.head.left.value==7 # test remove left child with right child
    assert newTree.head.left.left.value==6


    newTree.add(15)
    newTree.add(12)
    newTree.add(13)
    newTree.remove(15)
    assert newTree.head.right.value==12 # test remove right child with left child
    assert newTree.head.right.right.value==13

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