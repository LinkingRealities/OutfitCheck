import bpy
from mathutils import Vector
from mathutils import Euler

from components.constants import var_bodyparts
from components.constants import var_garmenttypes
from components.constants import var_forbiddentextures

from components.constants import OUTFIT_TRIANGLE_LIMIT 
from components.constants import ACCESSORIES_TRIANGLE_LIMIT
from components.constants import TOP_TRIANGLE_LIMIT
from components.constants import BOTTOM_TRIANGLE_LIMIT
from components.constants import SHOES_TRIANGLE_LIMIT
from components.constants import MAX_TEXTURE_SIZE

def validate_required_objects(panel_props):
    try:
        if panel_props.topBool:
            bpy.data.objects[var_garmenttypes['var_top']].select_get()
        if panel_props.bottomBool:
            bpy.data.objects[var_garmenttypes['var_bottom']].select_get()
        if panel_props.shoesBool:
            bpy.data.objects[var_garmenttypes['var_shoes']].select_get()
        if panel_props.acsBool:
            bpy.data.objects[var_garmenttypes['var_acs']].select_get()
        return True
    except:
        return False

def check_existence(obj_name):
    try:
        bpy.data.objects[obj_name].select_get()
        return True
    except:
        return False
    
def check_material_name(var_target, col):
    active = bpy.data.objects[var_target]
    slots_materials = active.material_slots
    for count_m, _ in enumerate(slots_materials):
        if count_m > 0:
            if not bpy.data.objects[var_target].material_slots[count_m].name == var_target + str(count_m):
                raise ValueError("Error appeared in materials")
        else:
            if not bpy.data.objects[var_target].material_slots[count_m].name == var_target:
                raise ValueError("Error appeared in materials")

    col.alert = False


def select_top_if_not_selected(box, panel_props):
    if check_existence(obj_name=var_garmenttypes['var_top']):
        try:
            check_material_name(var_garmenttypes['var_top'], box)
            box.alert = False
            box.scale_y = .9
            box.label(text=f"Top set to {var_garmenttypes['var_top']} object")
        except:
            box.alert = True
            box.scale_y = .9
            box.label(text=f"{var_garmenttypes['var_top']} has an incorrect material name")
            row = box.row()
            row.operator("object.top_material_rename")
    else:
        sub = box.row()
        sub.scale_x = 0.2
        sub.alert = False
        sub.prop(panel_props, "topBool", icon_only=True)

        if panel_props.topBool:
            sub.alert = True
            sub.label(text="Select the top object for your character:")
            box.alert = True
            sub = box.row()
            sub.scale_y = 2.0
            sub.operator("object.top_object_rename")
        else:
            sub.alert = False
            sub.label(text="Scene contains a top object")


def select_bottom_if_not_selected(box, panel_props):
    if check_existence(obj_name=var_garmenttypes['var_bottom']):
        
        try:
            check_material_name(var_garmenttypes['var_bottom'], box)
            box.alert = False
            box.scale_y = .9
            box.label(text=f"Bottom set to {var_garmenttypes['var_bottom']} object")
        except:
            box.alert = True
            box.scale_y = .9
            box.label(text=f"{var_garmenttypes['var_bottom']} has an incorrect material name")
            row = box.row()
            row.operator("object.bottom_material_rename")
            
    else:
        sub = box.row()
        sub.scale_x = 0.2
        sub.alert = False
        sub.prop(panel_props, "bottomBool", icon_only=True)

        if panel_props.bottomBool:
            sub.alert = True
            sub.label(text="Select the bottom object for your character:")
            box.alert = True
            sub = box.row()
            sub.scale_y = 2.0
            sub.operator("object.bottom_object_rename")
        else:
            sub.alert = False
            sub.label(text="Scene contains a bottom object")


