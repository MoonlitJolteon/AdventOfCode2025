# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    boxes = [tuple(map(int, line.split(","))) for line in rawInput]


def distance(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5


n = len(boxes)
pairs = sorted(
    (distance(boxes[i], boxes[j]), i, j) for i in range(n) for j in range(i + 1, n)
)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py
            return True
        return False


uf = UnionFind(n)
for dist, i, j in pairs:
    if uf.union(i, j) and len(set(uf.find(k) for k in range(n))) == 1:
        print(boxes[i][0] * boxes[j][0])
        break
