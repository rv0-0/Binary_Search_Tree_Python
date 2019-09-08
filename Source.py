class node:
    def __init__(self,value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value,self.root)
    
    def _insert(self,value,cur_node):
        if cur_node.value > value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
            else:
                self._insert(value,cur_node.left_child)
        elif cur_node.value < value:
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("Value already in the tree")
    
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


    def print_tree(self):
        if (self.root!=None):
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

def filltree(tree,num_elems=100,max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem=randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree=binary_search_tree()

tree=filltree(tree)
tree.print_tree()
print("height:"+str(tree.get_height()))
