array1 = [2,7,12,18,5,6,20,22]
num_list = [12,56,23,45,34,54,67,89,56]

def merge(array,lower,middle,upper):
    i = lower
    j = middle+1
    merged_result = []
    while i <= middle and j <= upper:
        if array[i] < array [j]:
            merged_result.append(array[i])
            i += 1
        else:
            merged_result.append(array[j])
            j+=1
    while i <= middle:
        merged_result.append(array[i])
        i += 1
    while j <= upper:
        merged_result.append(array[j])
        j += 1

    k=0
    for i in range(lower,upper+1):
        array[i] = merged_result[k]
        k+=1


def merge_sort(array,lower,upper):
    if lower<upper:
        middle = (lower+upper)//2
        merge_sort(array,lower,middle)
        merge_sort(array,middle+1,upper)
        merge(array,lower,middle,upper)
        print(num_list)


merge_sort(num_list,0,8)

