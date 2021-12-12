from hash_table import __version__
from hash_table.hash import HashTable, repeated_word

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

# Test Function First Repeated :

def test_first_repeated () :
    assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
    assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == "it"
    assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == "summer"

def test_no_repeated () :
    assert repeated_word("My Name Is Mohammad Alwrekat") == "Nothing Repeate !!!"
