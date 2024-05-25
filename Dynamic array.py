class Arrays:
    def __init__(self, capacity:int = 2):
        self.__capacity = capacity
        self.__size = 0
        self.__data = [None] * capacity

    def __getitem__(self, index:int):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        return self.__data[index]
    
    def __setitem__(self, index:int, value):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        self.__data[index] = value

    def __len__(self):
        return self.__size

    def __resize__(self):
        new_data = [None] * (self.__capacity * 2) 
        for i in range(self.__size):
            new_data[i] = self.__data[i]
        self.__data = new_data  
        self.__capacity *= 2

    def append(self, value):
        if self.__size == self.__capacity:
            self.__resize__()
        self.__data[self.__size] = value
        self.__size += 1

    def insertAtIndex(self, index, value):
        if index < 0 or index > self.__size:
            raise IndexError("Index out of range")
        if self.__size == self.__capacity:
            self.__resize__()
        for i in range(self.__size, index, -1):
            self.__data[i] = self.__data[i - 1]
        self.__data[index] = value
        self.__size += 1
    
    def removeValue(self, value):
        for i in range(self.__size):
            if self.__data[i] == value:
                for j in range(i, self.__size - 1):
                    self.__data[j] = self.__data[j + 1]
                self.__data[self.__size - 1] = None
                self.__size -= 1
                return
    
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")
        for i in range(index, self.__size - 1):
            self.__data[i] = self.__data[i + 1]
        self.__data[self.__size - 1] = None
        self.__size -= 1

    def IsEmpty(self):
        return self.__size == 0
    
    def rotate_right(self, k):
        if self.__size == 0:
            return
        k = k % self.__size
        self.__data = self.__data[-k:] + self.__data[:-k]

    def Reverse(self):
        left, right = 0, self.__size - 1
        while left < right:
            self.__data[left], self.__data[right] = self.__data[right], self.__data[left]
            left += 1
            right -= 1

    def Prepend(self, value):
        self.insertAtIndex(0, value)

    def MergeTwoArrays(self, arr2):
        for i in range(arr2.__size):
            self.append(arr2[i])
    
    def interleave(self, other):
        result = Arrays()
        i, j = 0, 0
        while i < self.__size and j < other.__size:
            result.append(self.__data[i])
            result.append(other.__data[j])
            i += 1
            j += 1
        while i < self.__size:
            result.append(self.__data[i])
            i += 1
        while j < other.__size:
            result.append(other.__data[j])
            j += 1
        return result
    
    def MiddleElement(self):
        if self.__size == 0:
            return None
        return self.__data[self.__size // 2]
        
    def IndexOf(self, value):
        for i in range(self.__size):
            if self.__data[i] == value:
                return i
        return -1
    
    def ResizeBy(self, value):
        if value < 1:
            raise ValueError("Resize factor must be greater than or equal to 1")
        new_data = [None] * (self.__capacity * value)
        for i in range(self.__size):
            new_data[i] = self.__data[i]
        self.__data = new_data
        self.__capacity *= value
    
    def split(self, index):
        if index < 0 or index > self.__size:
            raise IndexError("Index exceeds the limit")
        left = Arrays()
        right = Arrays()
        for i in range(index):
            left.append(self.__data[i])
        for i in range(index, self.__size):
            right.append(self.__data[i])
        return left, right

    def __str__(self):
        return str(self.__data[:self.__size])


# Creating an array
array = Arrays(5)

# Appending elements to the array
array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)

# Splitting the array at index 3
left, right = array.split(3)
print("Left array:", left)   # Output: Left array: [1, 2, 3]
print("Right array:", right) # Output: Right array: [4, 5]

# Removing an element
array.removeValue(2)

# Checking the length of the array
print(len(array))  # Output: 4 (after removing, it should be 4)

# Inserting an element at index 1
array.insertAtIndex(1, 15)

# Accessing elements by index
print(array[0])  # Output: 1
print(array[1])  # Output: 15

# Checking the length of the array
print(len(array))  # Output: 5 (after insertion, it should be 5)

# Deleting an element at index 0
array.deleteAtIndex(0)

# Checking the length of the array
print(len(array))  # Output: 4 (after deletion, it should be 4)
