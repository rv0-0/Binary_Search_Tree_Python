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
