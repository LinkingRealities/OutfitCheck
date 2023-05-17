""" Material renaming """
import bpy

var_head = "UnionAvatars_Head"
var_body = "UnionAvatars_Body"
var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"
var_shoes = "UnionAvatars_Shoes"
var_acs = "UnionAvatars_Acs"


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


class BodyMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.body_material_rename"
    bl_label = "Rename"

    def execute(self, context):
        rename_material(context, var_body)
        return {"FINISHED"}


class TopMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.top_material_rename"
    bl_label = "Rename"

    def execute(self, context):
        rename_material(context, var_top)
        return {"FINISHED"}


class BottomMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.bottom_material_rename"
    bl_label = "Rename"

    def execute(self, context):
        rename_material(context, var_bottom)
        return {"FINISHED"}


class ShoesMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.shoes_material_rename"
    bl_label = "Rename"

    def execute(self, context):
        rename_material(context, var_shoes)
        return {"FINISHED"}


class AccesoryMaterialRename_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.accessory_material_rename"
    bl_label = "Rename"

    def execute(self, context):
        rename_material(context, var_acs)
        return {"FINISHED"}


def check_material_name(var_target, col):
    active = bpy.data.objects[var_target]
    slots_materials = active.material_slots
    for count_m, _ in enumerate(slots_materials):
        if count_m > 0:
            if not bpy.data.objects[var_target].material_slots[count_m].name == var_target + str(count_m):
                raise ValueError("Error appeared in materials")
        else:
            if not bpy.data.objects[var_target].material_slots[count_m].name == var_target:
                raise ValueError("Error appeared in materials")

    col.alert = False
    col.label(icon="KEYTYPE_JITTER_VEC")
