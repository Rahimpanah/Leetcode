class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        answer , high = self.hight_of_tree(root)
        return answer
    
    def hight_of_tree(self, root):
        if not root:
            return 0, 0
        answer_left, h_left = self.hight_of_tree(root.left)
        answer_right, h_right = self.hight_of_tree(root.right)
        x = h_left + h_right
        return max(x, answer_left, answer_right), max(h_left,h_right) + 1