from node import Node
# AVL Tree Class
class AVLTree:
    def __init__(self, compare_function, equal_function):
        self.root = None
        self.size = 0
        self.comparator = compare_function
        self.equal = equal_function

    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def is_leaf(self, node):
        return node and node.left is None and node.right is None

    def is_root(self, node):
        return node and node.parent is None

    def add_node(self, node):
        if not self.root:
            self.root = node
            return
        pointer = self.root
        while pointer:
            if self.equal(pointer, node):
                return pointer
            if self.comparator(node, pointer):
                if pointer.left is None:
                    pointer.left = node
                    node.parent = pointer
                    break
                pointer = pointer.left
            else:
                if pointer.right is None:
                    pointer.right = node
                    node.parent = pointer
                    break
                pointer = pointer.right

        node.height = 1
        self.balance_tree(node)

    def balance_tree(self, node):
        ancestor = node.parent
        imbalance = None

        while ancestor:
            left_height = self.height(ancestor.left)
            right_height = self.height(ancestor.right)
            prev_height = ancestor.height

            ancestor.height = 1 + max(left_height, right_height)

            if prev_height == ancestor.height:
                break
            if abs(left_height - right_height) > 1:
                imbalance = ancestor
                break
            ancestor = ancestor.parent

        if imbalance:
            self.restructure(imbalance)

    def delete_leaf(self, pointer):
        if pointer.right is None:
            self._replace_node_in_parent(pointer, pointer.left)
        elif pointer.left is None:
            self._replace_node_in_parent(pointer, pointer.right)

        pointer.parent = pointer.left = pointer.right = None

    def _replace_node_in_parent(self, node, new_child):
        if not node.parent:
            self.root = new_child
            if new_child:
                new_child.parent = None
        elif node == node.parent.right:
            node.parent.right = new_child
        else:
            node.parent.left = new_child

        if new_child:
            new_child.parent = node.parent

    def delete_node(self, target):
        pointer = self.root
        delete_leaf = None

        while pointer:
            if self.equal(pointer, target):
                if pointer.left is None or pointer.right is None:
                    delete_leaf = pointer
                    break
                internal_node = pointer
                curr = internal_node.right
                while curr.left:
                    curr = curr.left
                internal_node.key = curr.key
                delete_leaf = curr
                break
            elif self.comparator(target, pointer):
                pointer = pointer.left
            else:
                pointer = pointer.right

        ancestor = delete_leaf.parent
        self.delete_leaf(delete_leaf)

        if not self.is_leaf(ancestor):
            self.balance_after_deletion(ancestor)

    def balance_after_deletion(self, ancestor):
        while ancestor:
            left_height = self.height(ancestor.left)
            right_height = self.height(ancestor.right)
            ancestor.height = 1 + max(left_height, right_height)

            if abs(left_height - right_height) > 1:
                imbalance = ancestor
                self.restructure(imbalance)

            ancestor = ancestor.parent

    def left_rotation(self, p):
        y = p.right
        T2 = y.left

        self._relink_parents(p, y)
        y.left = p
        p.parent = y
        p.right = T2
        if T2:
            T2.parent = p

        self.update_height(p)
        self.update_height(y)

    def right_rotation(self, p):
        y = p.left
        T2 = y.right

        self._relink_parents(p, y)
        y.right = p
        p.parent = y
        p.left = T2
        if T2:
            T2.parent = p

        self.update_height(p)
        self.update_height(y)

    def _relink_parents(self, old_node, new_node):
        if old_node.parent:
            if old_node == old_node.parent.right:
                old_node.parent.right = new_node
            else:
                old_node.parent.left = new_node
        else:
            self.root = new_node

        new_node.parent = old_node.parent

    def restructure(self, p):
        if self.height(p.left) > self.height(p.right):
            x = p.left
            if self.height(x.left) >= self.height(x.right):
                self.right_rotation(p)
            else:
                self.left_rotation(x)
                self.right_rotation(p)
        else:
            x = p.right
            if self.height(x.right) >= self.height(x.left):
                self.left_rotation(p)
            else:
                self.right_rotation(x)
                self.left_rotation(p)

    def binid_search(self, bin_id):
        pointer = self.root
        while pointer:
            if pointer.key.bin_id < bin_id:
                pointer = pointer.right
            elif pointer.key.bin_id > bin_id:
                pointer = pointer.left
            else:
                return pointer

    def obj_id_search(self, obj_id):
        pointer = self.root
        while pointer:
            if pointer.key.object_id < obj_id:
                pointer = pointer.right
            elif pointer.key.object_id > obj_id:
                pointer = pointer.left
            else:
                return pointer

    def bfs(self, node, out=None):
        if out is None:
            out = []
        if not node:
            return out
        out.append(node.key.object_id)
        if node.left:
            self.bfs(node.left, out)
        if node.right:
            self.bfs(node.right, out)
        return out
