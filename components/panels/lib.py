import bpy


var_head = "UnionAvatars_Head"
var_body = "UnionAvatars_Body"
var_top = "UnionAvatars_Top"
var_bottom = "UnionAvatars_Bottom"
var_shoes = "UnionAvatars_Shoes"
var_acs = "UnionAvatars_Acs"


def validate_required_objects(mytool):
    try:
        bpy.data.objects[var_body].select_get()
        bpy.data.objects[var_top].select_get()
        if mytool.bottomBool:
            bpy.data.objects[var_bottom].select_get()
        if mytool.shoesBool:
            bpy.data.objects[var_shoes].select_get()
        if mytool.acsBool:
            bpy.data.objects[var_acs].select_get()
        return True
    except:
        return False


def check_existence(layout, obj_name):
    try:
        bpy.data.objects[obj_name].select_get()
        return True
    except:
        #box = layout.box()
        #box.alert = True
        #box.label(text="haka haka")
        return False


def select_top_if_not_selected(layout, box):
    if check_existence(layout=layout, obj_name=var_top):
        box.label(text=f"Top set to {var_top} object")
    else:
        box.label(text="Select the top object for your character:")
        row = box.row()
        row.scale_y = 2.0
        row.operator("object.top_object_rename")


def select_bottom_if_not_selected(layout, box, mytool):
    if check_existence(layout=layout, obj_name=var_bottom):
        box.label(text=f"Bottom set to {var_bottom} object ")
    else:
        sub = box.row()
        sub.scale_x = 0.2
        sub.alert = False
        sub.prop(mytool, "bottomBool", icon_only=True)

        if mytool.bottomBool:
            sub.alert = True
            sub.label(text="Select the bottom object for your character:")
            box.alert = True
            sub = box.row()
            sub.scale_y = 2.0
            sub.operator("object.bottom_object_rename")
        else:
            sub.alert = False
            sub.label(text="Scene contains a bottom object")


def select_shoes_if_not_selected(layout, box, mytool):
    if check_existence(layout=layout, obj_name=var_shoes):
        box.label(text=f"Shoes set to {var_shoes } object")
    else:
        sub = box.row()
        sub.scale_x = 0.2
        sub.alert = False
        sub.prop(mytool, "shoesBool", icon_only=True)

        if mytool.shoesBool:
            sub.alert = True
            sub.label(text="Select the shoes object for your character:")
            box.alert = True
            sub = box.row()
            sub.scale_y = 2.0
            sub.operator("object.shoes_object_rename")
        else:
            sub.alert = False
            sub.label(text="Scene contains shoes")


def select_accessories_if_not_selectedv(layout, box, mytool):
    # Check if accessory object is present and has correct naming
    if check_existence(layout=layout, obj_name=var_acs):
        box.label(text=f"Accessory set to object {var_acs}")

    else:
        sub = box.row()
        sub.scale_x = 0.2
        sub.alert = False
        sub.prop(mytool, "acsBool", icon_only=True)

        if mytool.acsBool:
            sub.alert = True
            sub.label(text="Select the accessory object for your character:")
            box.alert = True
            sub = box.row()
            sub.scale_y = 2.0
            sub.operator("object.accessory_object_rename")
        else:
            sub.alert = False
            sub.label(text="Scene contains accessory")


def select_empty_head_if_not_selected(layout, mytool):
    if not mytool.commsCheck:
        row = layout.row()
        row.label(text="Empty is not required")
    else:
        try:
            bpy.data.objects["Empty-Head"].select_get()
            row = layout.row()
            row.label(text="Empty Head is included")
        except:
            row = layout.row()
            row.alert = True
            row.label(text="Missing Empty Head")
            row = layout.row()
            row.alert = True
            row.operator("object.empty_female_head")
            row.operator("object.empty_male_head")
            layout.separator()


def create_objects_validation_panel(layout, mytool):
    box = layout.box()

    if check_existence(layout=layout, obj_name="Armature"):
        box.label(text="Armature is valid")
    else:
        box.alert = True
        box.label(text="Can't find provided Armature. Please re-import it")

    if check_existence(layout=layout, obj_name=var_body):
        box.label(text=f"Body set to {var_body} object ")
    else:
        box.alert = True
        box.label(text=f"Can't find provided {var_body}. Please re-import it")

    select_top_if_not_selected(layout=layout, box=box)
    select_bottom_if_not_selected(layout=layout, box=box, mytool=mytool)
    select_shoes_if_not_selected(layout=layout, box=box, mytool=mytool)
    select_accessories_if_not_selectedv(layout=layout, box=box, mytool=mytool)
    select_empty_head_if_not_selected(layout=layout, mytool=mytool)




