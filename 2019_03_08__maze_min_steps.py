'''
March 8, 2019

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you
can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the
minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down,
and right. You cannot move through walls. You cannot wrap around the edges of
the board.

For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum
number of steps required to reach the end is 7, since we would need to go
through (1, 2) because there is a wall everywhere else on the second row.
'''

# Classic dijkstra's algorithm
# Now how does that algorithm go again...
def get_min_steps(maze, start, end):
    # return null if no solution exists
    no_solution = None

    # maze[row][col] = True iff there is a wall there
    if maze[start[0]][start[1]] or maze[end[0]][end[1]]:
        return no_solution

    nodes = {
        (row, col): float('inf') for row in range(len(maze))
        for col in range(len(maze[0])) if not maze[row][col]
    }

    # it takes 0 moves to get to the starting position
    nodes[tuple(start)] = 0
    while nodes:
        this_key = min(nodes.keys(), key=nodes.get)
        this_dist = nodes.pop(this_key)
        if this_key == tuple(end):
            return this_dist

        for diff in zip((-1, 1, 0, 0), (0, 0, -1, 1)):
            neighbor = (this_key[0] + diff[0], this_key[1] + diff[1])
            # Only valid moves are contained in the nodes dict
            if neighbor in nodes:
                nodes[neighbor] = this_dist + 1

    return no_solution

if __name__ == '__main__':
    import sys
    start, end = ([int(x) for x in y.split(',')] for y in sys.argv[1:3])
    print('start: {}'.format(start))
    print('end: {}'.format(end))
    print('maze:')
    maze = []
    for row in sys.argv[3:]:
        row = [True if x == 't' else False for x in row.split(',')]
        print(row)
        maze.append(row)

    result = get_min_steps(maze, start, end)
    print('min steps to solve: {}'.format(result))