def select_shoes_if_not_selected(box, panel_props):
    if check_existence(obj_name=var_garmenttypes['var_shoes']):
        try:
            check_material_name(var_garmenttypes['var_shoes'], box)
            box.alert = False
            box.scale_y = .9
            box.label(text=f"Shoes set to {var_garmenttypes['var_shoes']} object")
        except:
            box.alert = True
            box.scale_y = .9
            box.label(text=f"{var_garmenttypes['var_shoes']} has an incorrect material name")
            row = box.row()
            row.operator("object.shoes_material_rename")
    else:
        sub = box.row()
        sub.scale_x = 0.2
        sub.alert = False
        sub.prop(panel_props, "shoesBool", icon_only=True)

        if panel_props.shoesBool:
            sub.alert = True
            sub.label(text="Select the shoes object for your character:")
            box.alert = True
            sub = box.row()
            sub.scale_y = 2.0
            sub.operator("object.shoes_object_rename")
        else:
            sub.alert = False
            sub.label(text="Scene contains shoes")


def select_accessories_if_not_selectedv(box, panel_props):
    # Check if accessory object is present and has correct naming
    if check_existence(obj_name=var_garmenttypes['var_acs']):
        try:
            check_material_name(var_garmenttypes['var_acs'], box)
            box.alert = False
            box.scale_y = .9
            box.label(text=f"Accessory set to {var_garmenttypes['var_acs']} object")
        except:
            box.alert = True
            box.scale_y = .9
            box.label(text=f"{var_garmenttypes['var_acs']} has an incorrect material name")
            row = box.row()
            row.operator("object.accessory_material_rename")

    else:
        sub = box.row()
        sub.scale_x = 0.2
        sub.alert = False
        sub.prop(panel_props, "acsBool", icon_only=True)

        if panel_props.acsBool:
            sub.alert = True
            sub.label(text="Select the accessory object for your character:")
            box.alert = True
            sub = box.row()
            sub.scale_y = 2.0
            sub.operator("object.accessory_object_rename")
        else:
            sub.alert = False
            sub.label(text="Scene contains accessory")


def create_objects_validation_panel(layout, panel_props):
    box = layout.box()

    if check_existence(obj_name="Armature"):
        box.scale_y = .9
        box.label(text="Armature is set")
    else:
        box.alert = True
        box.scale_y = .9
        box.label(text="Armature not found")
        box.operator("object.import_armature")

    select_top_if_not_selected(box=box, panel_props=panel_props)
    select_bottom_if_not_selected(box=box, panel_props=panel_props)
    select_shoes_if_not_selected(box=box, panel_props=panel_props)
    select_accessories_if_not_selectedv(box=box, panel_props=panel_props)


def calculate_polygons():
    sum_faces = []
    for obj in bpy.data.objects:
        if obj.type != 'MESH' or obj.name in var_bodyparts.values():
            continue
        faces = sum(len(polygon.vertices) - 2 for polygon in obj.data.polygons)
        sum_faces.append(faces)
    return sum(sum_faces)   

def image_size(layout):
    try:
        for img in bpy.data.images:
            if not img.packed_file:
                continue
            if img.packed_file.size/1024 > MAX_TEXTURE_SIZE:
                raise KeyError  
        var_bigger_images = True      
    except:
        #layout.separator()
        bigger_images = layout.box()
        bigger_images_row = bigger_images.row()
        bigger_images_row.alert = True
        bigger_images_row.scale_y = .9
        bigger_images_row.label(text = f"Some images are too big:")
        var_bigger_images = False
                
    
    for img in bpy.data.images:
        if not img.packed_file:
                continue
        if img.packed_file.size/1024 > MAX_TEXTURE_SIZE:
            bigger_images_row = bigger_images.row()
            bigger_images_row.alert = True
            bigger_images_row.scale_y = .9
            bigger_images_row.label(text = f"Image [{img.name}] is bigger than 150 kb")
    
    return var_bigger_images

