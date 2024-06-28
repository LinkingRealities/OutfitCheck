bl_info = {
    "name": "Union Avatars Production Tools",
    "author": "Union Avatars",
    "version": (1, 2, 0),
    "blender": (3, 7, 7),
    "location": "View3D -> Right Sidebar -> Production Tools",
    "description": "Checks if an asset is ready for production",
    "warning": "",
    "doc_url": "",
    "category": "Interface",
}

import os
import sys

import bpy

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from components.operators.armature_parent import ArmatureParent_Operator
from components.operators.export_fbx import FbxExport_Operator
from components.operators.export_glb_json import GlbJsonExport_Operator
from components.operators.face_orientation_toggle import \
    FaceOrientationToggle_Operator
from components.operators.material_renaming import (
    AccesoryMaterialRename_Operator, BottomMaterialRename_Operator,
    ShoesMaterialRename_Operator, TopMaterialRename_Operator)
from components.operators.mesh_renaming import (AccessoryMeshRename_Operator,
                                                BottomMeshRename_Operator,
                                                ShoesMeshRename_Operator,
                                                TopMeshRename_Operator)
from components.operators.metadata_generation import (
    ActivateArmsBottom_Operator, ActivateArmsTop_Operator,
    ActivateBelly_Operator, ActivateChest_Operator, ActivateFeet_Operator,
    ActivateHands_Operator, ActivateHead_Operator, ActivateHips_Operator,
    ActivateLegsBottom_Operator, ActivateLegsTop_Operator,
    ChangeGender_Operator, ImportArmature_Operator)
from components.operators.object_renaming import (
    AccessoryObjectRename_Operator, BottomObjectRename_Operator,
    ShoesObjectRename_Operator, TopObjectRename_Operator)
from components.operators.rigging_test import (DancingLeftPose_Operator,
                                               DancingRightPose_Operator,
                                               DefaultPose_Operator,
                                               RestPose_Operator,
                                               RiggingTest_Operator,
                                               TPose_Operator,
                                               WalkingLeftPose_Operator,
                                               WalkingRightPose_Operator)
from components.operators.texture_renaming import TextureRename_Operator
from components.operators.textures_validation import \
    RemoveForbiddenTextures_Operator
from components.operators.transformations_apply import \
    TransformationsApply_Operator
from components.panels.main_panel import ProductionCheck_PT_Panel_Main
from components.properties import Properties

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
    RestPose_Operator,
    TPose_Operator,
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
    ActivateHead_Operator,
    ArmatureParent_Operator,
    TransformationsApply_Operator,
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
