
class Node:

    def __init__(self, value, next=None):
        """
        This is the Node Constractor
        Arguments: value (value that the node represents) and next (optional param that defults to none and represents the next node in the list).
        """
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, head = None):
        """
        This is the constractor for the actual linked List.
        Arguments : head (optional param that defaults to none and represents the head of the Linked List)
        """
        self.head = head

    def insert(self,value):
        """
        Insert value to the head
        Argument: value (value that the new node represents)
        """
        node = Node(value)

        if self.head is not None:
            node.next = self.head ## (self.head) The old one

        self.head = node ## (self.head) the new one

    def includes(self,value):
        """
        Search the linkes List for a specific value.
        Arguments : value (value we are searching for in the list).
        Output: A boolean (true of false).
        """

        current = self.head

        while current :
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self,value):
        """
        Appends value to end of linked list
        Arguments: value (value we trying to append).
        """
        node  = Node(value)
        current = self.head
        if self.head == None:
            self.head = node
            return

        while current.next is not None:
            current = current.next

        current.next =node

    def insert_before(self,value, newValue):
        """
        Insert value before specified value
        Arguments: value and newValue (we traying to insert newValue before value (if exists) )
        """

        if self.head.value == value:
            self.insert(newValue)
            return

        current =self.head
        while current is not None:
            print(current.value)
            if current.next.value == value:
                print('yes')
                node = Node(newValue)
                node.next = current.next
                current.next = node
                return
            current = current.next

    def insert_Aftre(self,value, newValue):
        """
        Insert value after specified value
        Arguments: value and newValue (we traying to insert newValue after value (if exists) )
        """

        current = self.head
        while current is not None:
            if current.value == value:
                node = Node(newValue)
                node.next = current.next
                current.next = node
                return
            current = current.next

    def kthFromEnd(self,k):
        self.k=k
        arr = []
        current =self.head
        while current is not None:
            arr += [current.value]
            current =current.next

        if 0 <= k <len(arr):

            kValue =arr[len(arr)-1-k]
            return kValue

        raise Exception(f"Length of The list is {len(arr)-1} Please Enter index between [0-{len(arr)-1}]")


    def __str__(self):
        """
        Produce a string representation of the linked list.
        Output: String representation of the linked list.
        """

        current = self.head
        string = ''

        while current is not None:
            string += f"{{{current.value}}}->"
            current = current.next

        return string + 'None'

if __name__=="__main__":
    ll = LinkedList()
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    ll.append('value044')
    #ll.insert_before('value022','value077s')
    print(ll.kthFromEnd(4))
    print(ll)
