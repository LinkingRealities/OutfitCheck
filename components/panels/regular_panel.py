""" Regular panel """
import bpy

from components.operators.polygon_check import execute_polygon_check
from components.operators.texture_renaming import rename_texture
from components.panels.lib import create_objects_validation_panel
from components.panels.lib import validate_required_objects



var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"


def regular_panel(mytool, layout):
    create_objects_validation_panel(layout=layout, mytool=mytool)
    validation_row = layout.row()

    layout.separator()
    textures_removing_row = layout.row()
    textures_validation_row = layout.row()

    layout.separator()
    polygon_row = layout.row()

    layout.separator()
    rigging_raw = layout.box()
    try:
        #rigging_raw.scale_y = 1.5
        rigging_raw.label(text="Rigging Test")
        row0 = rigging_raw.row()
        row0.scale_y = 1.5
        row0.operator("object.default_pose")
        row1 = rigging_raw.row()
        row1.operator("object.dancingright_pose")
        row1.operator("object.dancingleft_pose")
        row2 = rigging_raw.row()
        row2.operator("object.walkingright_pose")
        row2.operator("object.walkingleft_pose")

    except:
        rigging_raw.label(text="Couldn't import poses library")
        export_row.enabled = False
    layout.separator()
    face_toggle_row = layout.row()

    layout.separator()
    export_row = layout.row()

    if validate_required_objects(mytool=mytool):
        export_row.enabled = True
        validation_row.enabled = True

    else:
        validation_row.alert = True
        validation_row.label(text="Objects requirements are not satisfied. Fix them to enable export button")
        validation_row.enabled = False
        export_row.alert = True
        export_row.enabled = False

    if validation_row.enabled:
        rename_texture(var_top)
        rename_texture(var_bottom)

    textures_removing_row.scale_x = 0.5
    textures_removing_row.operator("object.remove_metallic_texture")
    textures_removing_row.operator("object.remove_roughness_texture")
    textures_removing_row.operator("object.remove_emission_texture")

    is_correct, message = execute_polygon_check()

    if is_correct:
        polygon_row.label(text=message)
        polygon_row.enabled = True
    else:
        polygon_row.alert = True
        polygon_row.label(text=message)
        export_row.alert = True
        export_row.enabled = False

    textures_validation_row.scale_x = 0.5
    textures_validation_row.operator("object.validate_textures")


    face_toggle_row.scale_y = 1.5
    face_toggle_row.operator("object.face_orientation_toggle")

    export_row.scale_y = 3.0
    export_row.scale_x = 0.5
    export_row.operator("object.glb_export")
    
    row = layout.row()
    row.prop(mytool, "developerBool")


class ProductionCheck_PT_Panel_Regular(bpy.types.Panel):
    """Creates a Panel in the Navigation Toolbar"""
    bl_label = "Regular tools for production check"
    bl_idname = "OBJECT_PT_ProductionCheckRegular"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        regular_panel(mytool=mytool, layout=layout)



