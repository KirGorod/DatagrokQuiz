def intersectionCount(a:list, b:list):
    a = set(a)
    intersection = a.intersection(b)
    return intersection

a = [1,2,3,5]
b = [1,2,5]
print(intersectionCount(a, b))