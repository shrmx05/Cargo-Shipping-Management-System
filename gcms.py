from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
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
class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.bin_id_tree= AVLTree(f2,check_equal_bin)
        self.obj_tree= AVLTree(f3,check_equal_obj)
        self.bin_main_treeA= AVLTree(f1,check_equal_bin)
        self.bin_main_treeB= AVLTree(f4,check_equal_bin)

    def add_bin(self, bin_id, capacity):
        self.bin_id_tree.add_node(Node(Bin(bin_id,capacity)))
        self.bin_main_treeA.add_node(Node(Bin(bin_id,capacity)))
        self.bin_main_treeB.add_node(Node(Bin(bin_id,capacity)))
        


    def add_object(self, object_id, size, color):
        x=Object(object_id,size,color)
        obj=Node(x)
        if obj.key.color==Color.BLUE:
            allot=self.blue_search(self.bin_main_treeA,x.size)
            if allot==None:
                raise NoBinFoundException
        if obj.key.color==Color.YELLOW:
            allot=self.yellow_search(self.bin_main_treeB,x.size)
            if allot==None:
                raise NoBinFoundException
        if obj.key.color==Color.RED:
            allot=self.red_search(self.bin_main_treeB,x.size)
            if allot==None:
                raise NoBinFoundException
        if obj.key.color==Color.GREEN:
            allot=self.green_search(self.bin_main_treeA,x.size)
            if allot==None:
                raise NoBinFoundException
        obj.key.allotted_bin=allot.key.bin_id
        self.obj_tree.add_node(obj)
        p=allot.key
        self.bin_main_treeA.delete_node(Node(p))
        self.bin_main_treeB.delete_node(Node(p))
        self.bin_id_tree.delete_node(Node(p))
        p.add_object(x)
        self.bin_main_treeA.add_node(Node(p))
        self.bin_main_treeB.add_node(Node(p))
        self.bin_id_tree.add_node(Node(p))

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        x=self.obj_tree.obj_id_search(object_id)
        print(x.key.object_id)
        if not x:
            return None
        z=x.key
        y=self.bin_id_tree.binid_search(z.allotted_bin)
        w=y.key
        print(w.bin_id)
        self.bin_id_tree.delete_node(Node(w))
        self.bin_main_treeA.delete_node(Node(w))
        self.bin_main_treeB.delete_node(Node(w))
        print(w.bin_id)
        print(w.capacity)
        w.remove_object(object_id)
        print(w.capacity)
        print(w.bin_id)
        self.bin_id_tree.add_node(Node(w))
        self.bin_main_treeA.add_node(Node(w))
        self.bin_main_treeB.add_node(Node(w))
        x=self.obj_tree.obj_id_search(object_id)
        z=x.key
        self.obj_tree.delete_node(Node(z))
    def bin_info(self, bin_id):
        x=self.bin_id_tree.binid_search(bin_id)
        y=x.key
        t=y.nodeobjtree
        out=t.bfs(t.root,[])
        return (y.capacity,out)
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        x=self.obj_tree.obj_id_search(object_id)
        if not x:
            return None
        y=x.key
        ans=y.allotted_bin
        return ans
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
        
    
    