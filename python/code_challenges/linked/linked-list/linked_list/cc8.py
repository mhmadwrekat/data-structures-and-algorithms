def view():
    print('\n|------------------------------------------|')

class Node :
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f'{self.value}'

class LinkedList :
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else :
            current = self.head
            while current.next != None :
                current = current.next
            current.next = node

    def __str__(self):
        output = 'head -> '
        if self.head is None :
            output += None
        else :
            current = self.head
            while(current):
                output += f'{current.value} -> '
                current = current.next
            output += 'None'
            return output

    def zipLists(self, listOne , listTwo):
        finalList = LinkedList()
        currentOne = listOne.head
        currentTwo = listTwo.head
        while currentOne and currentTwo :
            finalList.append(currentOne)
            finalList.append(currentTwo)
            currentOne = currentOne.next
            currentTwo = currentTwo.next
        while currentOne :
            finalList.append(currentOne)
            currentOne = currentOne.next
        while currentTwo :
            finalList.append(currentTwo)
            currentTwo = currentTwo.next

        return finalList


listOne = LinkedList()
listOne.append(1)
listOne.append(3)
listOne.append(2)
listTwo = LinkedList()
listTwo.append(5)
listTwo.append(9)
listTwo.append(4)

if __name__ =="__main__":
    ll = LinkedList()
    view()
    print('\nList One :')
    print(listOne)

    print('\nList Two :')
    print(listTwo)

    print('\nFinal List :')
    print(ll.zipLists(listOne,listTwo))
    view()
