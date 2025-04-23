class Solution:
    def isBalanced(self, root) -> bool:
        balanced, height = self.check_balance(root)
        return balanced

    def check_balance(self, root):
        if not root:
            return True, 0
        left_balanced, left_height = self.check_balance(root.left)
        right_balanced, right_height = self.check_balance(root.right)
        balanced = ((left_balanced and right_balanced) and abs(left_height - right_height)<=1)
        height = max(left_height+1, right_height+1)
        return balanced, height