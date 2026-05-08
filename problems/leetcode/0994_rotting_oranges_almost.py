class Solution:
    def orangesRotting(self, grid: list[list[int]]): # -> int
        H, W = len(grid), len(grid[0])
        visited = [[False]*W for _ in range(H)]
        q = [(0,0)]
        visited[0][0] = True
        res = []
        minutes = 0

        def four_dir(r,c):
            nbrs = []
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            for dir in dirs:
                dir_r, dir_c = dir
                new_r, new_c = r+dir_r, c+dir_c
                if new_r >= 0 and new_r < H and new_c >= 0 and new_c < W:
                    nbrs.append((new_r, new_c))
                    if grid[r][c] == 2:
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
            return nbrs

        while len(q) > 0:
            curr = q.pop(0)
            r,c = curr
            res.append(curr)

            neighbours = four_dir(r,c)
            for orange in neighbours:
                r,c = orange
                if not visited[r][c]:
                    visited[r][c] = True
                    q.append((r,c))
            minutes += 1

        return grid, res


oranges_1 = [[2,1,1],
             [1,1,0],
             [0,1,1]]
oranges_2 = [[2,1,1],
             [0,1,1],
             [1,0,1]]
oranges_3 = [[0,2]]
oranges_4 = [[1, 0, 2],
             [1, 1, 1],
             [1, 1, 1]]
#print(Solution().orangesRotting(oranges_1))
#print(Solution().orangesRotting(oranges_2))
#print(Solution().orangesRotting(oranges_3))
print(Solution().orangesRotting(oranges_4))


# solved 
class Solution:
    def orangesRotting_solved(self, grid: list[list[int]]): # -> int
        H, W = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(H):
            for c in range(W):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1

        return minutes if fresh == 0 else -1
