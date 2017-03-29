# Script to practice linked list implementation and function to reverse

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        print self.head.data
        temp = self.head.next
        while (temp != None):
	    print temp.data
	    temp = temp.next

    def reverse(self):
        prev = self.head
        self.head = self.head.next
        prev.next = None
        while (self.head.next is not None):
            nxt = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = nxt
        self.head.next = prev

llist = LinkedList()
for x in xrange(11):
    llist.add_node(x**2)
print 'Current list order:'
llist.print_list()
llist.reverse()
print 'Reversed list:'
llist.print_list()
# Just to show a change
