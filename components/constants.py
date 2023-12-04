import os
import sys

var_garmenttypes = {
    'var_head': "UnionAvatars_Head",
    'var_body': "UnionAvatars_Body",
    'var_top': "UnionAvatars_Top",
    'var_bottom': "UnionAvatars_Bottom",
    'var_shoes': "UnionAvatars_Shoes",
    'var_acs': "UnionAvatars_Acs",
}

var_bodyparts = {
    'var_head': "UnionAvatars_Head",
    'var_neck': "UnionAvatars_Neck",
    'var_hands': "UnionAvatars_Hands",
    'var_armsBottom': "UnionAvatars_Arms_bottom",
    'var_armsTop': "UnionAvatars_Arms_top",
    'var_chest': "UnionAvatars_Chest",
    'var_belly': "UnionAvatars_Belly",
    'var_hips': "UnionAvatars_Hips",
    'var_legsTop': "UnionAvatars_Legs_top",
    'var_legsBottom': "UnionAvatars_Legs_bottom",
    'var_feet': "UnionAvatars_Feet",
    
}

var_forbiddentextures = ["Metallic","Roughness"]

FEMALE_BODY_PATH = "v4_phr_female_UA_base.blend"
MALE_BODY_PATH = "v4_phr_male_UA_base.blend"

OUTFIT_TRIANGLE_LIMIT = 15000  # acceptable max value

ACCESSORIES_TRIANGLE_LIMIT = 4000  # acceptable max value
TOP_TRIANGLE_LIMIT = 5000  # acceptable max value
BOTTOM_TRIANGLE_LIMIT = 3000  # acceptable max value
SHOES_TRIANGLE_LIMIT = 4000  # acceptable max value

MAX_TEXTURE_SIZE = 200  # kbytes

POSES_PATH = "Addon_Poses.blend"

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)