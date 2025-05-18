from functools import lru_cache

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        valid_columns = []

        # Step 1: Generate all valid column combinations
        def generate_columns(current: str):
            """
            Use DFS to generate all valid vertical colorings (column-wise),
            ensuring no two adjacent cells have the same color.
            """
            if len(current) == m:
                valid_columns.append(current)
                return
            
            for color in "123":
                # Ensure the current color is different from the one above
                if current and current[-1] == color:
                    continue
                generate_columns(current + color)
        
        generate_columns("")

        # Step 2: Dynamic Programming with memoization
        @lru_cache(None)
        def dp(col_index: int, prev_col: str) -> int:
            """
            Count ways to color from col_index to the last column,
            given that the previous column's coloring is 'prev_col'.
            """
            if col_index == n:
                # Base case: successfully colored all columns
                return 1

            total_ways = 0

            # Try all valid column configurations
            for curr_col in valid_columns:
                # Check compatibility with the previous column
                for row in range(m):
                    if curr_col[row] == prev_col[row]:
                        break  # Same color in the same row as previous column — not allowed
                else:
                    # Valid transition
                    total_ways += dp(col_index + 1, curr_col)
            
            return total_ways

        # Start with an imaginary column filled with '0's (non-conflicting placeholder)
        return dp(0, '0' * m) % MOD
