class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(city):
            visited[city] = 1
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and visited[neighbor]==0:
                    dfs(neighbor)

        n = len(isConnected)
        visited = [0] * n
        count = 0

        for i in range(n):
            if visited[i]==0:
                dfs(i)
                count += 1

        return count

        
