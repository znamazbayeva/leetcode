# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(l, r):
            if l == r:
                return [None]
            nodes = []
            for i in range(l, r):
                for lch in generate(l, i):
                    for rch in generate(i+1, r):
                        node = TreeNode(i+1)
                        node.left = lch
                        node.right = rch
                        nodes.append(node)
            return nodes
        return generate(0, n) if n else []
        
        
        