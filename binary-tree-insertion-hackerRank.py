

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_recursive(self.root, val)
        return self.root

    def _insert_recursive(self, root, val):
        if val < root.info:
            if root.left is None:
                root.left = Node(val)
            else:
                self._insert_recursive(root.left, val)
        elif val > root.info:
            if root.right is None:
                root.right = Node(val)
            else:
                self._insert_recursive(root.right, val)
