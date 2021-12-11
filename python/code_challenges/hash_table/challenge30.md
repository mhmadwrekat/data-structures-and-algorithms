## Hash Table

---
## Challenge

create a functional hashtable that can add, get, search and hash the value into it .

- **Hash :** Turn the key into an index to indicate where to add it in the hash table
- **Get :** Search for the key in the hash table and returns the value paired to it else returns 'NULL'
- **Contain :** Search for the key in the hash table and returns boolean
- **Insert :** Add a key,value pair to The hash table .

---
## API

***Time :***

- Hash : O(1)
- Get : O(n)
- Contain : O(n)
- Insert : O(n)


***Space :***

- Hash : O(1)
- Get : O(1)
- Contain : O(1)
- Insert : O(n)


> ***[The Code .....](/python/code_challenges/hash_table/hash_table/hash.py)***

> ***[The Tests .....](/python/code_challenges/hash_table/tests/test_hash_table.py)***

---
## Check List

- [x] Branch Name : hashtable .
- [x] create a Node that holds key, pair values .
- [x] create the hashing method in the hash table .
- [x] create a get method to get the key value in the hash table .
- [x] create a contain method to check for the existance of the key in the hash table .
- [x] create add method to insert key,value into the hash table .
- [x] Test adding a key/value to your hashtable results in the value being in the data structure .
- [x] Teat retrieving based on a key returns the value stored .
- [x] Test successfully returns null for a key that does not exist in the hash table .
- [x] Test successfully handle a collision within the hash table .
- [x] Test successfully retrieve a value from a bucket within the hashtable that has a collision .
- [x] Test successfully hash a key to an in-range value .

