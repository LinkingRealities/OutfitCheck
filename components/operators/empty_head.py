"""Create Empty head"""
import bpy


def empty_head(context, location, scale, empty_display_size):
    bpy.ops.object.empty_add(type="PLAIN_AXES")
    bpy.data.objects["Empty"].name = "Empty-Head"
    bpy.data.objects["Empty-Head"].location = location
    bpy.data.objects["Empty-Head"].scale = scale
    bpy.data.objects["Empty-Head"].empty_display_size = empty_display_size


class EmptyFemaleHead_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.empty_female_head"
    bl_label = "Create female's head placeholder"
    bl_description = "Create an empty head object for the female avatar"

    def execute(self, context):
        location = (0, 0.04121, 1.54022)
        scale = (0.946819, 0.946819, 0.946819)
        empty_display_size = 0.14376
        empty_head(context=context, location=location, scale=scale, empty_display_size=empty_display_size)
        return {"FINISHED"}


class EmptyMaleHead_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.empty_male_head"
    bl_label = "Create male's head placeholder"
    bl_description = "Create an empty head object for the male avatar"

    def execute(self, context):
        location = (0, 0.01217, 1.65994)
        scale = (1.09001, 1.09001, 1.09001)
        empty_display_size = 0.14376
        empty_head(context=context, location=location, scale=scale, empty_display_size=empty_display_size)
        return {"FINISHED"}
