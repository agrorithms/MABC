from typing import Optional, Union, Tuple

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

    def add(self,toAdd: Union[int,Node]) -> None:
        if not isinstance(toAdd,Node):
            toAdd = Node(toAdd)
        if not self.head:
            self.head = toAdd
            return

        curr: Node = self.head

        while curr:
            if toAdd.value > curr.value:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right=toAdd
                    return
            elif toAdd.value < curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left=toAdd
                    return
            else:
                return
           
    def min(self, start: Optional[Node] = None) -> Node:
        if not self.head:
            return None

        if start:
            curr: Node = start
        else:
            curr: Node = self.head

        while curr:
            if curr.left:
                curr=curr.left
            else:
                return curr
    
    def max(self,start: Optional[Node] = None) -> Node:
        if not self.head:
            return None

        if start:
            curr: Node = start
        else:
            curr: Node = self.head

        while curr:
            if curr.right:
                curr=curr.right
            else:
                return curr

    
    def contains(self, value: int) -> bool:
        return bool(self._findNode(value))
    
    def remove(self, value: int) -> None:
        prev, curr = self._findNode(value)
        new=None
        if curr.left:
            new=self.max(curr.left)
            self.remove(new.value)
            new.left=curr.left
            new.right=curr.right
            
        elif curr.right:
            new=self.min(curr.right)
            self.remove(new.value)
            new.left=curr.left
            new.right=curr.right
            
        if not prev:
            self.head = new or None
        elif prev.value<curr.value:
            prev.right = new or None
        else:
            prev.left = new or None
        

        

    
    
    def remove2(self, value: int) -> None:
        prev, curr = self._findNode(value)
        head=False
        if not curr:
            return
        if not prev:
            prev=curr
            head=True
        

        if prev.value<=curr.value:
            if curr.left:
                toAdd=curr.right
                if head:
                    self.head=curr.left
                else:
                    prev.right = curr.left
                if toAdd:
                    self.add(toAdd)
                    return
            elif head:
                self.head = curr.right
            else:
                prev.right = curr.right
                return
        else:

            if curr.right:
                toAdd=curr.left
                prev.left = curr.right
                if toAdd:
                    self.add(toAdd)
                    return
            else:
                prev.left = curr.left
                return
            
    def _findNode(self,value: int) -> Optional[Tuple[Optional['Node'], 'Node']]:
        if not self.head:
            return None
        
        prev: Optional[Node] = None
        curr: Node = self.head
        while curr:
            if value > curr.value:
                prev=curr
                curr = curr.right
            elif value < curr.value:
                prev=curr
                curr = curr.left
            else:
                return prev , curr
        return None
    
    def maxDepth(self, start: Optional[Node] = None ) -> int:
        if not self.head:
            return None
        curr = start or self.head
        seen: set = set()
        nodeStack: list = [curr]
        depth: int = 0
        maxdepth=depth
        
        while nodeStack:
            if curr.left and curr.left.value not in seen:
                nodeStack.append(curr)
                curr=curr.left
                seen.add(curr.value)
                
                depth+=1
            elif curr.right and curr.right.value not in seen:
                nodeStack.append(curr)
                curr=curr.right
                seen.add(curr.value)
                depth+=1
            else:
                curr=nodeStack.pop()
                depth-=1
            maxdepth = depth if depth>maxdepth else maxdepth
        return maxdepth
            

    def __repr__(self):
        return dict(head=self.head).__repr__()