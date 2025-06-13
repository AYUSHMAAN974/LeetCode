from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        safe=[]
        ele=len(graph)
        out_deg=[0]*ele
        in_deg=[[] for _ in range(ele)]
        for i in range(ele):
            for j in graph[i]:
                in_deg[j].append(i)
            
        for i in range(ele):
            for j in in_deg[i]:
                out_deg[j]+=1
        
        queue=deque()
        for i in range(ele):
            if out_deg[i]==0:
                queue.append(i)

        while queue:
            x=queue.popleft()
            safe.append(x)
            for i in in_deg[x]:
                out_deg[i]-=1
                if out_deg[i]==0:
                    queue.append(i)

        safe.sort()
        return safe

        
