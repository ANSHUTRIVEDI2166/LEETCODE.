class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        n = len(arr)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    count += 1
        return count
