#Word is a palindrome if it has at no more than one letter that has odd count
def Palindrome(string:str):
    from collections import Counter
    count = Counter(string)
    count_odd = sum(1 for letter, cnt in count.items() if cnt % 2)
    return count_odd <= 1

print(Palindrome('civic'))
print(Palindrome('ivicc'))
print(Palindrome('civil'))
print(Palindrome('livci'))