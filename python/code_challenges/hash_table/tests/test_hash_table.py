from hash_table import __version__
from hash_table.hash import HashTable, repeated_word, left_join_hash
import pytest

def test_version() :
    assert __version__ == '0.1.0'

def test_key_value() :
    table = HashTable()
    table.add('Wrekat', 100)
    assert table.contains('Wrekat') == True

def test_in_range () :
    table = HashTable()
    assert table.hash('Wrekat') == 622

def test_add_item() :
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert len(hash_table.arr[hash_table.hash('hello')]) == 1

def test_get() :
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert hash_table.get('hello') == 15

def test_contains() :
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert hash_table.contains('hello')

def test_delete() :
  hash_table = HashTable()
  hash_table.add('hello',15)
  hash_table.delete('hello')
  assert len(hash_table.arr[hash_table.hash('hello')]) == 0

# Test Function First Repeated (Challenge 31) :

def test_first_repeated () :
    assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
    assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == "it"
    assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == "summer"

def test_no_repeated () :
    assert repeated_word("My Name Is Mohammad Alwrekat") == "Nothing Repeate !!!"

# Test Function Hash Map Left Join (Challenge 33) :

def test_hashmap_left_join(data) :
    expected = [['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['flow', None, 'jam']]
    assert (left_join_hash(data[0],data[1])) == expected

## DATA

@pytest.fixture
def data() :
    hash_one = HashTable()
    hash_one.add("fond", "enamored")
    hash_one.add("wrath", "anger")
    hash_one.add("diligent", "employed")
    hash_one.add("outfit", "garb")
    hash_one.add("guide", "usher")
    hash_two = HashTable()
    hash_two.add("fond", "averse")
    hash_two.add("wrath", "delight")
    hash_two.add("diligent", "idle")
    hash_two.add("guide", "follow")
    hash_two.add("flow", "jam")

    return[hash_one,hash_two]
