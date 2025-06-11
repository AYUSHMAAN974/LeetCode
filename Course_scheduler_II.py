from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj=[[] for _ in range(numCourses)]
        in_degree=[0]*numCourses
        final=[]

        for x,y in prerequisites:
            adj[y].append(x)
            in_degree[x]+=1
        queue=deque()
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        
        completed=0
        while queue:
            current=queue.popleft()
            final.append(current)
            completed+=1
            for nei in adj[current]:
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    queue.append(nei)
                  
        if completed==numCourses:
            return final
        else:
            return []
        
            
            
