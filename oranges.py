from collections import deque

def minimumTimeToRotOranges(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    fresh_oranges = 0
    rotten_queue = deque()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh_oranges += 1
            elif grid[i][j] == 2:
                rotten_queue.append((i, j, 0))  

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

    time_to_rot = 0
    while rotten_queue:
        row, col, time = rotten_queue.popleft()
        time_to_rot = max(time_to_rot, time)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                grid[new_row][new_col] = 2
                rotten_queue.append((new_row, new_col, time + 1))
                fresh_oranges -= 1

    return time_to_rot if fresh_oranges == 0 else -1


N, M = map(int, input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

result = minimumTimeToRotOranges(grid)
print(result)
