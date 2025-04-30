class Solution:
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSame(node,subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    
    def isSame(self, main, sub):
        if not main and not sub:
            return True
        if not main or not sub:
            return False
        result = main.val==sub.val and (self.isSame(main.left, sub.left)) and (self.isSame(main.right,sub.right))
        return result