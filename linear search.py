# looking at every item starting from the first
items = [1,2,3,4,5,6,7,8,9,0]
find = int(input("which digit do you want to find? "))
found = False # flag variable - yes or no

for i in range(len(items)):
    if items[i] == find:
        print("item found at",i)
        found = True
        break
if not found: print("not found")