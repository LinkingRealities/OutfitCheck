""" Object renaming """
import bpy

from components.constants import var_garmenttypes


def rename_object(context, var_target):
    for obj in bpy.context.selected_objects:
        obj.name = var_target

class TopObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.top_object_rename"
    bl_label = "Choose selected object as top"
    bl_description = "Rename selected object to " + var_garmenttypes['var_top']

    def execute(self, context):
        rename_object(context, var_garmenttypes['var_top'])
        return {"FINISHED"}


class BottomObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bottom_object_rename"
    bl_label = "Choose selected object as bottom"
    bl_description = "Rename selected object to " + var_garmenttypes['var_bottom']

    def execute(self, context):
        rename_object(context, var_garmenttypes['var_bottom'])
        return {"FINISHED"}


class ShoesObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.shoes_object_rename"
    bl_label = "Choose selected object as shoes"
    bl_description = "Rename selected object to " + var_garmenttypes['var_bottom']

    def execute(self, context):
        rename_object(context, var_garmenttypes['var_shoes'])
        return {"FINISHED"}


class AccessoryObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.accessory_object_rename"
    bl_label = "Choose selected object as accessory"
    bl_description = "Rename selected object to " + var_garmenttypes['var_acs']

    def execute(self, context):
        rename_object(context, var_garmenttypes['var_acs'])
        return {"FINISHED"}
