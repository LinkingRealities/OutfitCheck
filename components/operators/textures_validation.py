""" Textures validation """
import bpy

var_head = "UnionAvatars_Head"
var_body = "UnionAvatars_Body"
var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"
var_shoes = "UnionAvatars_Shoes"
var_acs = "UnionAvatars_Acs"

MAX_TEXTURE_SIZE = 16777216  # bytes


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
            print(f"  {material.name}")
            try:
                nodes = material.node_tree.nodes  # Get a principled node
                principled = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
                if principled.inputs[texture_name].is_linked:
                    found = True
                    for link in principled.inputs[texture_name].links:
                        material.node_tree.links.remove(link)

                print(f"{texture_name}'s links were removed")

            except:
                print(f"Color Map was not presented for {var_target} object")

        bpy.data.objects[var_target].active_material_index = 0
        return found

    except:
        print(f"Couldn't remove {texture_name}. No {var_target} object was found")
        return False


class RemoveMetallicTexture_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.remove_metallic_texture"
    bl_label = "Remove Metallic texture"
    bl_description = "Remove metallic texture"

    def execute(self, context):
        if remove_unecessary_textures(texture_name="Metallic"):
            self.report({"INFO"}, "Metallic texture was detected and removed.")
        else:
            self.report({"INFO"}, "Metallic was already removed.")

        return {"FINISHED"}


class RemoveEmissionTexture_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.remove_emission_texture"
    bl_label = "Remove Emission texture"
    bl_description = "Remove Emission texture"

    def execute(self, context):
        if remove_unecessary_textures(texture_name="Emission"):
            self.report({"INFO"}, "Emission texture was detected and removed.")
        else:
            self.report({"INFO"}, "Emission was already removed.")

        return {"FINISHED"}


class RemoveRoughnessTexture_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.remove_roughness_texture"
    bl_label = "Remove Roughness texture"
    bl_description = "Remove Roughness texture"

    def execute(self, context):
        if remove_unecessary_textures(texture_name="Roughness"):
            self.report({"INFO"}, "Roughness texture was detected and removed.")
        else:
            self.report({"INFO"}, "Roughness was already removed.")

        return {"FINISHED"}


class ValidateTextures_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.validate_textures"
    bl_label = "Validate Textures"
    bl_description = "Validate Textures"

    def _check_textures_size(self, var_target):
        try:
            bpy.data.objects[var_target].active_material_index = 0
            for mat in bpy.data.objects[var_target].data.materials:
                try:
                    for node in mat.node_tree.nodes:
                        if node.type != 'TEX_IMAGE':
                            continue
                        texture = node.image
                        if not texture:
                            continue
                        size_bytes = texture.size[0] * texture.size[1] * texture.channels * texture.depth // 8

                        if size_bytes > MAX_TEXTURE_SIZE:
                            self.report({"WARNING"},
                                        f"{texture.name} texture's size={size_bytes}. It exceeds {MAX_TEXTURE_SIZE} "
                                        f"bytes. Please reduce it")
                        else:
                            self.report({"INFO"},
                                        f"{texture.name} texture's size={size_bytes}. It doesn't exceed "
                                        f"{MAX_TEXTURE_SIZE} bytes. It's acceptable")

                except:
                    print("Color Map not present")

            # return to index 0
            bpy.data.objects[var_target].active_material_index = 0
        except:
            print("Warning: No " + var_target)

    def _check_textures_format(self, var_target):
        try:
            bpy.data.objects[var_target].active_material_index = 0
            for mat in bpy.data.objects[var_target].data.materials:
                try:
                    for node in mat.node_tree.nodes:
                        if node.type != 'TEX_IMAGE':
                            continue
                        texture = node.image
                        if not texture:
                            continue

                        if texture.file_format != "JPEG":
                            self.report({"WARNING"},
                                        f"{texture.name} texture has "
                                        f"{texture.file_format} format. Please change to JPEG")
                        else:
                            self.report({"INFO"},
                                        f"{texture.name} texture has JPEG format. It's acceptable")

                except:
                    print("Color Map not present")

            # return to index 0
            bpy.data.objects[var_target].active_material_index = 0
        except:
            print("Warning: No " + var_target)

    def check_textures_size(self):
        self._check_textures_size(var_target=var_head)
        self._check_textures_size(var_target=var_body)
        self._check_textures_size(var_target=var_top)
        self._check_textures_size(var_target=var_bottom)
        self._check_textures_size(var_target=var_shoes)
        self._check_textures_size(var_target=var_acs)

    def check_textures_format(self):
        self._check_textures_format(var_target=var_head)
        self._check_textures_format(var_target=var_body)
        self._check_textures_format(var_target=var_top)
        self._check_textures_format(var_target=var_bottom)
        self._check_textures_format(var_target=var_shoes)
        self._check_textures_format(var_target=var_acs)

    def execute(self, context):
        self.check_textures_size()
        self.check_textures_format()

        return {"FINISHED"}
