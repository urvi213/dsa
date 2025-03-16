items = [12,14,25,34,36,45,47,68]
find = int(input("what integer are you searching for? "))
found = False


# method 1 - iteration
lower = 0
upper = len(items)-1
while lower <= upper:
    middle =(lower+upper)//2
    if find == items[middle]:
        found = True
        print("item found at",middle)
        break
    elif find > items[middle]:
        lower = middle+1
    else:
        upper = middle-1

if not found: 
    print("item not found")