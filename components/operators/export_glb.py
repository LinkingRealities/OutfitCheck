"""Export glb"""
import bpy
from components.operators.material_renaming import rename_material
from components.operators.mesh_renaming import rename_mesh
from components.operators.texture_renaming import rename_texture


def glb_export(context):
    # Purge unused files and pack external resources
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

    # Create glb with the same name as the blend file
    print("Export options: export_draco_mesh_compression_enable = 1, export_draco_mesh_compression_level=10")
    path = bpy.data.filepath
    fn = path.replace(".blend", "")
    bpy.ops.export_scene.gltf(filepath=fn + ".glb", export_draco_mesh_compression_enable=1,
                              export_draco_mesh_compression_level=10,
                              export_image_format="JPEG")

def MeshAndMaterialAndTexturesRename(context, mytool):
    
    rename_mesh(context,'UnionAvatars_Top')
    rename_material(context,'UnionAvatars_Top')
    rename_texture('UnionAvatars_Top')
    
    if mytool.shoesBool:
        rename_mesh(context,'UnionAvatars_Shoes')
        rename_material(context,'UnionAvatars_Shoes')
        rename_texture('UnionAvatars_Shoes')
        
    if mytool.bottomBool:
        rename_mesh(context,'UnionAvatars_Bottom')
        rename_material(context,'UnionAvatars_Bottom')
        rename_texture('UnionAvatars_Bottom')
    
    if mytool.acsBool:
        rename_mesh(context,'UnionAvatars_Acs')
        rename_material(context,'UnionAvatars_Acs')
        rename_texture('UnionAvatars_Acs')


class GlbExportDev_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.glb_dev_export"
    bl_label = "Export GLB"
    bl_description = "Create Glb with the same name as the blend file"

    def execute(self, context):
        if bpy.data.is_saved:
            try:
                bpy.data.objects["Empty-Head"].select_get()
                glb_export(context)
                self.report({"INFO"}, "Glb File Exported Correctly")
                self.report({"INFO"}, "All textures were compressed to JPEG format")
            except:
                self.report({"ERROR"}, "ERROR: missing Empty-Head. Add to the scene to export Glb")
        else:
            self.report({"ERROR"}, "ERROR: Save this Blender file before exporting. Filename unknown")
        return {"FINISHED"}


class GlbExport_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.glb_export"
    bl_label = "Export GLB File"
    bl_description = "Create Glb file ready to send"

    def execute(self, context):
        if bpy.data.is_saved:
            try:
                bpy.data.objects["Empty-Head"].select_get()
                glb_export(context)
                self.report({"INFO"}, "Glb File Exported Correctly")
                self.report({"INFO"}, "All textures were compressed to JPEG format")
                
                MeshAndMaterialAndTexturesRename(context, mytool=context.scene.my_tool)
                
            except:
                self.report({"ERROR"}, "ERROR: missing Empty-Head. Add to the scene to export Glb")
        else:
            self.report({"ERROR"}, "ERROR: Save this Blender file before exporting. Filename unknown")
        return {"FINISHED"}
