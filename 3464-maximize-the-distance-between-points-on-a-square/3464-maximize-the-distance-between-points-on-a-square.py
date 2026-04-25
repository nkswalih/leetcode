from bisect import bisect_left

class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(points)
        unrolled = []

        # 1. Map 2D boundary coordinates to a 1D perimeter line
        for x, y in points:
            if x == 0:
                u_dist = y                     # Left edge
            elif y == side:
                u_dist = side + x              # Top edge
            elif x == side:
                u_dist = 3 * side - y          # Right edge
            else:
                u_dist = 4 * side - x          # Bottom edge
            unrolled.append((u_dist, x, y))

        # 2. Sort points based on perimeter traversal
        unrolled.sort()
        u_vals = [pt[0] for pt in unrolled]

        # 3. Helper to find the next valid point >= d Manhattan distance away
        def find_next(current_idx, d):
            curr_u, curr_x, curr_y = unrolled[current_idx]
            
            # The next point must be at least d units away in the unrolled 1D line
            target_u = curr_u + d
            idx = bisect_left(u_vals, target_u)
            
            # Line of sight across edges might violate actual Manhattan distance,
            # so we verify via coordinates before accepting.
            while idx < n:
                dist = abs(unrolled[idx][1] - curr_x) + abs(unrolled[idx][2] - curr_y)
                if dist >= d:
                    return idx
                idx += 1
            return -1

        # 4. Feasibility check for a given distance d
        def is_possible(d):
            # Since k <= 25, we can check all feasible starting anchors
            for i in range(n):
                count = 1
                current_idx = i
                
                # Greedily search for the remaining k - 1 points
                for _ in range(k - 1):
                    next_idx = find_next(current_idx, d)
                    if next_idx == -1:
                        count = 0
                        break
                    current_idx = next_idx
                    count += 1
                
                # Verify that k points were selected and the loop completes properly
                if count == k:
                    dist_to_start = abs(unrolled[current_idx][1] - unrolled[i][1]) + \
                                    abs(unrolled[current_idx][2] - unrolled[i][2])
                    if dist_to_start >= d:
                        return True
            return False

        # 5. Binary Search on the answer
        low, high = 1, side
        ans = 1

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                ans = mid
                low = mid + 1 # Attempt to increase the valid minimum distance
            else:
                high = mid - 1
                
        return ans
