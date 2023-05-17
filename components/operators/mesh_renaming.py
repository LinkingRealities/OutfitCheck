""" Mesh renaming """
import bpy


var_head = "UnionAvatars_Head"
var_body = "UnionAvatars_Body"
var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"
var_shoes = "UnionAvatars_Shoes"
var_acs = "UnionAvatars_Acs"


def rename_mesh(context, var_target):
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True)
    bpy.data.objects[var_target].data.name = bpy.data.objects[var_target].name


class BodyMeshRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.body_mesh_rename"
    bl_label = "Rename"
    bl_description = "Rename Body mesh to match their parent object"

    def execute(self, context):
        rename_mesh(context, var_body)
        return {"FINISHED"}


class TopMeshRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.top_mesh_rename"
    bl_label = "Rename"
    bl_description = "Rename Top mesh to match their parent object"

    def execute(self, context):
        rename_mesh(context, var_top)
        return {"FINISHED"}


class BottomMeshRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bottom_mesh_rename"
    bl_label = "Rename"
    bl_description = "Rename Bottom mesh to match their parent object"

    def execute(self, context):
        rename_mesh(context, var_bottom)
        return {"FINISHED"}


class ShoesMeshRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.shoes_mesh_rename"
    bl_label = "Rename"
    bl_description = "Rename Shoes mesh to match their parent object"

    def execute(self, context):
        rename_mesh(context, var_shoes)
        return {"FINISHED"}


class AccessoryMeshRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.accessory_mesh_rename"
    bl_label = "Rename"
    bl_description = "Rename Accessory mesh to match their parent object"

    def execute(self, context):
        rename_mesh(context, var_acs)
        return {"FINISHED"}
