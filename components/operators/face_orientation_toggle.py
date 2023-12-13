""" Face orientation toggle """
import bpy

def toggle_face_orientation(context):
    for area in bpy.context.screen.areas:
        if area.type != "VIEW_3D":
            continue
        for space in area.spaces:
            if space.type != "VIEW_3D":
                continue
            space.overlay.show_face_orientation = not space.overlay.show_face_orientation
            break

class FaceOrientationToggle_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.face_orientation_toggle"
    bl_label = "Toggle Face Orientation"
    bl_description = "Toggles face orientation on and off (what where you expecting? Jeez)"

    def execute(self, context):
        toggle_face_orientation(context)
        return {"FINISHED"}