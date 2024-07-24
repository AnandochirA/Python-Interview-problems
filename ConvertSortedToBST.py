class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        sz = len(nums)
        if sz == 0:
            return None
        
        middle = sz // 2
        root = TreeNode(nums[middle])
        left = []
        right = []
        
        for i in range (0, middle):
            left.append(nums[i])
        for i in range (middle + 1, len(nums)):
            right.append(nums[i])
            
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        
        return root