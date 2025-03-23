list1 = [2,6,2,8,4,9,4,6,23,14,2]

def insertion_sort(list):
    for i in range(len(list)):
        key = list[i]
        prev = i-1
        while key < list[prev] and prev >= 0:
            list[prev+1] = list[prev]
            prev -= 1
        list[prev+1] = key
        print(list)
        
insertion_sort(list1)