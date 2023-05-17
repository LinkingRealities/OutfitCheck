"""PROPERTIES"""
import bpy


class Properties(bpy.types.PropertyGroup):
    commsCheck: bpy.props.BoolProperty(
        name="Comms",
        description="Specify if the scene is for comms",
        default=True
    )
    objectsEnum: bpy.props.EnumProperty(
        name="Options",
        description="Optional Objects",
        default="0",
        items=[("0", "None", ""),
               ("1", "Shoes", "")
               ]
    )
    shoesBool: bpy.props.BoolProperty(
        name="Shoes",
        description="Specify if the scene contains shoes",
        default=False
    )

    bottomBool: bpy.props.BoolProperty(
        name="Bottom",
        description="Specify if the scene contains a bottom object",
        default=True
    )
    acsBool: bpy.props.BoolProperty(
        name="Accessory",
        description="Specify if the scene contains an accesory object",
        default=False
    )

    decoyBool: bpy.props.BoolProperty(
        name="Cannot disable this property",
        description="",
        default=True
    )

    developerBool: bpy.props.BoolProperty(
        name="Developer options (This configuration is advanced and not mandatory)",
        description="",
        default=False
    )
    passwordString: bpy.props.StringProperty(name="")

