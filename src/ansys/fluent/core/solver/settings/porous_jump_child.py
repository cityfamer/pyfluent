#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from .adhesion_angle import adhesion_angle
from .adhesion_constrained import adhesion_constrained
from .alpha import alpha
from .c2 import c2
from .dm import dm
from .dpm_bc_collision_partner import dpm_bc_collision_partner
from .dpm_bc_type import dpm_bc_type
from .dpm_bc_udf import dpm_bc_udf
from .geom_bgthread import geom_bgthread
from .geom_dir_spec import geom_dir_spec
from .geom_dir_x import geom_dir_x
from .geom_dir_y import geom_dir_y
from .geom_dir_z import geom_dir_z
from .geom_disable import geom_disable
from .geom_levels import geom_levels
from .ir_absp import ir_absp
from .ir_trans import ir_trans
from .jump_adhesion import jump_adhesion
from .phase_15 import phase
from .porous_jump_turb_wall_treatment import porous_jump_turb_wall_treatment
from .reinj_inj import reinj_inj
from .solar_fluxes import solar_fluxes
from .strength import strength
from .thermal_ctk import thermal_ctk
from .v_absp import v_absp
from .v_trans import v_trans
from .x_displacement_type import x_displacement_type
from .x_displacement_value import x_displacement_value
from .y_displacement_type import y_displacement_type
from .y_displacement_value import y_displacement_value
from .z_displacement_type import z_displacement_type
from .z_displacement_value import z_displacement_value


class porous_jump_child(Group):
    """'child_object_type' of porous_jump."""

    fluent_name = "child-object-type"

    child_names = [
        "phase",
        "geom_disable",
        "geom_dir_spec",
        "geom_dir_x",
        "geom_dir_y",
        "geom_dir_z",
        "geom_levels",
        "geom_bgthread",
        "porous_jump_turb_wall_treatment",
        "alpha",
        "dm",
        "c2",
        "thermal_ctk",
        "solar_fluxes",
        "v_absp",
        "ir_absp",
        "ir_trans",
        "v_trans",
        "dpm_bc_type",
        "dpm_bc_collision_partner",
        "reinj_inj",
        "dpm_bc_udf",
        "strength",
        "jump_adhesion",
        "adhesion_constrained",
        "adhesion_angle",
        "x_displacement_type",
        "x_displacement_value",
        "y_displacement_type",
        "y_displacement_value",
        "z_displacement_type",
        "z_displacement_value",
    ]

    phase: phase = phase
    """
    phase child of porous_jump_child
    """
    geom_disable: geom_disable = geom_disable
    """
    geom_disable child of porous_jump_child
    """
    geom_dir_spec: geom_dir_spec = geom_dir_spec
    """
    geom_dir_spec child of porous_jump_child
    """
    geom_dir_x: geom_dir_x = geom_dir_x
    """
    geom_dir_x child of porous_jump_child
    """
    geom_dir_y: geom_dir_y = geom_dir_y
    """
    geom_dir_y child of porous_jump_child
    """
    geom_dir_z: geom_dir_z = geom_dir_z
    """
    geom_dir_z child of porous_jump_child
    """
    geom_levels: geom_levels = geom_levels
    """
    geom_levels child of porous_jump_child
    """
    geom_bgthread: geom_bgthread = geom_bgthread
    """
    geom_bgthread child of porous_jump_child
    """
    porous_jump_turb_wall_treatment: porous_jump_turb_wall_treatment = (
        porous_jump_turb_wall_treatment
    )
    """
    porous_jump_turb_wall_treatment child of porous_jump_child
    """
    alpha: alpha = alpha
    """
    alpha child of porous_jump_child
    """
    dm: dm = dm
    """
    dm child of porous_jump_child
    """
    c2: c2 = c2
    """
    c2 child of porous_jump_child
    """
    thermal_ctk: thermal_ctk = thermal_ctk
    """
    thermal_ctk child of porous_jump_child
    """
    solar_fluxes: solar_fluxes = solar_fluxes
    """
    solar_fluxes child of porous_jump_child
    """
    v_absp: v_absp = v_absp
    """
    v_absp child of porous_jump_child
    """
    ir_absp: ir_absp = ir_absp
    """
    ir_absp child of porous_jump_child
    """
    ir_trans: ir_trans = ir_trans
    """
    ir_trans child of porous_jump_child
    """
    v_trans: v_trans = v_trans
    """
    v_trans child of porous_jump_child
    """
    dpm_bc_type: dpm_bc_type = dpm_bc_type
    """
    dpm_bc_type child of porous_jump_child
    """
    dpm_bc_collision_partner: dpm_bc_collision_partner = (
        dpm_bc_collision_partner
    )
    """
    dpm_bc_collision_partner child of porous_jump_child
    """
    reinj_inj: reinj_inj = reinj_inj
    """
    reinj_inj child of porous_jump_child
    """
    dpm_bc_udf: dpm_bc_udf = dpm_bc_udf
    """
    dpm_bc_udf child of porous_jump_child
    """
    strength: strength = strength
    """
    strength child of porous_jump_child
    """
    jump_adhesion: jump_adhesion = jump_adhesion
    """
    jump_adhesion child of porous_jump_child
    """
    adhesion_constrained: adhesion_constrained = adhesion_constrained
    """
    adhesion_constrained child of porous_jump_child
    """
    adhesion_angle: adhesion_angle = adhesion_angle
    """
    adhesion_angle child of porous_jump_child
    """
    x_displacement_type: x_displacement_type = x_displacement_type
    """
    x_displacement_type child of porous_jump_child
    """
    x_displacement_value: x_displacement_value = x_displacement_value
    """
    x_displacement_value child of porous_jump_child
    """
    y_displacement_type: y_displacement_type = y_displacement_type
    """
    y_displacement_type child of porous_jump_child
    """
    y_displacement_value: y_displacement_value = y_displacement_value
    """
    y_displacement_value child of porous_jump_child
    """
    z_displacement_type: z_displacement_type = z_displacement_type
    """
    z_displacement_type child of porous_jump_child
    """
    z_displacement_value: z_displacement_value = z_displacement_value
    """
    z_displacement_value child of porous_jump_child
    """