from stack_queue.stackQueue import *
open = ["(", "[", "{"]
close = [")", "]", "}"]

def validateBrackets(value):
    arr = []
    for i in value:
        if i in open:
            arr.append(i)
        elif i in close:
            result = close.index(i)
            if ((len(arr) > 0) and (open[result] == arr[len(arr)-1])):
                arr.pop()
            else:
                return False
    if len(arr) == 0:
        return True
    else:
        return False

if __name__ =="__main__":
    view()
    print("{} -> " , validateBrackets("{}"))
    print("{}(){} -> " , validateBrackets("{}(){}"))
    print("()[[Extra Characters]] -> " , validateBrackets("()[[Extra Characters]]"))
    print("(){}[[]] -> " , validateBrackets("(){}[[]]"))
    print("{}{Code}[Fellows](()) -> " , validateBrackets("{}{Code}[Fellows](())"))
    view()
    print("[({}] -> " , validateBrackets("[({}]"))
    print("(]( -> " , validateBrackets("(]("))
    print("{(}) -> " , validateBrackets("{(})"))
    view()
