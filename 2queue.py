class queue:
    def __init__(self):
        self.itmes = []

    def add(self,item):
        self.items.append(item)

    def delete(self):
        itemtodelete = self.items[0]
        del self.items[0]
        return itmetodelete

    def size(self):
        return len(self.items)



myqueue = queue()
myqueue.add("jaimin")
myqueue.add("ajay")
myqueue.add("yo")
myqueue.add("jalfjj")
print(myqueue.size())
print(myqueue.report())
print(myqueue.delete())
print(myqueue.report())
