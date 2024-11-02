
# Brute force
#  Time & Space Complexity
# Time complexity: O(n square)

# Space complexity: O(1)


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res


