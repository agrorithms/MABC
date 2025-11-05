from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
    
    def __repr__(self) -> str:
        return dict(value = self.value, left=self.left.value if self.left else None,right=self.right.value if self.right else None).__repr__()
    
    def __eq__(self,other: 'Node') -> bool:  
        if not isinstance(other, Node):
            return False
        this: tuple = (self.value, self.left.value if self.left else None, self.right.value if self.right else None)
        that: tuple = (other.value, other.left.value if other.left else None, other.right.value if other.right else None)
        return this == that


        

class BinaryTree:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def add(self,value: int) -> None:
        
        if not self.head:
            self.head = Node(value)
            return

        curr: Node = self.head

        while curr:
            if value > curr.value:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right=Node(value)
                    return
            elif value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left=Node(value)
                    return
            else:
                return
           
    def min(self) -> int:
        if not self.head:
            return None

        curr: Node = self.head

        while curr:
            if curr.left:
                curr=curr.left
            else:
                return curr.value
    
    def max(self) -> int:
        if not self.head:
            return None

        curr: Node = self.head

        while curr:
            if curr.right:
                curr=curr.right
            else:
                return curr.value

    """
    def remove(self, value) -> None:
        if not self.head:
            return

        curr: Node = self.head

        while curr:
            if value > curr.value:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right=Node(value)
                    return
            elif value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left=Node(value)
                    return
            else:
                return
    """
        

    def __repr__(self):
        return dict(head=self.head).__repr__()
    
