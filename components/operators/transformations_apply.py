""" Transformations Apply """
import bpy
from mathutils import Vector
from mathutils import Euler

from components.constants import var_garmenttypes
from components.panels.lib import check_existence

def transformations_apply():
    for garment_types in var_garmenttypes.values():
    
        if check_existence(garment_types):
            obj = bpy.data.objects[garment_types]
            
            if obj.location !=Vector((0.0,0.0,0.0)) or obj.scale !=Vector((1.0,1.0,1.0))or obj.rotation_euler != Euler((0.0, 0.0, 0.0)):
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[obj.name].select_set(True)
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


class TransformationsApply_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.transformations_apply"
    bl_label = "Fix"
    bl_description = "Apply transformations to conflicting objects"

    def execute(self, context):

        transformations_apply()
        
        return {"FINISHED"}
