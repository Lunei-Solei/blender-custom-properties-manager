﻿# This file defines all constants used to help avoid "magic strings" and
# other types of magic.
from collections import namedtuple

# Configuration
DEBUG = False
PROP_TYPE_LABEL = "Type"
PROP_TYPE_PROP = "property_type"
DEFAULT_VALUE_LABEL = "Default"
ALIGN_RIGHT = 'RIGHT'

# Default property values
DEFAULT_FLOAT_PROP = "default_float"
DEFAULT_FLOAT_ARRAY_PROP = "default_float_array"
DEFAULT_INT_PROP = "default_int"
DEFAULT_INT_ARRAY_PROP = "default_int_array"
DEFAULT_BOOL_PROP = "default_bool"
DEFAULT_BOOL_ARRAY_PROP = "default_bool_array"
DEFAULT_STRING_PROP = "default_string"
DEFAULT_DATA_BLOCK_PROP = "default_data_block"
DEFAULT_PYTHON_PROP = "default_python"

# RNA
RNA_CUSTOM_PROPERTY_TYPE_ITEMS = (
    ('FLOAT', "Float", "A single floating-point value"),
    ('FLOAT_ARRAY', "Float Array", "An array of floating-point values"),
    ('INT', "Integer", "A single integer"),
    ('INT_ARRAY', "Integer Array", "An array of integers"),
    ('BOOL', "Boolean", "A true or false value"),
    ('BOOL_ARRAY', "Boolean Array", "An array of true or false values"),
    ('STRING', "String", "A string value"),
    ('DATA_BLOCK', "Data-Block", "A data-block value"),
    ('PYTHON', "Python", "Edit a Python value directly, for unsupported property types"),
)
RNA_DEFAULT_VALUE_ITEMS = ['FLOAT', 'INT', 'BOOL', 'STRING']

# Window Manager Operators
WM_PROPERTIES_ADD = "wm.properties_add"
WM_PROPERTIES_REMOVE = "wm.properties_remove"
WM_PROPERTIES_EDIT = "wm.properties_edit"

# Icons
ADD_ICON = 'ADD'
PREFERENCES_ICON = 'PREFERENCES'
DOWNARROW_HLT_ICON = 'DOWNARROW_HLT'
RIGHTARROW_ICON = 'RIGHTARROW'
X_ICON = 'X'
FILE_REFRESH_ICON = 'FILE_REFRESH'

# CPM Operators
CPM_EXPAND_TOGGLE_OP = "cpm.expand_toggle"
CPM_ADD_NEW_PROPERTY_GROUP_OP = "cpm.add_new_property_group"
CPM_ADD_NEW_PROPERTY_OP = "cpm.add_new_property"
CPM_EDIT_PROPERTY_OP = "cpm.edit_property"
CPM_RESET_PROPERTY_OP = "cpm.reset_property"
CPM_REMOVE_PROPERTY_OP = "cpm.remove_property"
CPM_EDIT_PROPERTY_GROUP_NAME_OP = "cpm.edit_property_group_name"

# CPM Menus
CPM_EDIT_PROPERTY_MENU = "CPM_MT_edit_property"

# Attributes
ATTR_KEYS = 'keys'

# Panels
Panel = namedtuple("Panel", ["name", "data_path"])
panels = [
    Panel("VIEWLAYER_PT_layer_custom_props", "view_layer"),
    Panel("SCENE_PT_custom_props", "scene"),
    Panel("OBJECT_PT_custom_props", "active_object"),
    Panel("DATA_PT_custom_props_light", "active_object.data"),
]

# Misc.
CPM_GROUP_DATA = "_cpm_group_data"
CPM_SERIALIZED_GROUP_DATA = "_cpm_serialized_group_data"
CPM_DEFAULT_GROUP_DATA = "{}"