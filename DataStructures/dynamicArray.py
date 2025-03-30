import ctypes

class DynamicArray:
    
    def __init__(self):
        """
        set initial max capacity and initial amt of elements
        """
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        return current amt of items
        """
        return self.n

    def __getitem__(self, k):
        """
        get element in array at index k
        """
        if not 0 <= k <= self.n:
            return IndexError("Index out of range")

        return self.A[k]

    def append(self, element):
        """
        add element at the end of current list
        if current amt of items = current capacity then add room
        to new items
        """
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        self.A[self.n] = element
        self.n += 1

    def _resize(self, capacity):
        """
        do resize. Double current array size
        """
        B = self.make_array(capacity)

        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = capacity

    def make_array(self, new_capacity):
        """
        create a new array for new capacity
        """
        return (new_capacity * ctypes.py_object)()
