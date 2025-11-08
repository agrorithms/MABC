from typing import Optional, Union

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

    
    def contains(self, value: int) -> None:
        if not self.head:
            return False
        
        curr: Node = self.head
        while curr:
            if value > curr.value:
                curr = curr.right
            elif value < curr.value:
                curr = curr.left
            else:
                return True
        return False
    
    def remove(self, value: int) -> None:
        if not self.head:
            return
        
        curr: Node = self.head
        prev: Optional[Node] = None
        while curr:
            if value > curr.value:
                prev = curr
                curr = curr.right
            elif value < curr.value:
                prev = curr
                curr = curr.left
            else:
                break
        if not curr:
            return
        print(self, curr == self.head)
        print(f'remove {value}', curr)
        if curr == self.head:
            if self.head.left:
                toAdd=self.head.right
                self.head = self.head.left
                if toAdd:
                    self.add(toAdd)
                return
            else:
                self.head = self.head.right
                return
        
        if prev.value<curr.value:
            if curr.left:
                toAdd=curr.right
                prev.right = curr.left
                if toAdd:
                    self.add(toAdd)
                    return
            else:
                prev.right = curr.right
                return
        else:
            print(f'prev: {prev}' )
            if curr.right:
                toAdd=curr.left
                prev.left = curr.right
                if toAdd:
                    self.add(toAdd)
                    return
            else:
                prev.left = curr.left
                print(f'prev: {prev}')
                return
            

        """
        nodeStack: list[Node] = [curr]
        if curr == self.head:
            if curr.left and curr.right:
                
                while curr:
                    if curr.left:
                        curr=curr.left
                        nodeStack.append(curr)
                    else:
                        break
                while len(nodeStack)>1:
                    nodeStack.pop().left = nodeStack[-1].left

            elif curr.right:
                self.head = curr.right
            elif curr.left:
                self.head = curr.left
            else:
                self.head = None
            return    
                

        if curr.value<prev.value:
            prev.left = curr.left
            while curr:
                if curr.left:
                    curr=curr.left
                    nodeStack.append(curr)
                else:
                    break
            while len(nodeStack)>1:
                nodeStack.pop().left = nodeStack[-1].left
            return
        elif curr.value>prev.value:
            prev.value = curr.right
            while curr:
                if curr.right:
                    curr=curr.right
                    nodeStack.append(curr)
                else:
                    break
            while len(nodeStack)>1:
                nodeStack.pop().right = nodeStack[-1].right
            return
        """

    def __repr__(self):
        return dict(head=self.head).__repr__()
    
