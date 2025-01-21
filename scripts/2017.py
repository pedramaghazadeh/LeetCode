class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sum_rows = [[grid[0][0]], [grid[1][0]]]
        
        for i in range(1, len(grid[0])):
            sum_rows[0].append(sum_rows[0][-1] + grid[0][i])
            sum_rows[1].append(sum_rows[1][-1] + grid[1][i])
        
        ans = min(sum_rows[0][-1] - grid[0][0], sum_rows[1][-1] - grid[1][-1])
        for i in range(1, len(grid[0])):
            ans = min(ans, max(sum_rows[0][-1] - sum_rows[0][i], sum_rows[1][i - 1]))

        return ans