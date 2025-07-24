from collections import defaultdict
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        m = len(edges)
        children = defaultdict(set)
        xor = [0]*len(nums)
        G = defaultdict(list)
        for v, w in edges:
            G[v].append(w)
            G[w].append(v)
        visited = set()
        def dfs(v):
            visited.add(v)
            curxor = nums[v]
            children[v].add(v)
            for w in G[v]:
                if w not in visited:
                    curxor ^= dfs(w)
                    children[v] |= children[w]
            xor[v] = curxor
            return xor[v]
        root = 0
        dfs(root)
        res = float('inf')
        for i in range(m - 1):
            for j in range(i + 1, m):
                a, b = edges[i]
                if b in children[a]:
                    a, b = b, a
                c,d = edges[j]
                if d in children[c]:
                    c, d = d, c
                if c in children[a]:
                    cur = [xor[c], xor[a]^xor[c], xor[root]^xor[a]]
                elif a in children[c]:
                    cur = [xor[a], xor[c]^xor[a], xor[root]^xor[c]]
                else:
                    cur = [xor[a], xor[c], xor[root]^xor[a]^xor[c]]
                res = min(res, max(cur) - min(cur))
        return res
