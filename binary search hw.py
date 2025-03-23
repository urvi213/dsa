list1 = [23,34,35,45,48,67,78,789]
to_find1 = 35
to_find2 = 37


def binary_search(list,to_find,lower,upper):
    if lower <= upper:
        middle = (lower+upper)//2
        if to_find == list[middle]:
            print("{} found at {} in {}".format(to_find,middle,list))
        elif to_find > list[middle]:
            binary_search(list,to_find,middle+1,upper)
        else:
            binary_search(list,to_find,lower,middle-1)
    else:
        print("not in list")

binary_search(list1,to_find1,0,len(list1)-1)
binary_search(list1,to_find2,0,len(list1)-1)