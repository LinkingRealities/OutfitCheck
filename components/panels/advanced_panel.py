""" Advanced panel """
import bpy

var_head = "UnionAvatars_Head"
var_body = "UnionAvatars_Body"
var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"
var_shoes = "UnionAvatars_Shoes"
var_acs = "UnionAvatars_Acs"

from components.operators.material_renaming import check_material_name


def developer_panel(mytool, layout):
    
    row=layout.row(align = True)
    row.prop(mytool, "commsCheck", text="Include Empty Head")
    
    # Subpanel naming

    split = layout.split()

    # Column 0, aligned
    col = split.column(align=True)
    col.scale_x = 0.5
    col.label(text="")

    sub = col.row()
    sub.enabled = False
    sub.label(text="   ")
    sub.prop(mytool, "decoyBool", text="")

    sub = col.row()
    sub.enabled = False
    sub.label(text="   ")
    sub.prop(mytool, "decoyBool", text="")

    sub = col.row()
    sub.enabled = False
    sub.label(text="   ")
    sub.prop(mytool, "decoyBool", text="")

    sub = col.row()
    sub.label(text="   ")
    sub.prop(mytool, "shoesBool", text="")

    # First column
    col = split.column(align=True)
    col.label(text="")
    col.label(text="Body")
    col.label(text="Top")
    col.label(text="Bottom")

    sub = col.row()
    sub.enabled = mytool.shoesBool
    sub.label(text="Shoes")

    # Object Renaming Operators

    # Second column, aligned
    col = split.column(align=True)
    col.label(text="Object")

    # Check if body object is present and has correct naming
    try:
        bpy.data.objects[var_body].select_get()
        col.scale_x = 1.0
        col.alert = False
        col.label(icon="KEYTYPE_JITTER_VEC")

    except:
        col.alert = True
        col.operator("object.body_object_rename")

    # Check if top object is present and has correct naming
    try:
        bpy.data.objects[var_top].select_get()
        col.scale_x = 1.0
        col.alert = False
        col.label(icon="KEYTYPE_JITTER_VEC")

    except:
        col.alert = True
        col.operator("object.top_object_rename")

    # Check if bottom object is present and has correct naming
    try:
        bpy.data.objects[var_bottom].select_get()
        col.scale_x = 1.0
        col.alert = False
        col.label(icon="KEYTYPE_JITTER_VEC")

    except:
        col.alert = True
        col.operator("object.bottom_object_rename")

    # Check if shoes object is present and has correct naming
    if mytool.shoesBool:
        try:
            bpy.data.objects[var_shoes].select_get()
            col.scale_x = 1.0
            col.alert = False
            col.label(icon="KEYTYPE_JITTER_VEC")

        except:
            col.alert = True
            col.operator("object.shoes_object_rename")
    else:
        sub = col.row()
        sub.enabled = False
        sub.label(text="  -")

    # Mesh Renaming Operators

    # Third column, aligned
    col = split.column(align=True)
    col.label(text="Mesh")

    # Check if body mesh is present and has correct naming
    try:
        bpy.data.objects[var_body].select_get()
        if bpy.data.objects[var_body].data.name == bpy.data.objects[var_body].name:
            col.alert = False
            col.label(icon="KEYTYPE_JITTER_VEC")
        else:
            col.alert = True
            # row.label(icon="ORPHAN_DATA")
            col.operator("object.body_mesh_rename")
    except:
        col.label(text="  -")

    # Check if top mesh is present and has correct naming
    try:
        bpy.data.objects[var_top].select_get()
        if bpy.data.objects[var_top].data.name == bpy.data.objects[var_top].name:
            col.alert = False
            col.label(icon="KEYTYPE_JITTER_VEC")
        else:
            col.alert = True
            col.operator("object.top_mesh_rename")
    except:
        col.label(text="  -")

    # Check if bottom mesh is present and has correct naming
    try:
        bpy.data.objects[var_bottom].select_get()
        if bpy.data.objects[var_bottom].data.name == bpy.data.objects[var_bottom].name:
            col.alert = False
            col.label(icon="KEYTYPE_JITTER_VEC")
        else:
            col.alert = True
            col.operator("object.bottom_mesh_rename")
    except:
        col.label(text="  -")

    # Check if shoes mesh is present and has correct naming
    if mytool.shoesBool:
        try:
            bpy.data.objects[var_shoes].select_get()
            if bpy.data.objects[var_shoes].data.name == bpy.data.objects[var_shoes].name:
                col.alert = False
                col.label(icon="KEYTYPE_JITTER_VEC")
            else:
                col.alert = True
                col.operator("object.shoes_mesh_rename")
        except:
            col.label(text="  -")
    else:
        sub = col.row()
        sub.enabled = False
        sub.label(text="  -")

    # Material Renaming Operators

    # Fourth column, aligned
    col = split.column(align=True)
    col.label(text="Mats")

    # Check if body has the correct material naming
    try:
        bpy.data.objects[var_body].select_get()
        try:
            check_material_name(var_body, col)
        except:
            col.alert = True
            col.operator("object.body_material_rename")
    except:
        col.label(text="  -")

    # Check if top has the correct material naming
    try:
        bpy.data.objects[var_top].select_get()
        try:
            check_material_name(var_top, col)
        except:
            col.alert = True
            col.operator("object.top_material_rename")
    except:
        col.label(text="  -")

    # Check if bottom has the correct material naming
    try:
        bpy.data.objects[var_bottom].select_get()
        try:
            check_material_name(var_bottom, col)
        except:
            col.alert = True
            col.operator("object.bottom_material_rename")
    except:
        col.label(text="  -")

    # Check if shoes has the correct material naming
    if mytool.shoesBool:
        try:
            bpy.data.objects[var_shoes].select_get()
            try:
                check_material_name(var_shoes, col)
            except:
                col.alert = True
                col.operator("object.shoes_material_rename")
        except:
            col.label(text="  -")
    else:
        sub = col.row()
        sub.enabled = False
        sub.label(text="  -")
    row=layout.row(align = True)
    row.operator("object.fbx_export")


class ProductionCheck_PT_Panel_Advanced(bpy.types.Panel):
    """Creates a Panel in the Navigation Toolbar"""
    bl_label = "Advanced tools for production check"
    bl_idname = "OBJECT_PT_ProductionCheckAdvanced"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'DEFAULT_CLOSED', "HIDE_HEADER"}
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        if mytool.developerBool:
            developer_panel(mytool=mytool, layout=layout)
