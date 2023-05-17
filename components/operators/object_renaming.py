""" Object renaming """
import bpy

var_head = "UnionAvatars_Head"
var_body = "UnionAvatars_Body"
var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"
var_shoes = "UnionAvatars_Shoes"
var_acs = "UnionAvatars_Acs"


def rename_object(context, var_target):
    for obj in bpy.context.selected_objects:
        obj.name = var_target


class BodyObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.body_object_rename"
    bl_label = "Choose selected object as body"
    bl_description = "Rename selected object to " + var_body

    def execute(self, context):
        rename_object(context, var_body)
        return {"FINISHED"}


class TopObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.top_object_rename"
    bl_label = "Choose selected object as top"
    bl_description = "Rename selected object to " + var_top

    def execute(self, context):
        rename_object(context, var_top)
        return {"FINISHED"}


class BottomObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bottom_object_rename"
    bl_label = "Choose selected object as bottom"
    bl_description = "Rename selected object to " + var_bottom

    def execute(self, context):
        rename_object(context, var_bottom)
        return {"FINISHED"}


class ShoesObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.shoes_object_rename"
    bl_label = "Choose selected object as shoes"
    bl_description = "Rename selected object to " + var_shoes

    def execute(self, context):
        rename_object(context, var_shoes)
        return {"FINISHED"}


class AccessoryObjectRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.accessory_object_rename"
    bl_label = "Choose selected object as accessory"
    bl_description = "Rename selected object to " + var_acs

    def execute(self, context):
        rename_object(context, var_acs)
        return {"FINISHED"}
