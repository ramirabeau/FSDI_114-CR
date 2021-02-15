#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DLNode(Node):
    def __init__(self, data):
        self.prev
        super().__init__(data)

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add(self, data, prev_node=None, position=None):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return True

        if prev_node:
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            return True
                
        if position:
            last = self.find_index(index=position)
            if last == self.head:
                last.next = self.head
                self.head = last
                return True
            return self.add(data, prev_node=last)
        
        last = self.find_index()
        last.next = new_node
        return True

    def remove(self, target_data):
        if self.head.data == target_data:
            self.head = self.head.next
            return True
        
        last = self.head
        while last:
            current = last.next
            if current.data == target_data:
                last.next = current.next
            
                return True
            last = last.next
        return False

        temp = self.head

        if temp is not None:
            if (temp.data == data):
                self.head = temp.next
                return True
            
            while (temp is not None):
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next

            if (temp == None):
                return "Data was not found, nothing was removed."

            prev.next = temp.next

            return True
        return "There is no data at the head of the list, nothing was removed."
    
    def find_index(self, index=None):
        last = self.head
        counter = 0
        while (last.next):
            last = last.next
            
            if counter == index:
                break
            counter += 1
        return last

class DLList:
    def __init__(self)
        self.head = None
    
    def find_tail():
        last = self.head
        while last.next:
            last = last.next
        return last

    def add(self, data):
        if not self.head:
            self.head = DLNode(data)
            return True

        tail = self.find_tail()

        new_node = DLNode(data)
        tail.next = new_mode
        new_node.prev = tail
        return True

    def insert_after(self, prev_node, data, new_data):
        """This method inserts data after the prev_node
            prev pointer has to point to its previous node
            and its next pointer has to point to the next node
            in the list
        """
        if prev_node is None:
            return ("This node is not present.")
       
        new_node = Node(data = new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        
        return True





