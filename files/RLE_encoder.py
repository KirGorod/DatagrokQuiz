from itertools import groupby
def rle(s: str):
    return "".join(f"{x}{sum(1 for _ in y)}" for x, y in groupby(s))

print(rle('ABBA'))
print(rle('ATTTGC'))