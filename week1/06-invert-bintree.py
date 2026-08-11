#!/usr/bin/env python

# Leetcode Problem 226: Invert Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode | None) -> TreeNode | None:
    if root is not None:
        invertTree(root.left)
        invertTree(root.right)
        root.left, root.right = root.right, root.left
    return root


# An iterative solution using a stack.
def invertTree_it(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None

    stack = [root] # Initialize our stack with the root node.
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


# We can also use a queue instead of a stack for the iterative solution, using
# a collections.deque object for the queue.  We can then use queue.append() to
# add elements to the queue, and queue.popleft() to process the nodes in FIFO
# order.  That's left as an exercise for you, dear reader!
