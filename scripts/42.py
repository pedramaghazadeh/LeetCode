class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        
        max_l[0] = height[0]
        max_r[-1] = height[-1]
        for i in range(1, len(height)):
            max_l[i] = max(max_l[i - 1], height[i])
            max_r[-i - 1] = max(max_r[-i], height[-i - 1])
        
        ans = 0
        for i in range(1, len(height) - 1):
            ans += max(min(max_l[i - 1], max_r[i + 1]) - height[i], 0)
        return ans