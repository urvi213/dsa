to_sort = [1,4,2,7,4,5,3,9,8]
text_tosort = ["banana","cat","busker","eat","eden","mad","feel","play"]

def bubble_sort(list):
    for i in range(len(list)):
        swap = False
        print("pass",i)
        for x in range(len(list)-1):
            if list[x] > list[x+1]:
                swap = True
               # to_swap = list[x]
                #list[x] = list[x+1]
                #list[x+1] = to_swap
                list[x],list[x+1] = list[x+1],list[x]
                print(list)
        if swap == False:
            break
                

bubble_sort(to_sort)
print("")
bubble_sort(text_tosort)

#c , b = 23,24