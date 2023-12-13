""" Material renaming """
import bpy

from components.constants import var_garmenttypes

def rename_material(context, var_target):
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True)
    material_slots = bpy.data.objects[var_target].material_slots

    for count_rename, _ in enumerate(material_slots):
        bpy.data.objects[var_target].active_material_index = count_rename

        if count_rename > 0:
            bpy.data.objects[var_target].active_material.name = var_target + str(count_rename)
        else:
            bpy.data.objects[var_target].active_material.name = var_target

    bpy.data.objects[var_target].active_material_index = 0

class TopMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.top_material_rename"
    bl_label = "Rename material"

    def execute(self, context):
        rename_material(context, var_garmenttypes['var_top'])
        #rename_texture(var_garmenttypes['var_top']) (commented, does not work)
        return {"FINISHED"}


class BottomMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bottom_material_rename"
    bl_label = "Rename material"

    def execute(self, context):
        rename_material(context, var_garmenttypes['var_bottom'])
        #rename_texture(var_garmenttypes['var_bottom']) (commented, does not work)
        return {"FINISHED"}


class ShoesMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.shoes_material_rename"
    bl_label = "Rename material"

    def execute(self, context):
        rename_material(context, var_garmenttypes['var_shoes'])
        #rename_texture(var_garmenttypes['var_shoes']) (commented, does not work)
        return {"FINISHED"}


class AccesoryMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.accessory_material_rename"
    bl_label = "Rename"

    def execute(self, context):
        rename_material(context, var_garmenttypes['var_acs'])
        return {"FINISHED"}

