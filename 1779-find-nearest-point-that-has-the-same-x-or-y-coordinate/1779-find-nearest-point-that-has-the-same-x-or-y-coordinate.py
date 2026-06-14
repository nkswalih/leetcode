class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        min_distance = float('inf')
        best_index = -1
        
        for i, (px, py) in enumerate(points):
            # Check if the point is valid (shares X or Y coordinate)
            if x == px or y == py:
                # Calculate Manhattan distance
                distance = abs(x - px) + abs(y - py)
                
                # Keep the point with the strictly smallest distance
                if distance < min_distance:
                    min_distance = distance
                    best_index = i
                    
        return best_index
