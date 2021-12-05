def view() :
    print('\n-------------------------------------------------')

def insert_sort(data) :
    for i in range(1, len(data)) :
        j = i - 1
        sort = data[i]
        while j >= 0 and sort < data[j] :
            data[j + 1] = data[j]
            j = j - 1
        data[j+1] = sort
    return data

arr_one= [8, 4, 23, 42, 16, 15]
arr_two = [20, 18, 12, 8, 5, -2]
arr_three = [5, 12, 7, 5, 5, 7]
arr_four = [2, 3, 5, 7, 13, 11]

if __name__=="__main__" :
    view()
    print("[8, 4, 23, 42, 16, 15] -> ", insert_sort(arr_one))
    view()
    print("[20 ,18 ,12 ,8 , 5, -2] -> ", insert_sort(arr_two))
    view()
    print("[5, 12, 7, 5, 5, 7] -> ", insert_sort(arr_three))
    view()
    print("[2, 3, 5, 7, 13, 11] -> ", insert_sort(arr_four))
    view()
