# Delete Line (2) And Delete Line (41) To Test .
"""
from stack_queue.animal_shelter import Dog, Cat, AnimalShelter
import pytest
# Test.1
def test_animal_enqueue(data) :
    oscar = Dog()
    ketti = Dog()

    animal = AnimalShelter()
    assert animal.animalEnqueue(oscar) == animal.front.value.type
    assert animal.animalEnqueue(ketti) == animal.front.value.type
# Test.2
def test_animal_enqueue_multiple(data) :
    assert 'dog'  == data.front.value.type
    assert 'cat'  == data.rear.value.type
# Test.3
def test_animal_dequeue(data) :
    data.dequeue('dog')
    assert 'cat'  == data.rear.value.type
# Test.4
def test_animal_empty_after_dequeue(data) :
    data.dequeue('dog')
    data.dequeue('dog')
    data.dequeue('cat')
    data.dequeue('cat')
    assert data.front == None
@pytest.fixture
def data() :
    dog1 = Dog()
    dog2 = Dog()
    cat1 = Cat()
    cat2 = Cat()
    animal = AnimalShelter()
    animal.animalEnqueue(dog1)
    animal.animalEnqueue(cat1)
    animal.animalEnqueue(dog2)
    animal.animalEnqueue(cat2)
    return animal
##################################
"""
