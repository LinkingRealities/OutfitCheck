bl_info = {
    "name": "Union Avatars Production Tools",
    "author": "Jónathan Garcia, Gaukhar Kuttubeck",
    "version": (1, 1),
    "blender": (3, 3, 0),
    "location": "View3D -> Right Sidebar -> Production Tools",
    "description": "Checks if a model is ready for production",
    "warning": "",
    "doc_url": "",
    "category": "Interface",
}

# TODO:
# -Check if objects are parented to armature
# -Check if transformations are applied
# -Add button to pack textures
# -Find a way to check collisions (separate linked/material & bool?)

import os
import sys
import bpy

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from components.operators.export_glb_json import GlbJsonExport_Operator
from components.operators.export_fbx import FbxExport_Operator
from components.operators.texture_renaming import TextureRename_Operator
from components.operators.face_orientation_toggle import FaceOrientationToggle_Operator
from components.operators.mesh_renaming import TopMeshRename_Operator
from components.operators.mesh_renaming import BottomMeshRename_Operator
from components.operators.mesh_renaming import ShoesMeshRename_Operator
from components.operators.mesh_renaming import AccessoryMeshRename_Operator
from components.operators.material_renaming import TopMaterialRename_Operator
from components.operators.material_renaming import BottomMaterialRename_Operator
from components.operators.material_renaming import ShoesMaterialRename_Operator
from components.operators.material_renaming import AccesoryMaterialRename_Operator
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
from components.operators.textures_validation import RemoveForbiddenTextures_Operator
from components.operators.metadata_generation import ImportArmature_Operator
from components.operators.metadata_generation import ActivateHands_Operator
from components.operators.metadata_generation import ActivateArmsBottom_Operator
from components.operators.metadata_generation import ActivateArmsTop_Operator
from components.operators.metadata_generation import ActivateChest_Operator
from components.operators.metadata_generation import ActivateBelly_Operator
from components.operators.metadata_generation import ActivateHips_Operator
from components.operators.metadata_generation import ActivateLegsTop_Operator
from components.operators.metadata_generation import ActivateLegsBottom_Operator
from components.operators.metadata_generation import ActivateFeet_Operator
from components.operators.metadata_generation import ChangeGender_Operator
from components.operators.armature_parent import ArmatureParent_Operator
from components.operators.transformations_apply import TransformationsApply_Operator
from components.properties import Properties
from components.panels.main_panel import ProductionCheck_PT_Panel_Main

classes = [
    ProductionCheck_PT_Panel_Main,
    TextureRename_Operator,
    FaceOrientationToggle_Operator,
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
    GlbJsonExport_Operator,
    FbxExport_Operator,
    RiggingTest_Operator,
    DancingLeftPose_Operator,
    DancingRightPose_Operator,
    WalkingLeftPose_Operator,
    WalkingRightPose_Operator,
    DefaultPose_Operator,
    RemoveForbiddenTextures_Operator,
    ImportArmature_Operator,
    ActivateHands_Operator,
    ActivateArmsBottom_Operator,
    ActivateArmsTop_Operator,
    ActivateChest_Operator,
    ActivateBelly_Operator,
    ActivateHips_Operator,
    ActivateLegsTop_Operator,
    ActivateLegsBottom_Operator,
    ActivateFeet_Operator,
    ChangeGender_Operator,
    ArmatureParent_Operator,
    TransformationsApply_Operator
]


def register():
    try:
        bpy.utils.register_class(Properties)
        bpy.types.Scene.PanelProperties = bpy.props.PointerProperty(type=Properties)

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

    del bpy.types.Scene.PanelProperties


if __name__ == "__main__":
    register()
