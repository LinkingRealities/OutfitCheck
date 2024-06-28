""" Texture renaming """
import bpy


def rename_texture(var_target):
    try:
        print(f"Renaming materials for {bpy.data.objects[var_target].name}:")

        bpy.data.objects[var_target].active_material_index = 0

        # Go through list of materials assigned to selected object
        for material in bpy.data.objects[var_target].data.materials:
            print("  " + material.name)
            # Rename BaseColor if present
            try:
                # Get the nodes in the node tree
                nodes = material.node_tree.nodes
                # Get a principled node
                principled = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
                # Get the slot for "base color"
                base_color = principled.inputs["Base Color"]  # Or principled.inputs[0]
                # Get the link
                linkColor = base_color.links[0]
                linkColor_node = linkColor.from_node

                # Rename the image to the material name plus the extension
                linkColor_node.image.name = material.name + "_c.jpg"
                print(f"   {linkColor_node.image.name} renamed")

            except:
                print("   -Color Map not present")

            # Rename NormalMap if present
            try:
                # Get the nodes in the node tree
                nodes = material.node_tree.nodes
                # Get a principled node
                principled = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
                # Get the slot for "base color"
                normal = principled.inputs["Normal"]
                # Get the link
                linkNormal = normal.links[0].from_node.inputs["Color"].links[0]
                linkNormal_node = linkNormal.from_node

                # Rename the image to the material name plus the extension
                linkNormal_node.image.name = material.name + "_n.jpg"

                print(f"   {linkNormal_node.image.name} renamed")

            except:
                print("   -Normal Map not present")

        # return to index 0
        bpy.data.objects[var_target].active_material_index = 0
    except:
        print("Warning: No " + var_target)


class TextureRename_Operator(bpy.types.Operator):
    """Tooltip"""

    bl_idname = "object.texture_rename"
    bl_label = "Rename Textures"
    bl_description = "Rename all textures to match material name"

    def execute(self, context):
        # texture_rename(context,var_body)
        # rename_texture(var_top)
        # rename_texture(var_bottom)
        # texture_rename(context,var_shoes)
        self.report({"INFO"}, "All textures Renamed Correctly")
        return {"FINISHED"}
