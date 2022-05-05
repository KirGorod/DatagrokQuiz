def FindDuplicate(l:list):
    from collections import Counter
    my_list = []
    for key, value in Counter(l).items():
        if value >= 2:
            my_list.append(key)
    return my_list

l = [1,2,2,3]
print(FindDuplicate(l))
