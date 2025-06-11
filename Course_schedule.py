from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)     
            in_degree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        completed = 0
        while queue:
            current = queue.popleft()
            completed += 1
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses
