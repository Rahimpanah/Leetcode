class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        return self.BST(nums)

    def BST (self, array):
        if not array:
            return None
        length = len (array)
        middle = length // 2
        root = TreeNode(array[middle])
        root.left = self.BST(array[:middle])
        root.right = self.BST(array[middle+1:])
        return root