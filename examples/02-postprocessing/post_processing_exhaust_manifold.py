""".. _ref_post_processing_exhaust_manifold:

Post Processing using PyVista and Matplotlib: Exhaust Manifold
----------------------------------------------
This example demonstrates the postprocessing capabilities of PyFluent
(using PyVista and Matplotlib) using a 3D model
of an exhaust manifold with high temperature flows passing through.
The flow through the manifold is turbulent and
involves conjugate heat transfer.

This example demonstrates how to do the following:

- Create surfaces for the display of 3D data.

- Display filled contours of temperature on several surfaces.

- Display velocity vectors.

- Plot quantitative results using Matplotlib

"""
###############################################################################
# Import the PyFluent Module

import ansys.fluent.core as pyfluent

###############################################################################
# Import the PyVista-based graphics module

from ansys.fluent.post.pyvista import Graphics

###############################################################################
# Import matplotlib plotting module
# Unable to import as affected by Issue 290
# from ansys.fluent.post.matplotlib import Plots

###############################################################################
# Import the examples module needed for case

from ansys.fluent.core import examples

###############################################################################
# First, download the case and data file and start Fluent as a service with
# Meshing mode, double precision, number of processors: 4

import_case = examples.download_file(
    "manifold_solution.cas.h5", "pyfluent/exhaust_manifold"
)

import_data = examples.download_file(
    "manifold_solution.dat.h5", "pyfluent/exhaust_manifold"
)
session = pyfluent.launch_fluent(precision="double", processor_count=4)
root = session.get_settings_root()

session.tui.solver.file.read_case(case_file_name=import_case)
session.tui.solver.file.read_data(case_file_name=import_data)

###############################################################################
# Get the graphics object for mesh display

gs_1 = Graphics(session)

###############################################################################
# Create a graphics object for mesh display

mesh1 = gs_1.Meshes["mesh-1"]

###############################################################################
# Show edges and faces

mesh1.show_edges = True
mesh1.show_faces = True

###############################################################################
# Get the surfaces list

mesh1.surfaces_list = [
    "in1",
    "in2",
    "in3",
    "out1",
    "solid_up:1",
    "solid_up:1:830",
    "solid_up:1:830-shadow",
]
mesh1.display("window-1")

###############################################################################
# Disable edges and display again

mesh1.show_edges = False
mesh1.display("window-2")

###############################################################################
# Create iso-surface on the outlet plane

surf_outlet_plane = gs_1.Surfaces["outlet-plane"]
surf_outlet_plane.surface.type = "iso-surface"
iso_surf1 = surf_outlet_plane.surface.iso_surface
iso_surf1.field = "y-coordinate"
iso_surf1.iso_value = -0.125017
surf_outlet_plane.display("window-3")

###############################################################################
# Create iso-surface on the mid-plane (Issue # 276)

surf_mid_plane_x = gs_1.Surfaces["mid-plane-x"]
surf_mid_plane_x.surface.type = "iso-surface"
iso_surf2 = surf_mid_plane_x.surface.iso_surface
iso_surf2.field = "x-coordinate"
iso_surf2.iso_value = -0.174
surf_mid_plane_x.display("window-4")

###############################################################################
# Temperature contour on the mid-plane and the outlet

local_surfaces_provider = Graphics(session=None).Surfaces
contour_temp = gs_1.Contours["contour-temperature"]
contour_temp.field = "temperature"
contour_temp.surfaces_list = ["mid-plane-x", "outlet-plane"]
contour_temp.display("window-4")

###############################################################################
# Contour plot of temperature on the manifold

contour_temp_manifold = gs_1.Contours["contour-temperature-manifold"]
contour_temp_manifold.field = "temperature"
contour_temp_manifold.surfaces_list = [
    "in1",
    "in2",
    "in3",
    "out1",
    "solid_up:1",
    "solid_up:1:830",
]
contour_temp_manifold.display("window-5")

###############################################################################
# Vector on the mid-plane
# Currently using outlet-plane since mid-plane is affected by Issue # 276

velocity_vector = gs_1.Vectors["velocity-vector"]
velocity_vector.surfaces_list = ["outlet-plane"]
velocity_vector.scale = 1
velocity_vector.display("window-6")

###############################################################################
# Commenting out due to issue #290
# Start the Plot Object for the session
# plots_session_1 = Plots(session)

###############################################################################
# Create a default XY-Plot
# plot_1 = plots_session_1.XYPlots["plot-1"]

###############################################################################
# Set the surface on which the plot is plotted and the Y-axis function
# plot_1.surfaces_list = ["outlet"]
# plot_1.y_axis_function = "temperature"

###############################################################################
# Plot the created XY-Plot
# plot_1.plot("window-7")