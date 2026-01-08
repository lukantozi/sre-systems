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
            if r < 0 or r >= H or c < 0 or c > W:
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
