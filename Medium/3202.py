class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r = [num % k for num in nums]
        l = [[] for _ in range(k)]
        for i, x in enumerate(r):
            l[x].append(i)
        
        m = max(len(lst) for lst in l) if k > 0 else 0
        
        if k == 0 or k == 1:
            return m
        
        for x in range(k):
            for y in range(x + 1, k):
                a = l[x]
                b = l[y]
                la = len(a)
                lb = len(b)
                if la == 0 and lb == 0:
                    continue
                i = j = 0
                sx = sy = 0
                while i < la or j < lb:
                    if j == lb or (i < la and a[i] < b[j]):
                        nx = 1
                        if sy > 0:
                            nx = sy + 1
                        if nx > sx:
                            sx = nx
                        i += 1
                    else:
                        ny = 1
                        if sx > 0:
                            ny = sx + 1
                        if ny > sy:
                            sy = ny
                        j += 1
                c = max(sx, sy)
                if c > m:
                    m = c
        return m
