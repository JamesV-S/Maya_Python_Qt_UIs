
from maya.api import OpenMaya as om
import importlib

'''
import sys
import importlib

from Maya_Python_Qt_UIs.Learning_Maya_API.easy_to_tackle_problems import MObject
importlib.reload(MObject)

MObject.convert_name_to_MObject_node('pymel_sphere')
'''
from Maya_Python_Qt_UIs.Learning_Maya_API import pymel_test
importlib.reload(pymel_test)

pymel_test.test_pymel("pymel_sphere")

def convert_name_to_MObject_node(obj_name):
    '''
    # 1 = create instance of `MSelectionList` type. (Doesn't have anything to 
        do with selections).This must be created and populated in seperate 
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
