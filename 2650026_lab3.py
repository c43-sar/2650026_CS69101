# Read a set of integer elements from an input file (input.txt)
import sys
arr0 = []
data0 = open("input.txt", 'r')

try:
    for line in data0.readlines():
        line_data = line.rstrip().split(',') #using rstrip to remove the \n
        for data in line_data:
            arr0.append(int(data))
except:
    sys.exit("[ERROR] Invalid data")

print(arr0)

# Construct a balanced AVL tree by inserting these elements one by one, performing the
# necessary LL, RR, LR, RL rotations to maintain balance after every insertion.

class AVL_Node:
    def __init__(self):
        self.lchild = None
        self.rchild = None
        self.value = None
        self.parent = None
        self.height = None
        self.balance_factor = None

def AVL_get_height(node: AVL_Node) -> int:
    if not node:
        return 0

    left = right = 0
    if node.lchild:
        left = node.lchild.height
    if node.rchild:
        right = node.rchild.height

    node.height = 1 + max(left.height, right.height) # type: ignore
    return node.height

def AVL_get_balance_factor(node: AVL_Node) -> int:
    if not node:
        return 0
    return AVL_get_height(node.lchild) - AVL_get_height(node.rchild) # type: ignore

