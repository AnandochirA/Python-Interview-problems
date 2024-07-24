from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def in_order_traversal(self, node: Optional[TreeNode], arr: list) -> list:
        if node is not None:
            self.in_order_traversal(node.left, arr)
            arr.append(node.val)
            self.in_order_traversal(node.right, arr)
        return arr
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        
        self.in_order_traversal(root, arr)
        for i in range (1, len(arr)):
            if(arr[i - 1] >= arr[i]):
                return False
        return True