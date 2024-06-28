""" Export fbx"""
import bpy


def fbx_export(context):
    # Purge unused files and pack external resources
    bpy.ops.outliner.orphans_purge(
        do_local_ids=True, do_linked_ids=True, do_recursive=True
    )
    bpy.ops.file.autopack_toggle()

    # Create fbx with the same name as the blend file
    print("Export options: path_mode COPY, embed_textures = True")
    path = bpy.data.filepath
    fn = path.replace(".blend", "")
    bpy.ops.export_scene.fbx(
        filepath=fn + ".fbx", path_mode="COPY", embed_textures=True
    )


class FbxExport_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.fbx_export"
    bl_label = "Export FBX"
    bl_description = "Create FBX with the same name as the blend file"

    def execute(self, context):
        if bpy.data.is_saved:
            fbx_export(context)
            self.report({"INFO"}, "Fbx File Exported Correctly")
        else:
            self.report(
                {"ERROR"}, "ERROR: Save your file before exporting. Filename unknown"
            )
        return {"FINISHED"}
