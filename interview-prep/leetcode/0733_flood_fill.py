class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        H, W = len(image), len(image[0])
        s_color = image[sr][sc]
        if s_color == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= H or c < 0 or c >= W:
                return
            if image[r][c] != s_color:
                return

            image[r][c] = color 

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        dfs(sr,sc)

        return image


print(Solution().floodFill([[1,1,1], [1,1,0], [1,0,1]], 1, 1, 2))
print(Solution().floodFill([[0,0,0], [0,0,0], [0,0,0]], 0, 0, 0))
