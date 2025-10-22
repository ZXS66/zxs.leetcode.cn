from typing import Optional
from _models import TreeNode

def build_tree_from_preorder_list(values: list[int]) -> Optional[TreeNode]:
    """build TreeNode from preorder traversal of full tree with None as null nodes

    Args:
        values (list[int]): values

    Returns:
        Optional[TreeNode]: TreeNode, None if the list is empty
    """
    if values is None or len(values) == 0:
        return None
    n = len(values)
    nodes = { i: None if values[i] is None else TreeNode(values[i]) for i in range(n)}
    for i in range(n):
        theNode = nodes[i]
        if theNode is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < n and nodes[left_index] is not None:
                theNode.left = nodes[left_index]
            if right_index < n and nodes[right_index] is not None:
                theNode.right = nodes[right_index]
    return nodes[0]
    
    