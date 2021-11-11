
def view():
    print('\n|------------------------------------------|')
############## NODE ###############
class Node :
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f'{self.value}'
############## STACK ###############
class EmptyStack(Exception) :
    pass

class Stack :
    def __init__(self) :
        self.top = None

    def push(self,value) :
        node = Node(value)
        if self.top :
            node.next = self.top
        self.top = node

    def pop(self) :
        try :
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except EmptyStack :
            raise EmptyStack('Its Empty')

    def stackEmpty(self) :
        return self.top == None

    def stackPeek(self):
        if not self.top:
            raise Exception('Its Empty')
        else:
            return self.top
############## QUEUE ###############
class EmptyQueue(Exception) :
    pass

class Queue :
    def __init__(self) :
        self.front = None
        self.rear = None

    def enqueue(self,value) :
        node = Node(value)
        if not self.rear :
            self.front = node
            self.rear = node
        else :
            self.rear.next = node
            self.rear = node

    def dequeue(self) :
        try :
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return self.front
        except EmptyQueue :
            raise EmptyQueue('Its Empty')

    def queueEmpty(self) :
        return self.front == None
    # Other Way :  return self.rear == None

    def queuePeek(self):
        if not self.front:
            raise Exception("Its Empty")
        else:
            return self.front

if __name__ =="__main__":
    view()
    view()
