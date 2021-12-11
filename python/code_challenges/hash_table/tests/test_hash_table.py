from hash_table import __version__
from hash_table.hash import Hashtable

def test_version() :
    assert __version__ == '0.1.0'

def test_key_value() :
    table = Hashtable()
    table.add('Wrekat', 100)
    assert table.contain('Wrekat') == True

def test_retrieve() :
    table = Hashtable()
    table.add('Wrekat', 100)
    assert table.get('Wrekat') == 100

def test_return_null() :
    table = Hashtable()
    table.add('Wrekat',100)
    assert table.get('Mhmad') == 'NULL'

def test_handle_collision () :
    table = Hashtable()
    table.add('Wrekat',100)
    table.add('takerW',50)
    assert table.contain('takerW') == True
    assert table.contain('Wrekat') == True

def test_retrieve_bucket () :
    table = Hashtable()
    table.add('Wrekat',100)
    table.add('takerW',50)
    assert table.get('takerW') == 50
    assert table.get('Wrekat') == 100

def test_in_range () :
    table = Hashtable()
    assert table.hash('Wrekat') == 554
