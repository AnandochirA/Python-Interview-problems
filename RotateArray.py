from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = []
        k = k % len(nums)
        for i in range(len(nums) - k, len(nums)):
            arr.append(nums[i])
        for i in range(0, len(nums) - k):
            arr.append(nums[i])
        nums[:] = arr

# Test the solution
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
expected_output = [5, 6, 7, 1, 2, 3, 4]

solution = Solution()
solution.rotate(nums, k)

print("Output:", nums)
print("Expected Output:", expected_output)
print("Test Passes:", nums == expected_output)
