import heapq
from collections import defaultdict
from typing import List

MOD = int(1e9 + 7)

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]  
        heapq.heapify(pq)
        
        while pq:
            d, node = heapq.heappop(pq)
            
            if d > dist[node]:
                continue
            
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_dist, neighbor))
                elif new_dist == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n - 1]
