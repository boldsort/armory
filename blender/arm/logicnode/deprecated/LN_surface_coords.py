from arm.logicnode.arm_nodes import *


@deprecated('Get Touch Movement', 'Get Touch Location')
class SurfaceCoordsNode(ArmLogicTreeNode):
    """Deprecated. Is recommended to use 'Get Touch Location' and 'Get Touch Movement' node instead."""
    bl_idname = 'LNSurfaceCoordsNode'
    bl_label = 'Surface Coords'
    bl_description = "Please use the \"Get Touch Movement\" and \"Get Touch Location\" nodes instead"
    arm_category = 'Input'
    arm_section = 'surface'
    arm_is_obsolete = 'is_obsolete'
    arm_version = 2

    def init(self, context):
        super(SurfaceCoordsNode, self).init(context)
        self.add_output('NodeSocketVector', 'Coords')
        self.add_output('NodeSocketVector', 'Movement')
