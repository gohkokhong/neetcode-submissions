# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If root is empty, return empty string
        if not root:
            return []

        # Initialise result and queue
        result = []
        queue = deque([root])

        # While the len of queue is more than 0, iterate:
        while len(queue) > 0:
            # Initialise a list to store elements of current level
            level = []
            
            for i in range(len(queue)):
                # Set node = popleft() from the queue
                node = queue.popleft()
                # Append node.val to current level list
                level.append(node.val)

                # If node.left:
                if node.left:
                    queue.append(node.left)

                # If node.right:
                if node.right:
                    queue.append(node.right)

            # result.append(level)
            result.append(level)

        # return result
        return result