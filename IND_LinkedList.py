#


class Node:

    def _init_(self, data, next = None):
        self.data = []
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None



    # insertion method for the linked list
    def insert(self, data):

        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
