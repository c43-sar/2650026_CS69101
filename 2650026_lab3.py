# Read a set of integer elements from an input file (input.txt)
import sys
arr0 = []
data0 = open("input.txt", 'r')

try:
    for line in data0.readlines():
        line_data = line.rstrip().replace(' ','').split(',') #using rstrip to remove the \n
        for data in line_data:
            arr0.append(int(data))
except Exception as e:
    sys.exit("[ERROR] Invalid data" + str(e))

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

def AVL_get_height(node: AVL_Node | None) -> int:
    if node is None:
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

def AVL_right_rotate(y_node: AVL_Node | None) -> None:
    if y_node is None:
        return

    x_node = y_node.lchild
    TEMP_NODE = x_node.rchild # type: ignore

    x_node.rchild = y_node # type: ignore
    y_node.lchild = TEMP_NODE

    AVL_get_height(x_node)
    AVL_get_height(y_node)
    AVL_get_balance_factor(x_node) # type: ignore
    AVL_get_balance_factor(y_node)
    return

def AVL_left_rotate(y_node: AVL_Node | None) -> None:
    if y_node is None:
        return

    x_node = y_node.rchild
    TEMP_NODE = x_node.lchild # type: ignore

    y_node.lchild = x_node
    x_node.rchild = TEMP_NODE # type: ignore
    
    AVL_get_height(x_node)
    AVL_get_height(y_node)
    AVL_get_balance_factor(x_node) # type: ignore
    AVL_get_balance_factor(y_node)
    return
