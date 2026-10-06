from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#прямой обход:узел, лево, право
def pryamoy_obhod(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        pryamoy_obhod(root.left, result)
        pryamoy_obhod(root.right, result)
    return result


#симметричный: лево, узел, право
def simmetrichny_obhod(root, result=None):
    if result is None:
        result = []
    if root:
        simmetrichny_obhod(root.left, result)
        result.append(root.value)
        simmetrichny_obhod(root.right, result)
    return result


#обратный: лево, право, узел
def obratny_obhod(root, result=None):
    if result is None:
        result = []
    if root:
        obratny_obhod(root.left, result)
        obratny_obhod(root.right, result)
        result.append(root.value)
    return result


# обход по уровням(BFS)
def po_urovnyam(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


#самый длинный путь от корня до листа(вариативная часть)
def samy_dlinny_put(root):
    if root is None:
        return []
    # если лист, путь из одного узла
    if root.left is None and root.right is None:
        return [root.value]
    left_path = samy_dlinny_put(root.left)
    right_path = samy_dlinny_put(root.right)
    if len(left_path) > len(right_path):
        return [root.value] + left_path
    else:
        return [root.value] + right_path


if __name__ == '__main__':
    #    1
    #   / \
    #  2   3
    # / \   \
    #4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Дерево 1:")
    print("pryamoy:    ", pryamoy_obhod(root))
    print("simmetrichny:", simmetrichny_obhod(root))
    print("obratny:    ", obratny_obhod(root))
    print("po urovnyam:", po_urovnyam(root))
    print("samy dlinny put:", samy_dlinny_put(root))

    #     10
    #    /  \
    #   5    15
    #  / \
    # 3   7
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(7)

    print()
    print("Дерево 2:")
    print("pryamoy:    ", pryamoy_obhod(root2))
    print("simmetrichny:", simmetrichny_obhod(root2))
    print("obratny:    ", obratny_obhod(root2))
    print("po urovnyam:", po_urovnyam(root2))
    print("samy dlinny put:", samy_dlinny_put(root2))

    #бамбук
    #   1
    #  /
    # 2
    #/
    #3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)

    print()
    print("Дерево 3 (бамбук):")
    print("pryamoy:    ", pryamoy_obhod(root3))
    print("simmetrichny:", simmetrichny_obhod(root3))
    print("obratny:    ", obratny_obhod(root3))
    print("po urovnyam:", po_urovnyam(root3))
    print("samy dlinny put:", samy_dlinny_put(root3))