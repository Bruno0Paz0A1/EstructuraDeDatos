class Stack:
    def __init__(self):
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop()
 
    def top(self):
        return self.items[len(self.items)-1]
 
    def size(self):
        return len(self.items)
        
s = Stack()
print (s.isEmpty())
s.push(100)
s.push(200)
s.pop()
s.size()