""" Textures validation """
import bpy

var_head = "UnionAvatars_Head"
var_body = "UnionAvatars_Body"
var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"
var_shoes = "UnionAvatars_Shoes"
var_acs = "UnionAvatars_Acs"

from components.constants import var_forbiddentextures

def remove_unecessary_textures(texture_name):
    removed = False
    if remove_links(var_top, texture_name):
        removed = True
    if remove_links(var_bottom, texture_name):
        removed = True
    if remove_links(var_body, texture_name):
        removed = True
    if remove_links(var_shoes, texture_name):
        removed = True
    if remove_links(var_acs, texture_name):
        removed = True
    return removed


def remove_links(var_target, texture_name):
    found = False

    try:
        bpy.data.objects[var_target].active_material_index = 0
        # Go through list of materials assigned to selected object
        for material in bpy.data.objects[var_target].data.materials:
            try:
                nodes = material.node_tree.nodes  # Get a principled node
                principled = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
                if principled.inputs[texture_name].is_linked:
                    found = True
                    for link in principled.inputs[texture_name].links:
                        material.node_tree.links.remove(link)
                        print(f"{var_target}: removed {texture_name} map")

            except:
                print(f"Color Map was not presented for {var_target} object")

        bpy.data.objects[var_target].active_material_index = 0
        return found

    except:
        #print(f"Couldn't remove {texture_name}. No {var_target} object was found")
        return False


class RemoveForbiddenTextures_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.remove_metallic_texture"
    bl_label = "Remove Metallic texture"
    bl_description = "Remove metallic texture"

    def execute(self, context):

        for texture_name in var_forbiddentextures:
            remove_unecessary_textures(texture_name)


        return {"FINISHED"}
