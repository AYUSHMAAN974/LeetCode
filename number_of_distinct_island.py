class Solution(object):
    def distinctIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        unique_shapes = set()

        def dfs(r, c, base_r, base_c, path):
            visited[r][c] = True
            path.append((r - base_r, c - base_c))

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc, base_r, base_c, path)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    path = []
                    dfs(i, j, i, j, path)
                    unique_shapes.add(tuple(path)) 

        return len(unique_shapes)
