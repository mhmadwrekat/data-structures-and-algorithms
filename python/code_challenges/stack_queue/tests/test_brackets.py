# # Delete Line (2) And Delete Line (20) To Test .
"""
from stack_queue.brackets import *
# Test.1
def test_true():
  assert validateBrackets("{[]{()}}") == True
  assert validateBrackets("{}{}[](())") == True
# Test.2
def test_false():
  assert validateBrackets("[({}]") == False
  assert validateBrackets("{(})") == False
# Test.3
def test_true_with_word():
  assert validateBrackets("()Mhmad[[Wrekat]]") == True
  assert validateBrackets("{My}{Age}[Is]((25))") == True
# Test.4
def test_false_with_word():
  assert validateBrackets("{My}{Age}[Is]((25)") == False
  assert validateBrackets("(Mhmad[[Wrekat]") == False
"""
