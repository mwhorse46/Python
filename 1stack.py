class Stack:
     
    def __init__(self):
        self.stack = list()
        self.maxSize = 8
        self.top = 0
    
    def push(self,data):
        if self.top>=self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True
        
    def pop(self):
        if self.top<=0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
        
    def size(self):
        return self.top

    def merge(a,b):
        ans = []
        while(len(a)>0):
            ans.append(a.pop())
        while(len(b)>0):
            ans.append(b.pop())
        return(ans)
a = [3,4]
b = [1,2]  
m = merge(a,b)
for k in m:
    print(k)

s = Stack()
print(s.push(1))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.push(6))
print(s.push(7))
print(s.push(8))
print(s.push(9))
print(s.size())        
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
