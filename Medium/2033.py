class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:   
        flat_grid = [num for row in grid for num in row]
        flat_grid.sort()

        remainder = flat_grid[0] % x
        for num in flat_grid:
            if num % x != remainder:
                return -1

        median = flat_grid[len(flat_grid) // 2]
        return sum(abs(num - median) // x for num in flat_grid)



        
