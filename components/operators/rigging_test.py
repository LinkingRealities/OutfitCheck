""" Export main poses """
import bpy
import os

from components.constants import ROOT_DIR
from components.constants import POSES_PATH

def load_poses():

    try:
        bpy.data.actions["A Pose"]
    except:
        bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", POSES_PATH, "Action"),
                          files=[{"name": "A Pose"}])
    
    try:
        bpy.data.actions["Dancing Left"]
    except:
        bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", POSES_PATH, "Action"),
                          files=[{"name": "Dancing Left"}])

    try:
        bpy.data.actions["Dancing Right"]
    except:
        bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", POSES_PATH, "Action"),
                          files=[{"name": "Dancing Right"}])

    try:
        bpy.data.actions["Walking Left"] 
    except:
        bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", POSES_PATH, "Action"),
                          files=[{"name": "Walking Left"}])

    try:
        bpy.data.actions["Walking Right"] 
    except:    
        bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", POSES_PATH, "Action"),
                          files=[{"name": "Walking Right"}])

    try:
        bpy.data.actions["T Pose"]
    except:    
        bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", POSES_PATH, "Action"),
                          files=[{"name": "T Pose"}])
        
    try:
        bpy.data.actions["Rest Pose"]
    except:    
        bpy.ops.wm.append(directory=os.path.join(ROOT_DIR, "assets", POSES_PATH, "Action"),
                          files=[{"name": "Rest Pose"}])


class RiggingTest_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rigging_test"
    bl_label = "Import main poses library"
    bl_description = "Import pose library"

    def execute(self, context):
        try:
            load_poses()
            self.report({"INFO"}, "Pose library imported correctly")
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")
        return {"FINISHED"}

class DefaultPose_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.default_pose"
    bl_label = "A Pose (Default)"
    bl_description = "Default Pose"
    def execute(self, context):
        
        try:
            load_poses()
            ob = bpy.data.objects['Armature']

            action = bpy.data.actions["A Pose"]
            
            # Create the animation data if it doesn't exist
            if not ob.animation_data:
                ob.animation_data_create()
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")

        try:
            # Set the active action
            ob.animation_data.action = action
            bpy.ops.object.posemode_toggle()
            ob.animation_data_clear()
            for action in bpy.data.actions: bpy.data.actions.remove(action)
        except:
            self.report({"ERROR"}, "ERROR: Delete action assigned to armature before changing pose")

        return {"FINISHED"}

class DancingLeftPose_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.dancingleft_pose"
    bl_label = "Dancing Pose (left)"
    bl_description = "Dancing Pose"
    def execute(self, context):
        
        try:
            load_poses()
            ob = bpy.data.objects['Armature']

            action = bpy.data.actions["Dancing Left"]
            
            # Create the animation data if it doesn't exist
            if not ob.animation_data:
                ob.animation_data_create()
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")

        try:
            # Set the active action
            ob.animation_data.action = action
            bpy.ops.object.posemode_toggle()
            ob.animation_data_clear()
            for action in bpy.data.actions: bpy.data.actions.remove(action)
        except:
            self.report({"ERROR"}, "ERROR: Delete action assigned to armature before changing pose")
        return {"FINISHED"}
        
class DancingRightPose_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.dancingright_pose"
    bl_label = "Dancing Pose (right)"
    bl_description = "Dancing Pose"
    def execute(self, context):
        
        try:
            load_poses()
            ob = bpy.data.objects['Armature']

            action = bpy.data.actions["Dancing Right"]
            
            # Create the animation data if it doesn't exist
            if not ob.animation_data:
                ob.animation_data_create()
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")

        try:
            # Set the active action
            ob.animation_data.action = action
            bpy.ops.object.posemode_toggle()
            ob.animation_data_clear()
            for action in bpy.data.actions: bpy.data.actions.remove(action)
        except:
            self.report({"ERROR"}, "ERROR: Unlink animation assigned to armature before changing pose")
        return {"FINISHED"}
        
class WalkingLeftPose_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.walkingleft_pose"
    bl_label = "Walking Pose (left)"
    bl_description = "Walking Pose"
    def execute(self, context):
        
        try:
            load_poses()
            ob = bpy.data.objects['Armature']

            action = bpy.data.actions["Walking Left"]
            
            # Create the animation data if it doesn't exist
            if not ob.animation_data:
                ob.animation_data_create()
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")

        try:
            # Set the active action
            ob.animation_data.action = action
            bpy.ops.object.posemode_toggle()
            ob.animation_data_clear()
            for action in bpy.data.actions: bpy.data.actions.remove(action)
        except:
            self.report({"ERROR"}, "ERROR: Unlink animation assigned to armature before changing pose")
        return {"FINISHED"}

class WalkingRightPose_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.walkingright_pose"
    bl_label = "Walking Pose (right)"
    bl_description = "Walking Pose"
    def execute(self, context):
        
        try:
            load_poses()
            ob = bpy.data.objects['Armature']

            action = bpy.data.actions["Walking Right"]
            
            # Create the animation data if it doesn't exist
            if not ob.animation_data:
                ob.animation_data_create()
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")

        try:
            # Set the active action
            ob.animation_data.action = action
            bpy.ops.object.posemode_toggle()
            ob.animation_data_clear()
            for action in bpy.data.actions: bpy.data.actions.remove(action)
        except:
            self.report({"ERROR"}, "ERROR: Unlink animation assigned to armature before changing pose")
        return {"FINISHED"}
    
class TPose_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.t_pose"
    bl_label = "T Pose"
    bl_description = "Standard T pose"
    def execute(self, context):
        
        try:
            load_poses()
            ob = bpy.data.objects['Armature']
            print("Armature loaded")
            action = bpy.data.actions["T Pose"]
            print("Pose loaded")
            # Create the animation data if it doesn't exist
            if not ob.animation_data:
                ob.animation_data_create()
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")

        try:
            # Set the active action
            ob.animation_data.action = action
            bpy.ops.object.posemode_toggle()
            ob.animation_data_clear()
            for action in bpy.data.actions: bpy.data.actions.remove(action)
        except:
            self.report({"ERROR"}, "ERROR: Unlink animation assigned to armature before changing pose")
        return {"FINISHED"}
    
class RestPose_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rest_pose"
    bl_label = "Rest Pose"
    bl_description = "Rest pose"
    def execute(self, context):
        
        try:
            load_poses()
            ob = bpy.data.objects['Armature']

            action = bpy.data.actions["Rest Pose"]
            
            # Create the animation data if it doesn't exist
            if not ob.animation_data:
                ob.animation_data_create()
        except:
            self.report({"ERROR"}, "ERROR: Pose library was not imported")

        try:
            # Set the active action
            ob.animation_data.action = action
            bpy.ops.object.posemode_toggle()
            ob.animation_data_clear()
            for action in bpy.data.actions: bpy.data.actions.remove(action)
        except:
            self.report({"ERROR"}, "ERROR: Unlink animation assigned to armature before changing pose")
        return {"FINISHED"}