class stack():
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0
    
    def peek(self):
        assert not self.isEmpty(), "Tidak dapat dipeek"
        return self.items[-1]
    
    def pop(self):
        assert not self.isEmpty(), "Tidak dapat dipop"
        return self.items.pop()
    
    def push(self, data):
        self.items.append(data)

object = stack()
object.push("Cerpelai")
object.push("Bebek")
object.push("Ayam")
print(object.items)
object.pop()
print(object.items)

class queue():
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian Kosong"
        return self.items.pop(0)

antrian = queue()
antrian.enqueue("Cerpelai")
antrian.enqueue("Bebek")
antrian.enqueue("Ayam")
print(antrian.items)
antrian.dequeue()
print(antrian.items)