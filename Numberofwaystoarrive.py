import heapq
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MOD=10**9+7
        graph=defaultdict(list)
        for u,v,price in roads:
            graph[u].append((v,price))
            graph[v].append((u,price))

        dist=[float('inf')]*n
        dist[0]=0
        ways=[0]*n
        ways[0]=1

        heap=[(0,0)]

        while heap:
            p,v=heapq.heappop(heap)
            for nei,pri in graph[v]:
                cost=pri+p
                if cost<dist[nei]:
                    dist[nei]=cost
                    ways[nei]=ways[v]
                    heapq.heappush(heap,(cost,nei))
                elif cost==dist[nei]:
                    ways[nei]=(ways[nei]+ways[v])%MOD

        return ways[n-1]
                                     
