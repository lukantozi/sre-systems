class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        rows,cols= len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or i==rows or j<0 or j==cols or  grid[i][j]==0:
                return 0
            
            grid[i][j]=0
            return 1+dfs(i-1,j)+ dfs(i+1,j) + dfs(i,j-1)+dfs(i,j+1)
            
        a=0

        for x in range (rows):
            for y in range (cols):
                a=max(a,dfs(x,y))

        return a
