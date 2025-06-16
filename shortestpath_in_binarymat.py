from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        queue = deque()
        queue.append((0, 0, 1))  

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        visited[0][0] = True

        while queue:
            r, c, dist = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return dist

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

        return -1  
