import re
class HashTable :
  def __init__(self, size = 1024) :
    self.max = size
    self.arr = [[] for i in range(self.max)]

  def hash(self, key) :
    hash = 0
    for char in key :
        hash += ord(char)
    hash_index= hash % self.max
    return hash_index

  def add(self, key, value) :
    hash = self.hash(key)
    found = False
    for idx, element in enumerate(self.arr[hash]) :
      if len(element)==2 and element[0] == key :
          self.arr[hash][idx] = (key,value)
          found = True
    if not found :
      self.arr[hash].append((key,value))

  def get(self, key) :
    hash = self.hash(key)
    for element in self.arr[hash] :
      if element[0] == key :
        return element[1]

  def contains(self, key) :
    hash = self.hash(key)
    found = False
    for idx, element in enumerate(self.arr[hash]) :
      if len(element)==2 and element[0] == key :
        found = True
    return found

  def delete(self , key) :
    hash = self.hash(key)
    for idx , element in enumerate(self.arr[hash]) :
      if element[0] == key :
        del self.arr[hash][idx]

## Challenge 31 -> REPEATED WORD :

def repeated_word(str) :
  if str == "" :
    return 'Empty String'
  strs = re.sub(r'[^\w\s]','',str).lower().split(' ')
  hash_table = HashTable()
  for i in strs :
    if hash_table.contains(i) :
      return i
    else :
      hash_table.add(i, 1)
  return 'Nothing Repeate !!!'
