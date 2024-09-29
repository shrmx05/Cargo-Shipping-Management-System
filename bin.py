from avl import AVLTree
from node import Node
def f1(node1,node2):
    if node1.key.capacity<node2.key.capacity:
        return True
    elif node1.key.capacity==node2.key.capacity:
        if node1.key.bin_id<node2.key.bin_id:
            return True
        else:
            return False
    else:
        return False
def f2(node1,node2):
    if node1.key.bin_id<node2.key.bin_id:
        return True
    else:
        return False
def f3(node1,node2):
    if node1.key.object_id<node2.key.object_id:
        return True
    else:
        return False
def f4(node1,node2):
    if node1.key.capacity<node2.key.capacity:
        return True
    elif node1.key.capacity==node2.key.capacity:
        if node1.key.bin_id>node2.key.bin_id:
            return True
        else:
            return False
    else:
        return False
def check_equal_bin(node1,node2):
    if node1.key.bin_id==node2.key.bin_id:
        return True
    else:
        return False
def check_equal_obj(node1,node2):
    if node1.key.obj_id==node2.key.obj_id:
        return True
    else:
        return False
             
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.nodeobjtree= AVLTree(f3,check_equal_obj)

    def add_object(self, object):
        self.capacity-=object.size
        self.nodeobjtree.add_node(Node(object))

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        x=self.nodeobjtree.obj_id_search(object_id)
        self.capacity+=x.size
        a=x.key
        self.nodeobjtree.delete_node(Node(a))
        from avl import AVLTree
from node import Node
def f1(node1,node2):
    if node1.key.capacity<node2.key.capacity:
        return True
    elif node1.key.capacity==node2.key.capacity:
        if node1.key.bin_id<node2.key.bin_id:
            return True
        else:
            return False
    else:
        return False
def f2(node1,node2):
    if node1.key.bin_id<node2.key.bin_id:
        return True
    else:
        return False
def f3(node1,node2):
    if node1.key.object_id<node2.key.object_id:
        return True
    else:
        return False
def f4(node1,node2):
    if node1.key.capacity<node2.key.capacity:
        return True
    elif node1.key.capacity==node2.key.capacity:
        if node1.key.bin_id>node2.key.bin_id:
            return True
        else:
            return False
    else:
        return False
def check_equal_bin(node1,node2):
    if node1.key.bin_id==node2.key.bin_id:
        return True
    else:
        return False
def check_equal_obj(node1,node2):
    if node1.key.object_id==node2.key.object_id:
        return True
    else:
        return False
def blue_search(self,tree,obj_size):
    pointer=tree.root
    before=None
    while pointer:
        if pointer.key.capacity>=obj_size:
            before=pointer
            pointer=pointer.left
        else:
            pointer=pointer.right
    if before and before.key.capacity>=obj_size:        
        return before
    else:
        return None
        
    
def yellow_search(self,tree,obj_size):
    pointer=tree.root
    before=None
    while pointer:
        if pointer.key.capacity>=obj_size:
            before=pointer
            pointer=pointer.left
        else:
            pointer=pointer.right
    if before and before.key.capacity>=obj_size:        
        return before
    else:
        return None
def red_search(self,tree,obj_size):
    pointer=tree.root
    before=None
    while pointer:
        before=pointer
        pointer=pointer.right
    if before and before.key.capacity>=obj_size:        
        return before
    else:
        return None
def green_search(self,tree,obj_size):
    pointer=tree.root
    before=None
    while pointer:
        before=pointer
        pointer=pointer.right
    if before and before.key.capacity>=obj_size:        
        return before
    else:
        return None            
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id=bin_id
        self.capacity=capacity
        self.nodeobjtree= AVLTree(f3,check_equal_obj)

    def add_object(self, object):
        self.capacity-=object.size
        self.nodeobjtree.add_node(Node(object))

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        x=self.nodeobjtree.obj_id_search(object_id)
        print(x.key.object_id)
        self.capacity+=x.key.size
        a=x.key
        self.nodeobjtree.delete_node(Node(a))
        