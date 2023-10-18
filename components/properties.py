"""PROPERTIES"""
import bpy
import os

from components.constants import ROOT_DIR
from components.constants import FEMALE_BODY_PATH
from components.constants import MALE_BODY_PATH
from components.constants import var_bodyparts

def change_gender(self, context):
        scene = context.scene
        mytool = scene.PanelProperties
        
        if mytool.genderBool:
            BODIES_PATH = FEMALE_BODY_PATH
        else:
            BODIES_PATH = MALE_BODY_PATH
        for bodypart in var_bodyparts.values():
            try:
                
                bpy.data.objects[bodypart]
                
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[bodypart].select_set(True)
                bpy.ops.object.delete()

                bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

                bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", BODIES_PATH, "Object"),
                                files=[{"name": bodypart}])
                
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects[bodypart].modifiers["Armature"].object.select_set(True)
                bpy.ops.object.delete()

                bpy.data.objects[bodypart].parent = bpy.data.objects["Armature"]
                bpy.data.objects[bodypart].modifiers["Armature"].object = bpy.data.objects["Armature"]
            except:
                pass

class Properties(bpy.types.PropertyGroup):

    topBool: bpy.props.BoolProperty(
        name="Top",
        description="Specify if the scene contains a top object",
        default=False
    )

    shoesBool: bpy.props.BoolProperty(
        name="Shoes",
        description="Specify if the scene contains shoes",
        default=False
    )

    bottomBool: bpy.props.BoolProperty(
        name="Bottom",
        description="Specify if the scene contains a bottom object",
        default=False
    )
    acsBool: bpy.props.BoolProperty(
        name="Accessory",
        description="Specify if the scene contains an accesory object",
        default=False
    )

    bodypartsBool: bpy.props.BoolProperty(
        name="Body Parts Check",
        description="Select the body parts that should be visible and check that there are no collisions between them",
        default=False
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
        update = lambda self, context: change_gender(self, context)
    )

    unexpectedobjectBool: bpy.props.BoolProperty(
        name="Unexpected Object",
        default=False,
    )

