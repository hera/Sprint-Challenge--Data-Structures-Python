class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.index = 0
    
    def __str__(self):
        return str(self.storage)

    def get(self):
        return self.storage
    
    def append(self, value):
        if self.index >= self.capacity:
            self.index = 0
        
        if len(self.storage) < self.capacity:
            self.storage.append(value)
        else:
            self.storage[self.index] = value

        self.index += 1
