from stack_queue.stackQueue import view , Node

class Dog() :
  def __init__(self) :
    self.type = 'dog'
  def __str__(self):
    return 'dog'

class Cat():
  def __init__(self) :
    self.type = 'cat'
  def __str__(self):
    return 'cat'

class AnimalShelter :
  def __init__(self) :
      self.front = None
      self.rear = None

  def animalEnqueue (self , value) :
    node = Node(value)
    if not self.rear :
      self.front = node
      self.rear = node
    else :
      self.rear.next = node
      self.rear = node
    return value.type

  def dequeue (self , pref) :
      temp = self.front
      self.front = self.front.next
      temp.next = None
      return self.rear

oscar = Dog()
dog2 = Dog()
cat1 = Cat()
cat2 = Cat()
test = AnimalShelter()
test.animalEnqueue(oscar)
test.animalEnqueue(cat1)
test.animalEnqueue(dog2)
test.animalEnqueue(cat2)

if __name__ == "__main__" :
    view()
    print('dog -> cat -> dog -> cat -> cat -> none')
    print ('1 -> ',test.front )
    print('2 -> ',test.front.next)
    print('3 -> ',test.front.next.next)
    print('4 -> ',test.front.next.next.next)
    print('5 -> ',test.rear)
    print('6 -> ',test.rear.next)
    view()
