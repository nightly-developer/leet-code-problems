'''A linked list is a data structure that can easily grow or shrink. In linked list we have nodes where each node has a value and is pointing to nex node. there are three types of nodes 1)head node 2)in between nodes 3)tail node we store the address of head node this head node is pointing to first in-between node. The second last node of linked list is pointing to tail node. Tail node has a value and is pointing to Null
to create a linked list will first create a class `Node` which will generate nodes 
each node will point to next node by `self.next`
tail node will point to None
'''

class Node:
    #constructor to create node and assigning next value
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

#class to create LinkedList
class LinkedList:
    #constructor to create head of linked list
    def __init__(self) -> None:
        self.head = Node(None)

    #adding apend method
    def append(self,value):
        if self.head.val is None:
            self.head.val = value
        else:
            new_node = Node(value)
            if self.head.next is None:
              self.head.next = new_node
            else:
                current_node = self.head
                while current_node.next is not None:
                  current_node = current_node.next
                current_node.next = new_node
    
    def traverse(self):
        current_node = self.head
        print(current_node.val)
        while current_node.next is not None:
          current_node = current_node.next
          print(current_node.val)


list1 = LinkedList()
list1.append(9)
list1.append(10)
list1.append(11)
list1.append(12)

list1.traverse()