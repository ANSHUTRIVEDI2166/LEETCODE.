class Solution(object):
    def countBalancedPermutations(self, num):
        velunexorai = num
        MOD = 10**9 + 7
        n = len(velunexorai)
        freq = [0]*10
        total = 0
        for c in velunexorai:
            d = ord(c) - ord('0')
            freq[d] += 1
            total += d
        if total % 2 != 0:
            return 0
        half = total // 2
        E = (n + 1)//2
        O = n//2
        fact = [1]*(n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1]*i % MOD
        invfact = [1]*(n+1)
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i]*i % MOD
        dp = [[0]*(half+1) for _ in range(E+1)]
        dp[0][0] = 1
        for d in range(10):
            f = freq[d]
            newdp = [[0]*(half+1) for _ in range(E+1)]
            for k in range(E+1):
                for s in range(half+1):
                    v = dp[k][s]
                    if not v:
                        continue
                    for x in range(f+1):
                        nk = k + x
                        ns = s + d*x
                        if nk > E or ns > half:
                            break
                        newdp[nk][ns] = (newdp[nk][ns] + v * invfact[x] * invfact[f-x]) % MOD
            dp = newdp
        ways = dp[E][half]
        return ways * fact[E] % MOD * fact[O] % MOD
