from node import Node

#Doubly Linked List class (DLL)
class DLL:
    def __init__(self):
        """
        initialize dummy nodes for head and tail.  this way, edge case handling won't be needed for insert/delete
        and we get:
        most recent = head.next 
        least recent = tail.prev
        """
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def add_to_front(self, node):
        if not node:
            return

        temp = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node 

    

    def remove_from_tail(self):
        # self.tail is dummy the last value is at self.tail.prev 
        tail = self.tail.prev 

        tail.prev.next = self.tail 
        self.tail.prev = tail.prev
        return tail    # will be needed to delete the key from hashmap

        
    def remove_node(self, node):
        if not node:
            return 
        node.prev.next = node.next 
        node.next.prev = node.prev 