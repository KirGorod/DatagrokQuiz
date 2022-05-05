class Rect(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def aoi(r1, r2):
    width = min(r1.x2, r2.x2) - max(r1.x1, r2.x1)
    height = min(r1.y2, r2.y2) - max(r1.y1, r2.y1)
    if min(width, height) > 0:
        return width * height
    else:
        return 0

r1 = Rect(1,2,4,6)
r2 = Rect(3,4,5,8)
print(aoi(r1, r2))
