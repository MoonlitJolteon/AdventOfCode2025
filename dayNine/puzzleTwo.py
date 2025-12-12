# with open("exampleinput.txt") as rawInput:
with open("input.txt") as rawInput:
    redTiles = [tuple(map(int, line.split(","))) for line in rawInput]

redTilesSet = set(redTiles)


def is_point_in_polygon(x, y, polygon):
    inside = False
    p1x, p1y = polygon[0]
    for i in range(1, len(polygon) + 1):
        p2x, p2y = polygon[i % len(polygon)]
        if min(p1y, p2y) < y <= max(p1y, p2y) and x <= max(p1x, p2x) and p1y != p2y:
            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
                inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def is_on_polygon_edge(x, y, polygon):
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        if (
            min(x1, x2) <= x <= max(x1, x2)
            and min(y1, y2) <= y <= max(y1, y2)
            and (y2 - y1) * (x - x1) == (y - y1) * (x2 - x1)
        ):
            return True
    return False


def segments_intersect(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ccw = lambda ax, ay, bx, by, cx, cy: (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    d1, d2 = ccw(bx1, by1, bx2, by2, ax1, ay1), ccw(bx1, by1, bx2, by2, ax2, ay2)
    d3, d4 = ccw(ax1, ay1, ax2, ay2, bx1, by1), ccw(ax1, ay1, ax2, ay2, bx2, by2)
    return (d1 * d2 < 0) and (d3 * d4 < 0)


def is_valid_rectangle(x1, y1, x2, y2):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]

    for x, y in corners:
        if (x, y) not in redTilesSet:
            if not is_point_in_polygon(x, y, redTiles) and not is_on_polygon_edge(
                x, y, redTiles
            ):
                return False

    rect_edges = [
        (min_x, min_y, max_x, min_y),
        (max_x, min_y, max_x, max_y),
        (max_x, max_y, min_x, max_y),
        (min_x, max_y, min_x, min_y),
    ]

    for i in range(len(redTiles)):
        px1, py1 = redTiles[i]
        px2, py2 = redTiles[(i + 1) % len(redTiles)]
        for rx1, ry1, rx2, ry2 in rect_edges:
            if segments_intersect(rx1, ry1, rx2, ry2, px1, py1, px2, py2):
                return False
    return True


candidates = [
    (
        (abs(redTiles[i][0] - redTiles[j][0]) + 1)
        * (abs(redTiles[i][1] - redTiles[j][1]) + 1),
        i,
        j,
        redTiles[i][0],
        redTiles[i][1],
        redTiles[j][0],
        redTiles[j][1],
    )
    for i in range(len(redTiles))
    for j in range(i + 1, len(redTiles))
]

candidates.sort(reverse=True)

max_area = 0
for area, i, j, x1, y1, x2, y2 in candidates:
    if area <= max_area:
        break
    if is_valid_rectangle(x1, y1, x2, y2):
        max_area = area

print(max_area)
