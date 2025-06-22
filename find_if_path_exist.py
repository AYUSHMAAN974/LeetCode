from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        vis = [False] * n
        queue = deque()
        queue.append(source)
        vis[source] = True

        while queue:
            x = queue.popleft()
            if x == destination:
                return True
            for y in adj_list[x]:
                if not vis[y]:
                    vis[y] = True
                    queue.append(y)

        return False   
