class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        H, W = len(grid), len(grid[0])
        max_area = 0
        land_cord = []
        visited = [[False]*W for _ in range(H)]
        curr_land = [0]

        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    land_cord.append((r,c))


        def dfs(r,c):
            if r < 0 or r >= H or c < 0 or c >= W:
                return
            if grid[r][c] == 0 or visited[r][c]:
                return

            visited[r][c] = True
            curr_land[0] += 1

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r,c in land_cord:
            curr_land[0] = 0
            dfs(r,c)
            max_area = max(max_area, curr_land[0])

        return max_area


print(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,0,0,0,0,0,0,1,1,0,0,0,0]]))

# better
class Solution:
    def maxAreaOfIsland_better(self, grid: list[list[int]]) -> int:

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
