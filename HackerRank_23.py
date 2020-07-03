import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        node_list = []
        final_result = ''
        node_list.append(root)
        while len(node_list) > 0:
            node = node_list.pop(0)
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
            final_result += str(node.data) + ' '
        print(final_result)

T=int(input())  
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
