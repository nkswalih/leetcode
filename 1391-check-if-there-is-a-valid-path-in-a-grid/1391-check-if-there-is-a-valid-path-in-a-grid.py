from collections import deque

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # Directions: Up: (-1, 0), Down: (1, 0), Left: (0, -1), Right: (0, 1)
        # Map each street to its relative connection coordinates
        directions = {
            1: [(0, -1), (0, 1)],  # Left, Right
            2: [(-1, 0), (1, 0)],  # Up, Down
            3: [(0, -1), (1, 0)],  # Left, Down
            4: [(0, 1), (1, 0)],   # Right, Down
            5: [(0, -1), (-1, 0)], # Left, Up
            6: [(0, 1), (-1, 0)]   # Right, Up
        }
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return True
                
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and if the neighbor is already visited
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    # Check if the neighboring street connects back to the current cell
                    # For a valid path, the opposite direction (-dr, -dc) must be in the neighbor's allowed directions
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False
