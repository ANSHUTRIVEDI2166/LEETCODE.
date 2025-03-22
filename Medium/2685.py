from typing import List
from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        
        def dfs(node):
            stack = [node]
            vertices = 0
            edges = 0
            while stack:
                curr = stack.pop()
                if not visited[curr]:
                    visited[curr] = True
                    vertices += 1
                    edges += len(graph[curr])
                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            return vertices, edges
        
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                v_count, e_count = dfs(i)
                if e_count == v_count * (v_count - 1):
                    complete_components += 1
        
        return complete_components
