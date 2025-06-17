import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows=len(heights)
        cols=len(heights[0])
        start=0
        new_h=[[float("inf")]*cols for _ in range(rows)]
        new_h[0][0]=start

        heap=[(0,0,0)]
        while heap:
            effort,a,b=heappop(heap)
            if a==rows-1 and b==cols-1:
                return effort
            
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc=a+dr,b+dc
                if 0<=nr<rows and 0<=nc<cols:
                    next_effort=max(effort,abs(heights[nr][nc]-heights[a][b]))

                    if next_effort<new_h[nr][nc]:
                        new_h[nr][nc]=next_effort
                        heappush(heap,(next_effort,nr,nc))

        return -1
        
