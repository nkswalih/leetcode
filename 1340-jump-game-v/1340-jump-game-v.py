class Solution:

    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        memo = [-1] * n

        def dp(i: int) -> int:
            if memo[i] != -1:
                return memo[i]

            max_visited = 1

            # Jump Right (i + x)
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_visited = max(max_visited, 1 + dp(j))

            # Jump Left (i - x)
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break  # Blocked by a taller or equal bar
                max_visited = max(max_visited, 1 + dp(j))

            memo[i] = max_visited
            return max_visited

        # Try starting from every possible index and find the maximum
        return max(dp(i) for i in range(n))