def check_texture_links(textures_validation,var_target, texture_name):
    found = False
    try:
        # Go through list of materials assigned to selected object
        for material in bpy.data.objects[var_target].data.materials:
            try:
                nodes = material.node_tree.nodes  # Get a principled node
                principled = next(n for n in nodes if n.type == "BSDF_PRINCIPLED")
                if principled.inputs[texture_name].is_linked:
                    found = True
                    textures_row = textures_validation.row()
                    textures_row.alert = True
                    textures_row.scale_y = .9
                    textures_row.label(text = f"{var_target} has a {texture_name} map")
            except:
                pass
        return found

    except:
        return False
    
def textures_validation(layout):
    textures_validation = False

    for garmenttypes in var_garmenttypes.values():
        for textures in var_forbiddentextures:
            if check_texture_links(textures_validation,garmenttypes, textures):
                textures_validation = True
                
    if textures_validation:
        textures_validation = layout.box()

    for garmenttypes in var_garmenttypes.values():
        for textures in var_forbiddentextures:
            check_texture_links(textures_validation,garmenttypes, textures)

    if textures_validation:            
        textures_row = textures_validation.row()
        textures_row.alert = True
        textures_row.scale_y = .9
        textures_row.operator("object.remove_metallic_texture", text = "Remove")

def source_validation(layout):
    textures_validation = False

    for image in bpy.data.images:
        if bpy.data.images[image.name].source == 'TILED':
            textures_validation = True
                
    if textures_validation:
        textures_validation = layout.box()

    if textures_validation:            
        textures_row = textures_validation.row()
        textures_row.alert = True
        textures_row.scale_y = .9
        textures_row.label(text = f"UDIM IMAGES DETECTED")
        textures_row = textures_validation.row()
        textures_row.alert = True
        textures_row.label(text = "Some images are set in UDIM mode. Please change them to single mode.")

def image_packing(layout):
    try:
        for img in bpy.data.images:
            if not img.packed_file and img.name != "Render Result":
                raise KeyError
        var_unpacked_images = True 
    except:
        #layout.separator()
        unpacked_images = layout.box()  
        unpacked_images_row = unpacked_images.row()
        unpacked_images_row.alert = True
        unpacked_images_row.scale_y = .9
        unpacked_images_row.label(text = f"UNPACKED IMAGES IN THE SCENE")
        unpacked_images_row = unpacked_images.row()
        unpacked_images_row.alert = True
        unpacked_images_row.scale_y = .9
        unpacked_images_row.label(text = f"Please activate File-External Data-Pack Resources (can take a while to change)")
        var_unpacked_images = False  
    return var_unpacked_images

def unexpected_objects(layout):
    try:
        for obj in bpy.context.scene.objects: 
            if obj.name not in var_bodyparts.values() and obj.name not in var_garmenttypes.values() and obj.name != "Armature":
                raise KeyError
        var_unexpected_objects = False
    except:
        var_unexpected_objects = True
    
    if var_unexpected_objects:
        #layout.separator()
        strange_objects = layout.box()

    for obj in bpy.context.scene.objects: 
        if obj.name not in var_bodyparts.values() and obj.name not in var_garmenttypes.values() and obj.name != "Armature":
            strange_objects_row = strange_objects.row()
            strange_objects_row.scale_y = .9
            strange_objects_row.alert = True
            strange_objects_row.label(text=f"Unexpected object in the scene: [{obj.name}]. Please remove it")
    
    return var_unexpected_objects

