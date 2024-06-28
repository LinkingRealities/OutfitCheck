"""PROPERTIES"""
import os

import bpy

from components.constants import (CRT_BODY_PATH, FEMALE_BODY_PATH,
                                  MALE_BODY_PATH, ROOT_DIR, var_bodyparts)


def change_gender(self, context):
    scene = context.scene
    mytool = scene.PanelProperties

    if mytool.styleBool:
        if mytool.genderBool:
            BODIES_PATH = FEMALE_BODY_PATH
        else:
            BODIES_PATH = MALE_BODY_PATH
    else:
        BODIES_PATH = CRT_BODY_PATH

    bpy.ops.object.select_all(action="DESELECT")
    bpy.data.objects["Armature"].select_set(True)
    bpy.ops.object.delete()
    try:
        bpy.ops.wm.append(
            directory=os.path.join(ROOT_DIR, "assets", BODIES_PATH, "Object"),
            files=[{"name": "Armature"}],
        )
    except:
        raise ValueError("the Armature does not exist in the base file!")
    for bodypart in var_bodyparts.values():
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
            )

            bpy.ops.object.select_all(action="DESELECT")
            bpy.data.objects[bodypart].modifiers["Armature"].object.select_set(True)
            bpy.ops.object.delete()

            bpy.data.objects[bodypart].parent = bpy.data.objects["Armature"]
            bpy.data.objects[bodypart].modifiers["Armature"].object = bpy.data.objects[
                "Armature"
            ]
        except:
            pass


def change_style(self, context):
    scene = context.scene
    mytool = scene.PanelProperties

    if mytool.styleBool:
        if mytool.genderBool:
            BODIES_PATH = FEMALE_BODY_PATH
        else:
            BODIES_PATH = MALE_BODY_PATH
    else:
        BODIES_PATH = CRT_BODY_PATH

    bpy.ops.object.select_all(action="DESELECT")
    bpy.data.objects["Armature"].select_set(True)
    bpy.ops.object.delete()
    try:
        bpy.ops.wm.append(
            directory=os.path.join(ROOT_DIR, "assets", BODIES_PATH, "Object"),
            files=[{"name": "Armature"}],
        )
    except:
        raise ValueError("the Armature does not exist in the base file!")
    for bodypart in var_bodyparts.values():
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
            )

            bpy.ops.object.select_all(action="DESELECT")
            bpy.data.objects[bodypart].modifiers["Armature"].object.select_set(True)
            bpy.ops.object.delete()

            bpy.data.objects[bodypart].parent = bpy.data.objects["Armature"]
            bpy.data.objects[bodypart].modifiers["Armature"].object = bpy.data.objects[
                "Armature"
            ]
        except:
            pass


class Properties(bpy.types.PropertyGroup):
    topBool: bpy.props.BoolProperty(
        name="Top",
        description="Specify if the scene contains a top object",
        default=False,
    )

    shoesBool: bpy.props.BoolProperty(
        name="Shoes", description="Specify if the scene contains shoes", default=False
    )

    bottomBool: bpy.props.BoolProperty(
        name="Bottom",
        description="Specify if the scene contains a bottom object",
        default=False,
    )
    acsBool: bpy.props.BoolProperty(
        name="Accessory",
        description="Specify if the scene contains an accesory object",
        default=False,
    )

    bodypartsBool: bpy.props.BoolProperty(
        name="Body Parts Check",
        description="Select the body parts that should be visible and check that there are no collisions between them",
        default=False,
    )

    def default_bool():
        try:
            bpy.data.materials["UnionAvatars_Body_male"]
            return False
        except:
            return True

    genderBool: bpy.props.BoolProperty(
        name="Gender",
        description="Select the gender of your outfit",
        default=default_bool(),
        update=lambda self, context: change_gender(self, context),
    )

    unexpectedobjectBool: bpy.props.BoolProperty(
        name="Unexpected Object",
        default=False,
    )

    styleBool: bpy.props.BoolProperty(
        name="Style",
        description="Select the Style of your asset",
        default=default_bool(),
        update=lambda self, context: change_style(self, context),
    )
