from stack_queue.stackQueue import Stack
from stack_queue.stackQueue import view

class PseudoQueue :

    def __init__(self) :
        self.stackOne = Stack()
        self.stackTwo = Stack()

    def StackEnqueue(self,value) :
        self.stackOne.push(value)
        if self.stackOne.top.value :
            return self.stackOne.top.value
        else :
            return("Its Empty")

    def StackDequeue(self) :
        currunt = self.stackOne.top
        while currunt != None:
            self.stackTwo.push(currunt.value)
            self.stackOne.pop()
            currunt = self.stackOne.top

        self.stackTwo.pop()
        return self.stackTwo.top

stackEQ = PseudoQueue()
flow = "Mhmad -> 25 -> Al-Wrekat"

if __name__ =="__main__":

    view()
    print("First Stack enQueue : " , stackEQ.StackEnqueue("Mhmad"))
    print("Second Stack enQueue : " , stackEQ.StackEnqueue(25))
    print("Last Stack enQueue : " , stackEQ.StackEnqueue("Al-Wrekat"))
    view()
    print(flow)
    view()
    print("First Stack Are Removed (deQueue)\nThe Next Value : " , stackEQ.StackDequeue())
    print("Second Stack Are Removed (deQueue)\nThe Next Value : " , stackEQ.StackDequeue())
    print("Last Stack Are Removed (deQueue)\nThe Next Value : " , stackEQ.StackDequeue())
    view()
