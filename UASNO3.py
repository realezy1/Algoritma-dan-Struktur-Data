class pohonBiner():
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

A = pohonBiner("Hewan")
B = pohonBiner("Mamalia")
C = pohonBiner("Reptil")
D = pohonBiner("Kucing")

A.kiri = B
A.kanan = C
B.kiri = D

def inOrder(subpohon):
    if subpohon is not None:
        inOrder(subpohon.kiri)
        print(subpohon.data)
        inOrder(subpohon.kanan)

def preOrder(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        preOrder(subpohon.kiri)
        preOrder(subpohon.kanan)

inOrder(A)
preOrder(A)