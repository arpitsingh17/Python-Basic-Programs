class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None



#
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

def printInorderRecur(root):

    if root:

        # First recur on left child
        printInorderRecur(root.left)

        # then print the data of node
        print(root.key),

        # now recur on right child
        printInorderRecur(root.right)

def printInorderIter(root):
    current = root
    done = 0
    s = []
    while not done:
        if current is not None:
            s.append(current)
            current = current.left

        else:
            if len(s)>0:
                current = s.pop()
                print current.key,
                current = current.right
            else:
                done = 1




print "Preorder traversal of binary tree is", printInorderRecur(root)
print "Preorder traversal of binary tree is", printInorderIter(root)




