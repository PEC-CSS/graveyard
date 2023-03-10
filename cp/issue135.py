class Solution:
    def longestConsequtive(self, nums: list[int]) -> int:
        s = set(nums)
        count = 0
        ans = 0
        for num in nums:
            current_element = num
            previous_element = current_element - 1
            if previous_element not in s:
                while current_element in s:
                    current_element += 1
                    count += 1
                ans = max(ans, count)
                count = 0
        return ans

s = Solution()
nums = list(map(int, input().split()))
print(s.longestConsequtive(nums))