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
    assert tree.head == None
    tree.add(7)
    assert tree.head == Node(7)
    tree.add(6)
    assert tree.head.value == 7
    head1 = Node(7)
    head1.left=Node(6)
    assert tree.head == head1
    tree.remove(7)
    assert tree.head == Node(6)
    tree.remove(6)
    assert tree.head == None
    tree.add(7)
    tree.add(8)
    tree.remove(7)
    assert tree.head == Node(8)
    tree.add(7)
    assert tree.head.value == 8
    assert tree.head.left.value == 7
    tree.add(6)
    assert tree.head.value == 8
    assert tree.head.left.value == 7
    assert tree.head.left == head1
    tree.remove(7)
    assert tree.head.value == 8
    assert tree.head.left == Node(6)
    
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

    tree.add(3)
    tree.add(5)
    tree.add(2)
    tree.add(4)
    assert tree.head.left.value == 3
    
