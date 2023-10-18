""" Main Panel """
import bpy

from components.panels.lib import create_objects_validation_panel
from components.panels.lib import image_size
from components.panels.lib import textures_validation
from components.panels.lib import image_packing
from components.panels.lib import unexpected_objects
from components.panels.lib import metadata_selector
from components.panels.lib import rigging_test
from components.panels.lib import gender_toggle
from components.panels.lib import polycount_validation
from components.panels.lib import face_toggle
from components.panels.lib import export_button
from components.panels.lib import parented_to_armature
from components.panels.lib import transformations_applied

def main_panel(panel_props, layout):
    
    #Gender toggle section
    gender_toggle(layout=layout, panel_props=panel_props)
    
    #Create and validate objects section
    create_objects_validation_panel(layout=layout, panel_props=panel_props)
    
    #Textures validation section
    textures_validation(layout=layout)

    #Armature parent section
    armatureparent = parented_to_armature(layout=layout)

    #Image packing check section
    imagepacking = image_packing(layout=layout)
    
    #Image size check section
    imagesize = image_size(layout=layout)

    #Unexpected object section
    unexpected_objects(layout=layout)

    #Transformations applied section
    transformations = transformations_applied(layout=layout)
    
    #Polycount section
    polycount = polycount_validation(layout=layout)

    #Face toggle section
    face_toggle(layout=layout)

    #Metadata selector section
    metadata_selector(layout=layout, panel_props=panel_props)

    #Rigging test section
    rigging_test(layout=layout)
    
    #Export button section
    export_button(layout=layout, panel_props=panel_props, polycount=polycount, imagesize=imagesize, imagepacking = imagepacking, armatureparent = armatureparent, transformations=transformations)

class ProductionCheck_PT_Panel_Main(bpy.types.Panel):
    """Creates a Panel in the Navigation Toolbar"""
    bl_label = "Union Avatars Production Tools"
    bl_idname = "OBJECT_PT_ProductionCheckPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'UA Production Tools'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        panel_props = scene.PanelProperties

        main_panel(panel_props=panel_props, layout=layout)



