class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, summation = stack.pop()
            if node.left:
                stack.append((node.left, summation + node.left.val))
            if node.right:
                stack.append((node.right, summation + node.right.val))
            if not node.left and not node.right:
                if summation == targetSum:
                    return True
        return False