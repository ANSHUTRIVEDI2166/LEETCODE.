from functools import lru_cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        @lru_cache(None)
        def dfs(position: int, is_limited: int):
            if len(temp_string) < num_length:
                return 0
            if len(temp_string) - position == num_length:
                return int(s <= temp_string[position:]) if is_limited else 1
            upper_limit = min(int(temp_string[position]) if is_limited else 9, limit)
            counter = 0
            for i in range(upper_limit + 1):
                counter += dfs(position + 1, is_limited and i == int(temp_string[position]))
            return counter

        num_length = len(s)
        temp_string = str(start - 1)
        count_start = dfs(0, True)
        dfs.cache_clear()
        temp_string = str(finish)
        count_finish = dfs(0, True)
        return count_finish - count_start
