class Solution(object):
    def numIslands(self, grid):
        grid_height = len(grid)
        grid_width = len(grid[0])
        visited = [[False]*grid_width for _ in range(grid_height)]

        def dfs(r,c):
            if r < 0 or r >= grid_height or c < 0 or c >= grid_width:
                return
            if grid[r][c] != "1" or visited[r][c]:
                return
            visited[r][c] = True

            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r+1,c)

        islands = 0
        for r in range(grid_height):
            for c in range(grid_height):
                if grid[r][c] == "1" and not visited[r][c]:
                    islands += 1
                    dfs(r,c)

        return islands


        
grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] # -> [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 3), (2, 0), (2, 1)]
grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] # -> [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (3, 3), (3, 4)]
solution = Solution()
print(solution.numIslands(grid_1)) # -> 1
print(solution.numIslands(grid_2)) # -> 3