def metadata_selector(layout, panel_props):

    metadata_row = layout.box()

    metadata_row.label(text = "Visible Body Parts")

    row0 = metadata_row.row()
    row0.operator("object.activate_head", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts["var_head"]) else 'NONE' )

    row1 = metadata_row.row()
    row1.operator("object.activate_chest", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_chest']) else 'NONE' )
    row1.operator("object.activate_armstop", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_armsTop']) else 'NONE' )
    row1.operator("object.activate_legstop", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_legsTop']) else 'NONE' )
    
    row2 = metadata_row.row()
    row2.operator("object.activate_belly", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_belly']) else 'NONE' )
    row2.operator("object.activate_armsbottom", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_armsBottom']) else 'NONE' )
    row2.operator("object.activate_legsbottom", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_legsBottom']) else 'NONE' )
    
    row3 = metadata_row.row()
    row3.operator("object.activate_hips", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_hips']) else 'NONE' )
    row3.operator("object.activate_hands", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_hands']) else 'NONE' )
    row3.operator("object.activate_feet", icon = 'CHECKMARK' if bpy.context.scene.objects.get(var_bodyparts['var_feet']) else 'NONE' )
    
    row4 = metadata_row.row()
    
    if panel_props.bodypartsBool: 
        row4.alert = False
        row4.prop(panel_props, "bodypartsBool", text="I have checked that the visible body parts are correct")
    else:
        row4.alert = True
        row4.prop(panel_props, "bodypartsBool", text="I have checked that the visible body parts are correct")

def rigging_test(layout):
    rigging_raw = layout.box()

    try:
        rigging_raw.label(text="Rigging Test")
        row0 = rigging_raw.row(align = True)
        row0.scale_y = 1.5
        row0.operator("object.t_pose")
        row0.operator("object.default_pose")
        row0.operator("object.rest_pose")
        row1 = rigging_raw.row()
        row1.operator("object.dancingright_pose")
        row1.operator("object.dancingleft_pose")
        row2 = rigging_raw.row()
        row2.operator("object.walkingright_pose")
        row2.operator("object.walkingleft_pose")
        
    except:
        rigging_raw.label(text="Couldn't import poses library")

def gender_toggle(layout, panel_props):
    gender_toggle_box = layout.box()
    gender_toggle = gender_toggle_box.row(align = True)
    gender_toggle.scale_y = 2
    gender_toggle.prop(panel_props, "genderBool", toggle = True, text = "Female")
    gender_toggle.prop(panel_props, "genderBool", toggle = True, invert_checkbox = True, text = "Male")

def polygon_message(body_part, triangle_limit):
    try:
        summa = calculate_polygons()
        if summa <= 0:
            return False, "There are no garments in the scene"
        elif summa > triangle_limit:
            return False, f"{body_part} triangle count: {summa}/{triangle_limit}. Please reduce it to be able to export"
        
        elif summa <= triangle_limit:
            return True, f"{body_part} triangle count: {summa}/{triangle_limit}"

    except Exception as exc:
        print("ERROR: Can't count polygons: ", exc)

def polycount_validation(layout):

    if check_existence(var_garmenttypes['var_top']) and not check_existence(var_garmenttypes['var_bottom']) and not check_existence(var_garmenttypes['var_shoes']) and not check_existence(var_garmenttypes['var_acs']):
        polycount_result, polycount_message = polygon_message(var_garmenttypes['var_top'],TOP_TRIANGLE_LIMIT)

    elif not check_existence(var_garmenttypes['var_top']) and check_existence(var_garmenttypes['var_bottom']) and not check_existence(var_garmenttypes['var_shoes']) and not check_existence(var_garmenttypes['var_acs']):
        polycount_result, polycount_message = polygon_message(var_garmenttypes['var_bottom'],BOTTOM_TRIANGLE_LIMIT)

    elif not check_existence(var_garmenttypes['var_top']) and not check_existence(var_garmenttypes['var_bottom']) and check_existence(var_garmenttypes['var_shoes']) and not check_existence(var_garmenttypes['var_acs']):
        polycount_result, polycount_message = polygon_message(var_garmenttypes['var_shoes'],SHOES_TRIANGLE_LIMIT)

    elif not check_existence(var_garmenttypes['var_top']) and not check_existence(var_garmenttypes['var_bottom']) and not check_existence(var_garmenttypes['var_shoes']) and check_existence(var_garmenttypes['var_acs']):
        polycount_result, polycount_message = polygon_message(var_garmenttypes['var_acs'],ACCESSORIES_TRIANGLE_LIMIT)
    else:
        polycount_result, polycount_message = polygon_message("Outfit",OUTFIT_TRIANGLE_LIMIT)

    if polycount_result:
            polygon_row = layout.box()
            polygon_row.alert = False
            polygon_row.scale_y = .9
            polygon_row.label(text="Polycount")
            polygon_row.label(text=polycount_message)
    else: 
        polygon_row = layout.box()
        polygon_row.alert = True
        polygon_row.scale_y = .9
        polygon_row.label(text="Polycount")
        polygon_row.label(text=polycount_message)
    
    return polycount_result

def face_toggle(layout):
    face_toggle_row = layout.box()
    face_toggle_row.label(text="Face Orientation Test")
    row0 = face_toggle_row.row()
    row0.scale_y = 1.5
    row0.operator("object.face_orientation_toggle")

def export_button(layout, panel_props, polycount,imagesize, imagepacking, armatureparent,transformations):
    validation_row = layout.row()
    export_row = layout.row()
    #Check if export button should be active or inactive
    if validate_required_objects(panel_props=panel_props) and polycount and panel_props.bodypartsBool and not unexpected_objects(layout=layout) and imagesize and imagepacking and not textures_validation(layout = layout) and armatureparent and transformations:
        export_row.enabled = True
    else:
        validation_row.alert = True
        validation_row.label(text="Requirements are not satisfied. Fix them to enable export button")
        export_row.alert = True
        export_row.enabled = False
    
    export_row.scale_y = 3.0
    export_row.scale_x = 0.5
    export_row.operator("object.glb_export")

def parented_to_armature(layout):
    var_armatureparent = True

    for garment_types in var_garmenttypes.values():
        if check_existence(garment_types):
            try:
                bpy.data.objects[garment_types].modifiers["Armature"].object.name

                if bpy.data.objects[garment_types].parent != bpy.data.objects["Armature"]: raise KeyError

            except:
                var_armatureparent = False
    
    if not var_armatureparent:
        armatureparent_box = layout.box()
    
    for garment_types in var_garmenttypes.values():
        if check_existence(garment_types):
            try:
                bpy.data.objects[garment_types].modifiers["Armature"].object.name
                if bpy.data.objects[garment_types].parent != bpy.data.objects["Armature"]: raise KeyError
            except:
                armatureparent_row = armatureparent_box.row()
                armatureparent_row.alert = True
                armatureparent_row.scale_y = 0.9
                armatureparent_row.label(text=f"{garment_types} is not parented to the armature")

    if not var_armatureparent:
        armatureparent_row = armatureparent_box.row()
        armatureparent_row.alert = True
        armatureparent_row.scale_y = 0.9
        armatureparent_row.operator("object.armature_parent")

    return var_armatureparent

def transformations_applied(layout):
    var_transformations_applied = True
    
    for garment_types in var_garmenttypes.values():
        if check_existence(garment_types):
            obj = bpy.data.objects[garment_types]  
            if obj.location !=Vector((0.0,0.0,0.0)) or obj.scale !=Vector((1.0,1.0,1.0))or obj.rotation_euler != Euler((0.0, 0.0, 0.0)):
                var_transformations_applied = False
    
    if not var_transformations_applied:
        transformations_box = layout.box()
    
    for garment_types in var_garmenttypes.values():
    
        if check_existence(garment_types):
            obj = bpy.data.objects[garment_types]
            
            if obj.location !=Vector((0.0,0.0,0.0)) or obj.scale !=Vector((1.0,1.0,1.0))or obj.rotation_euler != Euler((0.0, 0.0, 0.0)):
                transformations_row = transformations_box.row()
                transformations_row.alert = True
                transformations_row.scale_y = 0.9
                transformations_row.label(text=f"{garment_types} has unapplied transformations")
                var_transformations_applied = False
    
    if not var_transformations_applied:
        transformations_row = transformations_box.row()
        transformations_row.alert = True
        transformations_row.scale_y = 0.9
        transformations_row.operator("object.transformations_apply")

    return var_transformations_applied
