class Queue:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items ==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def getList(self):
        return self.items


q=Queue()
q.enqueue("Bayu")
q.enqueue("Reski")
q.enqueue("Awan")
print(q.getList())