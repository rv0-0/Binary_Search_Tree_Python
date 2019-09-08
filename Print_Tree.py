    def print_tree(self):
        if (self.root!=None):
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)
