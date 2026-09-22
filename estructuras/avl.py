from estructuras.arbol_binario import BST, Node as BSTNode


# Inherits from arbol_binario to create an AVL tree that balances automatically
# everytime we add an node to the tree
class AVLNode(BSTNode):
    def __init__(self, key, item):
        super().__init__(key, item)
        self.height = 1   # a new leaf counts as height 1


class AVL(BST):
    """
    Same ordering rule as BST (smaller left, larger right), but after every
    insert it checks the tree is still balanced and rotates if not.
    search() and in_order() are inherited unchanged from BST - balance
    never affects how those two work.
    """

    # ---------- small helpers ----------
    def _height(self, node):
        # empty subtree has height 0
        return node.height if node else 0

    def _balance_factor(self, node):
        # >1 means left-heavy, <-1 means right-heavy
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # ---------- rotations ----------
    # These re-arrange 3 nodes to fix a balance violation while keeping
    # "smaller left, larger right" true for every node involved.
    def _rotate_right(self, y):
        x = y.left
        t2 = x.right

        # perform rotation
        x.right = y
        y.left = t2

        # y moved down, so its height must be recalculated first
        self._update_height(y)
        self._update_height(x)

        return x  # x is the new top of this subtree

    def _rotate_left(self, x):
        y = x.right
        t2 = y.left

        # perform rotation
        y.left = x
        x.right = t2

        self._update_height(x)
        self._update_height(y)

        return y  # y is the new top of this subtree

    # ---------- insert (the part that can't be inherited) ----------
    def insert(self, key, item):
        self.root = self._insert(self.root, key, item)

    def _insert(self, node, key, item):
        # base case: empty spot, same as plain BST
        if node is None:
            return AVLNode(key, item)

        if key < node.key:
            node.left = self._insert(node.left, key, item)
        elif key > node.key:
            node.right = self._insert(node.right, key, item)
        else:
            node.items.append(item)   # duplicate key: keep both, no rebalancing needed
            return node

        # on the way back UP the recursion: refresh height, then check balance
        self._update_height(node)
        balance = self._balance_factor(node)

        # left-left case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # right-right case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # left-right case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # right-left case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node   # already balanced, nothing to do

