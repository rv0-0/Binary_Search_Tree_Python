    def get_height(self):
        if self.root==None:
            return 0
        else:
            return self._get_height(self.root,0)

    def _get_height(self,cur_node,height):
        if cur_node==None:
            return height
        left_height=self._get_height(cur_node.left_child,height+1)
        right_height=self._get_height(cur_node.right_child,height+1)
        return max(left_height,right_height)
