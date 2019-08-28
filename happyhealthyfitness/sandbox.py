def firstDuplicate(a):
    # initialize the duplicate index at -1
    # check nth number against the current smallest index
    # if a duplicate record the index
    index = len(a)
    for i, first_num in enumerate(a):
        for j, second_num in enumerate(a[i+1:index]):
            if first_num == second_num and j < index:
                index = j
                
    return index
            

print(firstDuplicate([5, 1, 1, 5, 3, 2]))