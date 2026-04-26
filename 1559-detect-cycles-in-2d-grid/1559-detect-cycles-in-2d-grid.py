class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(r, c, pr, pc):
            visited[r][c] = True
            
            # 4 directional moves: up, down, left, right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and matching character value
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == grid[r][c]:
                    # Skip the cell we just came from
                    if nr == pr and nc == pc:
                        continue
                    
                    # If already visited and not the parent, cycle found!
                    if visited[nr][nc]:
                        return True
                    
                    # Recurse for the next cell
                    if dfs(nr, nc, r, c):
                        return True
                        
            return False

        # Check every cell in the grid
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    # Start DFS with dummy parent (-1, -1)
                    if dfs(i, j, -1, -1):
                        return True
                        
        return False
