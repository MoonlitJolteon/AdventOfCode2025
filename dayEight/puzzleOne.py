from collections import Counter

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
        self.parent[self.find(x)] = self.find(y)


uf = UnionFind(n)
for dist, i, j in pairs[:1000]:
    uf.union(i, j)

sizes = sorted(Counter(uf.find(i) for i in range(n)).values(), reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
