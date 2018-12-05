class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = Node

class Pilha:
    #pilha vazia
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #inserir valor na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        #retira o dado da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.dado
        raise IndexError("A pilha está vazia")

    def peek(self):
        #verifica o topo
        if self._size > 0:
            return self.top.dado
        raise IndexError("Pilha ainda está vazia")

    def __len__(self):
        #tamanho da pilha
        return self._size

    def __repr__(self):
        r =""
        pointer = self.top
        while(pointer):
            r = r+str(pointer.dado)+"\n"
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
