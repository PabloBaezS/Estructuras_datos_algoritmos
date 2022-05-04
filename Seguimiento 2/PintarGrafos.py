from collections import deque

from numpy import char

row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# check if it is possible to go to pixel (x, y) from the
# current pixel. The function returns false if the pixel
# has a different color, or it's not a valid pixel
def esPosibleIrAPixel(mat, x, y, objetivo):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == objetivo


# Flood fill using BFS
def cambioColor(mat, x, y, reemplazo):
    # base case
    if not mat or not len(mat):
        return

    # create a queue and enqueue starting pixel
    q = deque()
    q.append((x, y))

    # get the target color
    objetivo = mat[x][y]

    # target color is same as replacement
    if objetivo == reemplazo:
        return

    # break when the queue becomes empty
    while q:

        # dequeue front node and process it
        x, y = q.popleft()

        # replace the current pixel color with that of replacement
        mat[x][y] = reemplazo

        # process all eight adjacent pixels of the current pixel and
        # enqueue each valid pixel
        for k in range(len(row)):
            # if the adjacent pixel at position (x + row[k], y + col[k]) is
            # is valid and has the same color as the current pixel
            if esPosibleIrAPixel(mat, x + row[k], y + col[k], objetivo):
                # enqueue adjacent pixel
                q.append((x + row[k], y + col[k]))


def main():
    coordenadas = list(map(int, input().split(" ")))
    colores = list(map(char, input().split(" ")))
    tamañoM = list(map(int, input().split(" ")))
    a = []
    for i in range(0, n):
        a.append([int(j) for j in input().split()])


cambioColor(a, coordenadas[0], coordenadas[1], replacement)

main()