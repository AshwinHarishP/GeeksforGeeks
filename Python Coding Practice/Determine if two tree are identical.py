#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        def helper(root):
            q = []
            res = []
            
            if not root:
                return res
                
            q.append(root)
            while q:
                curr = q.pop()
                res.append(curr.data)
                
                if curr.left:
                    q.append(curr.left)
                else:
                    res.append("N")
                
                if curr.right:
                    q.append(curr.right)
                else:
                    res.append("N")
                    
            return res
            
        
        dfs_1 = helper(root1)
        dfs_2 = helper(root2)
        return dfs_1 == dfs_2
            
            
