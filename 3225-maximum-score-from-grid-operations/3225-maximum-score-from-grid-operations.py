class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        # 1. Precompute prefix sums for each column
        # S[col][h] is the sum of the first h elements in column col
        S = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                S[j][i + 1] = S[j][i] + grid[i][j]

        # dp[h_curr][h_prev] stores the max score for current column height 
        # and previous column height.
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # 2. Iterate through columns from 1 to n-1
        for i in range(1, n):
            new_dp = [[0] * (n + 1) for _ in range(n + 1)]
            
            # Precompute prefix/suffix maxes for the previous DP state
            # prevSuffixMax[h_prev][j] = max(dp[h_prev][k] for k in range(j, n+1))
            prevSuffixMax = [[0] * (n + 1) for _ in range(n + 1)]
            # prevMax[h_prev][j] = max(dp[h_prev][k] - max(0, S[i-1][k] - S[i-1][h_prev]))
            prevMax = [[0] * (n + 1) for _ in range(n + 1)]

            for h_p in range(n + 1):
                # Suffix Max calculation
                cur_max = -1
                for k in range(n, -1, -1):
                    cur_max = max(cur_max, dp[h_p][k])
                    prevSuffixMax[h_p][k] = cur_max
                
                # Prefix Max calculation (avoiding double counting)
                cur_max_prefix = -1
                for k in range(n + 1):
                    # contribution already covered by column i-2 (k)
                    already_covered = max(0, S[i-1][k] - S[i-1][h_p])
                    cur_max_prefix = max(cur_max_prefix, dp[h_p][k] - already_covered)
                    prevMax[h_p][k] = cur_max_prefix

            # 3. Perform Transitions
            for h_curr in range(n + 1):
                for h_prev in range(n + 1):
                    if h_curr <= h_prev:
                        # Situation 1: Decreasing or equal
                        new_dp[h_curr][h_prev] = prevSuffixMax[h_prev][0] + S[i][h_prev] - S[i][h_curr]
                    else:
                        # Situation 2: Increasing
                        # Max of Case 3 (Inherit) and Case 1/2 (New contribution)
                        case_3 = prevSuffixMax[h_prev][h_curr]
                        case_1_2 = prevMax[h_prev][h_curr] + S[i-1][h_curr] - S[i-1][h_prev]
                        new_dp[h_curr][h_prev] = max(case_3, case_1_2)
            
            dp = new_dp

        # 4. Find the overall maximum score from the last column state
        ans = 0
        for h_curr in range(n + 1):
            for h_prev in range(n + 1):
                ans = max(ans, dp[h_curr][h_prev])
                
        return ans
