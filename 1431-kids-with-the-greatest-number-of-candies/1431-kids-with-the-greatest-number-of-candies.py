class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        return [kid_candies + extraCandies >= max_candies for kid_candies in candies]