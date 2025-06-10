class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        def dfs(node,c):
            color[node]=c
            for neighbour in graph[node]:
                if color[neighbour]==-1:
                    if not dfs(neighbor, 1 - c):
                        return False
                elif color[neighbor] == c:
                    return False
            return True

                


        rows=len(graph)
        color=[-1]*rows
        for i in range(rows):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
