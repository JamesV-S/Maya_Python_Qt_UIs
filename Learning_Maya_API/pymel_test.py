
import maya.cmds as cmds
import pymel.core as pm

'''
import sys
import importlib

from Maya_Python_Qt_UIs.Learning_Maya_API import pymel_test
importlib.reload(pymel_test)
'''

def test_pymel(name):
    sphere = pm.polySphere(n=name)[0]
    pm.move(0,5,0, sphere)
    new_pos = pm.xform(sphere, q=True, translation=True, worldSpace=True)
    print(f"Created sphere: `{sphere}` using PyMel")
    print(f"Sphere's new position : `{new_pos}` using PyMel!")
    return sphere


def pyMel_vs_mayacmds():
    # key_difference_between maya.cmds & PyMel. 
        # maya.cmds is more direct
        
        # Pymel is more pythonic with its object-oriented approach for more 
        # intiuitive & readable code.

    # Maya.cmds example: 
    cmds_Cube = pm.polyCube(n='cmds_Cube')[0]
    cmds.setAttr(f"{cmds_Cube}.translate", -5, .5, 0, type="double3")

    # PyMel example:
    pymel_sphere = pm.polySphere(n='pymel_Spherre')[0]
    pymel_sphere.translate.set(5, 1, 0)