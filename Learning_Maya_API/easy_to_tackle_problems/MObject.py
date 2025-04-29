
from maya.api import OpenMaya as om
import importlib

'''
import sys
import importlib

from Maya_Python_Qt_UIs.Learning_Maya_API.easy_to_tackle_problems import MObject
importlib.reload(MObject)

node = MObject.convert_name_to_MObject_node('pymel_sphere')
MObject.get_name_of_MObject(node)
MObject.get_hash_of_a_node(node, True)
'''
from Maya_Python_Qt_UIs.Learning_Maya_API import pymel_test
importlib.reload(pymel_test)

pymel_test.test_pymel("pymel_sphere")

def convert_name_to_MObject_node(obj_name):
    '''
    # 1 = create an instance of `MSelectionList` type. (Doesn't have anything 
        to do with selections).This must be created and populated in seperate 
        steps (# 2 afterwards).
    # 2 = This takes a MEL-klike sekection string (e.g: the name of the node), 
        to add the object we are looking for to the list
    # 3 = Create an empty `MObject` instance that will eventually point to the 
        node we arer looking for.
    # 4 = Retrive the empty MObject istance corresponding to the node at the 
        specified index in the `MSelectionList`, since there is only one item 
        the index is 0. the `getDependNode` returns an MObject.
    # 5 = Finally, we have the MObject instance for our node. 
        (visible is the unsightly string representation of Maya Python API objects.)

    
    # Attributes:
        obj_name (string): name of a Maya node
    '''
    sellist = om.MSelectionList() # 1
    sellist.add(obj_name) # 2 
    node = om.MObject() # 3
    node = sellist.getDependNode(0) # 4
    print(f"MObject conversion {node}") # 5

    return node


def get_name_of_MObject(node):
    '''
    # 1 = `MFnDependencyNode` function set is used to find the node's name

    # Attributes:
        node (MObject): MObject node
    '''
    # How can I check if it's an MObject to begin with?
    try:
        mobj_name = om.MFnDependencyNode(node).name() # 1
        print(f"getting the name of an MObject: {mobj_name}")
    except ValueError as e:
        print(f"node passed to arg is NOT an MObject: {node} > error = {e}")


def get_hash_of_a_node(node, api=None):
    '''
    # 1 = `MObjectHandle` Gets the hash through the Maya Python Api. 
            (class works conceptually the same to a function set, 
            providing some additional functionality to an MObject's instance).
    # 2 = Get the hash of a node in Python's built in hash function. Which 
            PyMel returns with the hash value!
    
    # The usefulness of a hash is as follows: 
        > You can identify Maya nodes between PyMel and the API, even if names 
            change or all you have is the hash value.
        > The hash value is based off certain properties of the node such as 
            its attributes or connections.
        > 
    
    # Attributes:
        node (MObject/string): MObject node or pynode
        api (boolean): choose MObject node or pynode
    '''
    if api:
        om_hash = om.MObjectHandle(node).hashCode() # 1
        print(f"the hash of an MObject node: `{om_hash}`")
    else:
        pm_hash = hash(node) # 2
        print(f"the hash of a pynode: `{pm_hash}`")
        