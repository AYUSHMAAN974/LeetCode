from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows=len(mat)
        cols=len(mat[0])
        vis = [[False for _ in range(cols)] for _ in range(rows)] 
        dist = [[0 for _ in range(cols)] for _ in range(rows)] 
        queue=deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    queue.append((i,j,0))
                    vis[i][j]=True

        while queue:
            x,y,z=queue.popleft()
            dist[x][y] = z
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = x + dx, y + dy
                if 0 <= nr < rows and 0 <= nc < cols and not vis[nr][nc]:
                    vis[nr][nc] = True
                    queue.append((nr, nc, z + 1))  
        return dist


        
