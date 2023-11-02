bl_info = {
    "name": "Production Check",
    "author": "Jónathan Garcia",
    "version": (1, 0),
    "blender": (3, 4, 1),
    "location": "Misc > Production Check",
    "description": "Checks if a model is ready for production",
    "warning": "",
    "doc_url": "",
    "category": "Interface",
}

# TODO:
# -Add Check Rig Button
#    -Check if objects are parented to armature
# -Add changed textures for Rename Textures
# -Check texture name before exporting
# -Check for png files
# -Check if body has only one material
# -Find a way to check collisions (separate linked/material & bool?)

import os
import sys
import bpy

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from components.operators.empty_head import EmptyMaleHead_Operator
from components.operators.empty_head import EmptyFemaleHead_Operator
from components.operators.export_glb import GlbExport_Operator
from components.operators.export_glb import GlbExportDev_Operator
from components.operators.export_fbx import FbxExport_Operator
from components.operators.texture_renaming import TextureRename_Operator
from components.operators.face_orientation_toggle import FaceOrientationToggle_Operator
from components.operators.mesh_renaming import BodyMeshRename_Operator
from components.operators.mesh_renaming import TopMeshRename_Operator
from components.operators.mesh_renaming import BottomMeshRename_Operator
from components.operators.mesh_renaming import ShoesMeshRename_Operator
from components.operators.mesh_renaming import AccessoryMeshRename_Operator
from components.operators.material_renaming import TopMaterialRename_Operator
from components.operators.material_renaming import BodyMaterialRename_Operator
from components.operators.material_renaming import BottomMaterialRename_Operator
from components.operators.material_renaming import ShoesMaterialRename_Operator
from components.operators.material_renaming import AccesoryMaterialRename_Operator
from components.operators.object_renaming import BodyObjectRename_Operator
from components.operators.object_renaming import BottomObjectRename_Operator
from components.operators.object_renaming import TopObjectRename_Operator
from components.operators.object_renaming import ShoesObjectRename_Operator
from components.operators.object_renaming import AccessoryObjectRename_Operator
from components.operators.rigging_test import RiggingTest_Operator
from components.operators.rigging_test import DancingLeftPose_Operator
from components.operators.rigging_test import DancingRightPose_Operator
from components.operators.rigging_test import WalkingLeftPose_Operator
from components.operators.rigging_test import WalkingRightPose_Operator
from components.operators.rigging_test import DefaultPose_Operator
from components.operators.textures_validation import RemoveMetallicTexture_Operator
from components.operators.textures_validation import RemoveEmissionTexture_Operator
from components.operators.textures_validation import RemoveRoughnessTexture_Operator
from components.operators.textures_validation import ValidateTextures_Operator
from components.properties import Properties
from components.panels.regular_panel import ProductionCheck_PT_Panel_Regular
from components.panels.advanced_panel import ProductionCheck_PT_Panel_Advanced

classes = [
    EmptyFemaleHead_Operator,
    EmptyMaleHead_Operator,
    ProductionCheck_PT_Panel_Regular,
    ProductionCheck_PT_Panel_Advanced,
    TextureRename_Operator,
    FaceOrientationToggle_Operator,
    BodyMeshRename_Operator,
    BodyObjectRename_Operator,
    BodyMaterialRename_Operator,
    TopObjectRename_Operator,
    TopMeshRename_Operator,
    TopMaterialRename_Operator,
    BottomObjectRename_Operator,
    BottomMeshRename_Operator,
    BottomMaterialRename_Operator,
    ShoesMeshRename_Operator,
    ShoesObjectRename_Operator,
    ShoesMaterialRename_Operator,
    AccessoryMeshRename_Operator,
    AccessoryObjectRename_Operator,
    AccesoryMaterialRename_Operator,
    GlbExport_Operator,
    GlbExportDev_Operator,
    FbxExport_Operator,
    RiggingTest_Operator,
    DancingLeftPose_Operator,
    DancingRightPose_Operator,
    WalkingLeftPose_Operator,
    WalkingRightPose_Operator,
    DefaultPose_Operator,
    RemoveMetallicTexture_Operator,
    RemoveEmissionTexture_Operator,
    RemoveRoughnessTexture_Operator,
    ValidateTextures_Operator
]


def register():
    try:
        bpy.utils.register_class(Properties)
        bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=Properties)

        for bpy_class in classes:
            bpy.utils.register_class(bpy_class)

    except KeyboardInterrupt:
        unregister()
        bpy.ops.wm.quit_blender()
        print("Caught keyboard interruption. Quitting blender...")


def unregister():
    bpy.utils.unregister_class(Properties)
    for bpy_class in classes:
        bpy.utils.unregister_class(bpy_class)

    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
