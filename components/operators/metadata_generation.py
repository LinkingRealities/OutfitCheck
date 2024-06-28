""" Metadata generation """
import os

import bpy

from components.constants import (CRT_BODY_PATH, FEMALE_BODY_PATH,
                                  MALE_BODY_PATH, ROOT_DIR, var_bodyparts)


def load_armature():
    mytool = bpy.context.scene.PanelProperties
    try:
        bpy.data.objects["Armature"]
    except:
        if mytool.styleBool:
            BODY_PATH = FEMALE_BODY_PATH
        else:
            BODY_PATH = CRT_BODY_PATH
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
        bpy.ops.wm.append(
            directory=os.path.join(ROOT_DIR, "assets", BODY_PATH, "Armature"),
            files=[{"name": "Armature"}],
        )


def activate_bodypart(context, bodypart):
    try:
        bpy.data.objects["Armature"]
        try:
            bpy.data.objects[bodypart]
            bpy.ops.object.select_all(action="DESELECT")
            bpy.data.objects[bodypart].select_set(True)
            bpy.ops.object.delete()
            return {"FINISHED"}
        except:
            try:
                scene = context.scene
                panel_props = scene.PanelProperties
                if panel_props.styleBool:
                    if panel_props.genderBool:
                        BODIES_PATH = FEMALE_BODY_PATH
                    else:
                        BODIES_PATH = MALE_BODY_PATH
                else:
                    BODIES_PATH = CRT_BODY_PATH
                load_bodypart(bodypart, BODIES_PATH)
                return {"FINISHED"}
            except:
                print({"ERROR"}, f"ERROR: {bodypart} were not imported")
    except:
        return {"ERROR"}


def load_bodypart(bodypart, BODIES_PATH):
    try:
        bpy.data.objects[bodypart]

    except:
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
        bpy.ops.wm.append(
            directory=os.path.join(ROOT_DIR, "assets", BODIES_PATH, "Object"),
            files=[{"name": bodypart}],
            do_reuse_local_id=True,
        )
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[bodypart].modifiers["Armature"].object.select_set(True)
        bpy.ops.object.delete()

        bpy.data.objects[bodypart].parent = bpy.data.objects["Armature"]
        bpy.data.objects[bodypart].modifiers["Armature"].object = bpy.data.objects[
            "Armature"
        ]

        print(f"{bodypart} Loaded")


def override_bodypart(bodypart, BODIES_PATH):
    try:
        bpy.data.objects[bodypart]

        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[bodypart].select_set(True)
        bpy.ops.object.delete()

        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
        bpy.ops.wm.append(
            directory=os.path.join(ROOT_DIR, "assets", BODIES_PATH, "Object"),
            files=[{"name": bodypart}],
            do_reuse_local_id=True,
        )

        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[bodypart].modifiers["Armature"].object.select_set(True)
        bpy.ops.object.delete()

        bpy.data.objects[bodypart].parent = bpy.data.objects["Armature"]
        bpy.data.objects[bodypart].modifiers["Armature"].object = bpy.data.objects[
            "Armature"
        ]
    except:
        return {"FINISHED"}


class ChangeGender_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.change_gender"
    bl_label = "Change gender"
    bl_description = "Change the gender from the avatar"

    def execute(self, context):
        scene = context.scene
        panel_props = scene.PanelProperties

        if panel_props.genderBool:
            BODIES_PATH = MALE_BODY_PATH
            panel_props.genderBool = False
        else:
            BODIES_PATH = FEMALE_BODY_PATH
            panel_props.genderBool = True
        for bodypart in var_bodyparts.values():
            override_bodypart(bodypart, BODIES_PATH)
        return {"FINISHED"}


class ImportArmature_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.import_armature"
    bl_label = "Import Armature"
    bl_description = "Import default avatar armature"

    def execute(self, context):
        try:
            load_armature()
            self.report({"INFO"}, "Armature imported correctly")
        except:
            self.report({"ERROR"}, "ERROR: Armature was not imported")
        return {"FINISHED"}


class ActivateHands_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_hands"
    bl_label = "Hands"
    bl_description = "Activate hands for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_hands"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateArmsBottom_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_armsbottom"
    bl_label = "Arms Bottom"
    bl_description = "Activate arms for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_armsBottom"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateArmsTop_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_armstop"
    bl_label = "Arms Top"
    bl_description = "Activate arms for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_armsTop"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateChest_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_chest"
    bl_label = "Chest"
    bl_description = "Activate chest for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_chest"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateBelly_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_belly"
    bl_label = "Belly"
    bl_description = "Activate belly for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_belly"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateHips_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_hips"
    bl_label = "Hips"
    bl_description = "Activate hips for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_hips"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateLegsTop_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_legstop"
    bl_label = "Legs Top"
    bl_description = "Activate legs for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_legsTop"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateLegsBottom_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_legsbottom"
    bl_label = "Legs Bottom"
    bl_description = "Activate legs for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_legsBottom"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateFeet_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_feet"
    bl_label = "Feet"
    bl_description = "Activate feet for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_feet"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}


class ActivateHead_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.activate_head"
    bl_label = "Head"
    bl_description = "Activate head for the avatar"

    def execute(self, context):
        context.scene.PanelProperties.bodypartsBool = False
        if activate_bodypart(context, var_bodyparts["var_head"]) == {"ERROR"}:
            self.report({"WARNING"}, "Please import Armature before adding bodyparts")
        return {"FINISHED"}
