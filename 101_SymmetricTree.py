class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)

    def isMirror(self, left_root, right_root):
        if not left_root and not right_root:
            return True
        if not left_root or not right_root:
            return False
        if (left_root.val == right_root.val) and self.isMirror(left_root.left,right_root.right) and self.isMirror(left_root.right, right_root.left):
            return True
        return False