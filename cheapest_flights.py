from collections import defaultdict, deque

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        queue = deque()
        queue.append((src, 0, 0))

        min_cost = [float('inf')] * n
        min_cost[src] = 0

        while queue:
            city, cost, stops = queue.popleft()

            if stops > k:
                continue
            
            for neighbor, price in graph[city]:
                new_cost = cost + price
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    queue.append((neighbor, new_cost, stops + 1))

        return min_cost[dst] if min_cost[dst] != float('inf') else -1
        
