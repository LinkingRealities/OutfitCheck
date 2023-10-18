"""Export glb"""
import bpy
import os

from components.constants import var_bodyparts

def glb_export(context):
    # Purge unused files and pack external resources
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

    # Create glb with the same name as the blend file
    print("Export options: export_draco_mesh_compression_enable = 1, export_draco_mesh_compression_level=10, export_anim_single_armature = False")
    path = bpy.data.filepath
    fn = path.replace(".blend", "")
    bpy.ops.export_scene.gltf(filepath=fn + ".glb", export_draco_mesh_compression_enable=1, export_anim_single_armature = False,
                              export_draco_mesh_compression_level=10)
    

def bodyparts_present(context, bodypart):
    if context.scene.objects.get(bodypart):
        return "true"
    else:
        return "false"

def json_export(context):
    path = bpy.data.filepath
    fn = path.replace(".blend", ".json")
    file = open(fn, "w")
    result = "{\n    \"deployment_data\": {\n        \"source_type\": \"default\",\n        \"place\": \"body\"\n    },\n"
    
    result += "    \"garment_metadata\": {\n        \"body\":\n			{\n"
    
    for bodypart in var_bodyparts.values():
        if bodypart == list(var_bodyparts.values())[-1]:
            result += f"                \"{bodypart}\": {bodyparts_present(context, bodypart)}\n"
        elif bodypart == var_bodyparts['var_neck']:
            result += f"                \"{bodypart}\": true,\n"
        else:
            result += f"                \"{bodypart}\": {bodyparts_present(context, bodypart)},\n"
    

    result += "			},\n"
    result += "        \"version\": \"v4\",\n" 
    result += "        \"style\": \"phr\",\n"
    if context.scene.PanelProperties.genderBool: 
        result += "        \"gender\": \"female\",\n" 
    else:
        result += "        \"gender\": \"male\",\n"
    result += "        \"position\": \"outfit\",\n" 
    result += "        \"category\": null,\n"

    base=os.path.basename(path)
    garmentName = os.path.splitext(base)[0]

    result += f"        \"description\": \"{garmentName}\",\n"
    result += "        \"dyeable\": false,\n"
    result += "        \"default_colors\": [null]\n"
    result += "    }\n"
    result += "}"

    file.write(result)
    file.close()

class GlbJsonExport_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.glb_export"
    bl_label = "Create GLB and JSON files"
    bl_description = "Create Glb and Json files for this outfit"

    def execute(self, context):
        if bpy.data.is_saved:
            
            glb_export(context)
            json_export(context)
            self.report({"INFO"}, "Glb File Exported Correctly")
            self.report({"INFO"}, "All textures were compressed to JPEG format")
                
            
        else:
            self.report({"ERROR"}, "ERROR: Save this Blender file before exporting. Filename unknown")
        return {"FINISHED"}
