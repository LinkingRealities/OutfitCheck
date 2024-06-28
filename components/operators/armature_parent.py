""" Armature Parent """
import bpy

from components.constants import var_garmenttypes
from components.panels.lib import check_existence


def parent_to_armature():
    for garment_types in var_garmenttypes.values():
        if check_existence(garment_types):
            try:
                bpy.data.objects[garment_types].modifiers["Armature"].object.name
                if (
                    bpy.data.objects[garment_types].parent
                    != bpy.data.objects["Armature"]
                ):
                    raise KeyError
            except:
                try:
                    bpy.data.objects[garment_types].modifiers["Armature"].object
                except:
                    bpy.ops.object.select_all(action="DESELECT")
                    bpy.data.objects[garment_types].select_set(True)
                    bpy.ops.object.modifier_add(type="ARMATURE")

                bpy.data.objects[garment_types].modifiers[
                    "Armature"
                ].object = bpy.data.objects["Armature"]

                bpy.data.objects[garment_types].parent = bpy.data.objects["Armature"]


class ArmatureParent_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.armature_parent"
    bl_label = "Fix"
    bl_description = "Parent objects to armature"

    def execute(self, context):
        parent_to_armature()

        return {"FINISHED"}
