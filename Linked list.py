class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.data = data

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0
    
    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
        else:
            trav = self.__head
            while trav.next is not None:
                trav = trav.next
            trav.next = newNode
        self.__size += 1
    
    def __str__(self):
        l = []
        trav = self.__head
        while trav is not None:
            l.append(str(trav.data))
            trav = trav.next
        return '--->'.join(l)
    
    def addFirst(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
        else:
            newNode.next = self.__head
            self.__head = newNode
        self.__size += 1

    def addAt(self, data, index):
        if index < 0 or index > self.size():
            raise Exception("Index out of bound")
        elif index == 0:
            self.addFirst(data)
        elif index == self.__size:
            self.append(data)
        else:
            i = 0
            trav = self.__head
            while i != index - 1:
                i += 1
                trav = trav.next
            newNode = Node(data)
            newNode.next = trav.next
            trav.next = newNode
            self.__size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List Empty")
        else:
            temp = self.__head
            self.__head = temp.next
            del temp
        self.__size -= 1

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List Empty")
        elif self.__size == 1:
            self.removeFirst()
        else:
            trav = self.__head
            while trav.next.next is not None:
                trav = trav.next
            temp = trav.next
            trav.next = None
            del temp
            self.__size -= 1

    def getHead(self):
        return self.__head
    
    def removeAt(self, index):
        if index < 0 or index >= self.size():
            raise Exception("Index out of bound")
        elif index == 0:
            self.removeFirst()
        elif index == self.__size - 1:
            self.removeLast()
        else:
            i = 0
            trav = self.__head
            while i != index - 1:
                i += 1
                
# Create a linked list
ll = LinkedList()

# Append elements to the linked list
ll.append(10)
ll.append(20)
ll.append(30)

# Print the linked list
print("Initial list:", ll) # output : Initial list: 10--->20--->30

# Add elements at the beginning and a specific position
ll.addFirst(5)
ll.addAt(25, 3)

# Print the modified linked list
print("Modified list:", ll)  # output : Modified list: 5--->10--->20--->25--->30

# Remove elements from the linked list
ll.removeFirst()
ll.removeLast()
ll.removeAt(1)

# Print the linked list after removals
print("List after removals:", ll)   # output : List after removals: 10--->25

# Search for an element
index = ll.search(20)
print("Element 20 found at index:", index) # output : Element 20 found at index: -1

# Get the middle element
mid = ll.mid()
print("Middle element:", mid) # output : Middle element: 25

# Reverse the linked list
ll.reverse() 

# Print the reversed linked list
print("Reversed list:", ll) # output : Reversed list: 25--->10
