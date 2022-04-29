""".. _ref_mixing_elbow_settings_api:

Fluid Flow and Heat Transfer in a Mixing Elbow
----------------------------------------------
This example illustrates the setup and solution of a three-dimensional
turbulent fluid flow and heat transfer problem in a mixing elbow. The mixing
elbow configuration is encountered in piping systems in power plants and
process industries. It is often important to predict the flow field and
temperature field in the area of the mixing region in order to properly design
the junction.

This example demonstrates how to do the following:

- Launch Ansys Fluent.
- Read an existing mesh file into Ansys Fluent.
- Use mixed units to define the geometry and fluid properties.
- Set material properties and boundary conditions for a turbulent
  forced-convection problem.
- Create a surface report definition and use it as a convergence criterion.
- Calculate a solution using the pressure-based solver.
- Visually examine the flow and temperature fields using the postprocessing
  tools available in Ansys Fluent.

Problem Description:
A cold fluid at 20 deg C flows into the pipe through a large inlet, and mixes
with a warmer fluid at 40 deg C that enters through a smaller inlet located at
the elbow. The pipe dimensions are in inches and the fluid properties and
boundary conditions are given in SI units. The Reynolds number for the flow at
the larger inlet is 50, 800, so a turbulent flow model will be required.
"""


###############################################################################
# First, download the mesh file and start Fluent as a service with
# Solver Mode, Double Precision, Number of Processors 2

import ansys.fluent.core as pyfluent
from ansys.fluent.core import examples

import_filename = examples.download_file("mixing_elbow.msh.h5", "pyfluent/mixing_elbow")

session = pyfluent.launch_fluent(precision="double", processor_count=2)
session.tui.solver.file.read_case(import_filename)
###############################################################################
# Perform mesh check:
# The mesh check will list the minimum and maximum x, y, and z values from the
# mesh in the default SI unit of meters. It will also report a number of other
# mesh features that are checked. Any errors in the mesh will be reported at
# this time. Ensure that the minimum volume is not negative, since Ansys Fluent
# cannot begin a calculation when this is the case.

session.tui.solver.mesh.check()

###############################################################################
# The settings objects provide a natural way to access and modify settings.
# The top-level settings object for a session can be accessed with the
# get_settings_root() method of the session object.
# Enabling the settings objects.

root = session.get_settings_root()

###############################################################################
# Set the working units for the mesh:
# select "in" to set inches as the working unit for length. Note:  Because the
# default SI units will be used for everything except length, there is no need
# to change any other units in this problem. If you want a different working
# unit for length, other than inches (for example, millimeters), make the
# appropriate change.

session.tui.solver.define.units("length", "in")

###############################################################################
# Enable heat transfer by activating the energy equation.

root.setup.models.energy.enabled = True

###############################################################################
# Create a new material called water-liquid.

session.tui.solver.define.materials.copy("fluid", "water-liquid")

###############################################################################
# Set up the cell zone conditions for the fluid zone (elbow-fluid). Select
# water-liquid from the Material list.

session.tui.solver.define.boundary_conditions.fluid(
    "elbow-fluid",
    "yes",
    "water-liquid",
    "no",
    "no",
    "no",
    "no",
    "0",
    "no",
    "0",
    "no",
    "0",
    "no",
    "0",
    "no",
    "0",
    "no",
    "1",
    "no",
    "no",
    "no",
    "no",
    "no",
)

###############################################################################
# Set up the boundary conditions for the inlets, outlet, and walls for your CFD
# analysis.
# cold inlet (cold-inlet), Setting: Value:
# Velocity Specification Method: Magnitude, Normal to Boundary
# Velocity Magnitude: 0.4 [m/s]
# Specification Method: Intensity and Hydraulic Diameter
# Turbulent Intensity: 5 [%]
# Hydraulic Diameter: 4 [inch]
# Temperature: 293.15 [K]

root.setup.boundary_conditions.velocity_inlet["cold-inlet"].vmag = {
    "option": "constant or expression",
    "constant": 0.4,
}
root.setup.boundary_conditions.velocity_inlet[
    "cold-inlet"
].ke_spec = "Intensity and Hydraulic Diameter"
root.setup.boundary_conditions.velocity_inlet["cold-inlet"].turb_intensity = 5
root.setup.boundary_conditions.velocity_inlet[
    "cold-inlet"
].turb_hydraulic_diam = "4 [in]"
root.setup.boundary_conditions.velocity_inlet["cold-inlet"].t = {
    "option": "constant or expression",
    "constant": 293.15,
}

###############################################################################
# hot inlet (hot-inlet), Setting: Value:
# Velocity Specification Method: Magnitude, Normal to Boundary
# Velocity Magnitude: 1.2 [m/s]
# Specification Method: Intensity and Hydraulic Diameter
# Turbulent Intensity: 5 [%]
# Hydraulic Diameter: 1 [inch]
# Temperature: 313.15 [K]

root.setup.boundary_conditions.velocity_inlet["hot-inlet"].vmag = {
    "option": "constant or expression",
    "constant": 1.2,
}
root.setup.boundary_conditions.velocity_inlet[
    "hot-inlet"
].ke_spec = "Intensity and Hydraulic Diameter"
root.setup.boundary_conditions.velocity_inlet[
    "hot-inlet"
].turb_hydraulic_diam = "1 [in]"
root.setup.boundary_conditions.velocity_inlet["hot-inlet"].t = {
    "option": "constant or expression",
    "constant": 313.15,
}

###############################################################################
# pressure outlet (outlet), Setting: Value:
# Backflow Turbulent Intensity: 5 [%]
# Backflow Turbulent Viscosity Ratio: 4

root.setup.boundary_conditions.pressure_outlet["outlet"].turb_viscosity_ratio = 4

###############################################################################
# Enable the plotting of residuals during the calculation.

session.tui.solver.solve.monitors.residual.plot("yes")

###############################################################################
# Create a surface report definition of average temperature at the outlet
# (outlet) called outlet-temp-avg

root.solution.report_definitions.surface["outlet-temp-avg"] = {}
root.solution.report_definitions.surface[
    "outlet-temp-avg"
].report_type = "surface-massavg"
root.solution.report_definitions.surface["outlet-temp-avg"].field = "temperature"
root.solution.report_definitions.surface["outlet-temp-avg"].surface_names = ["outlet"]
root.solution.report_definitions.compute(report_defs=["outlet-temp-avg"])

###############################################################################
# Create a convergence condition for outlet-temp-avg:
# Provide con-outlet-temp-avg for Conditions. Select outlet-temp-avg Report
# Definition. Provide 1e-5 for Stop Criterion. Provide 20 for Ignore Iterations
# Before. Provide 15 for Use Iterations. Enable Print. Set Every Iteration to
# 3.
# These settings will cause Fluent to consider the solution converged when the
# surface report definition value for each of the previous 15 iterations is
# within 0.001% of the current value. Convergence of the values will be checked
# every 3 iterations. The first 20 iterations will be ignored, allowing for any
# initial solution dynamics to settle out. Note that the value printed to the
# console is the deviation between the current and previous iteration values
# only.
# Change Convergence Conditions

session.tui.solver.solve.convergence_conditions(
    "conv-reports",
    "add",
    "con-outlet-temp-avg",
    "initial-values-to-ignore",
    "20",
    "previous-values-to-consider",
    "15",
    "print?",
    "yes",
    "report-defs",
    "outlet-temp-avg",
    "stop-criterion",
    "1e-05",
    "quit",
    "quit",
    "condition",
    "1",
    "frequency",
    "3",
    "quit",
)
session.tui.solver.solve.convergence_conditions("frequency", "3", "quit")

###############################################################################
# Initialize the flow field using the Hybrid Initialization

session.tui.solver.solve.initialize.hyb_initialization()

###############################################################################
# Solve for 150 Iterations.

session.tui.solver.solve.iterate(150)

###############################################################################
# Save the case and data file (mixing_elbow1.cas.h5 and mixing_elbow1.dat.h5).
# session.tui.solver.file.write_case_data('mixing_elbow1.cas.h5')

###############################################################################
# Examine the mass flux report for convergence: Select cold-inlet, hot-inlet,
# and outlet from the Boundaries selection list.
# Compute a Mass Flux Report for convergence

root.solution.report_definitions.flux[
    "report_mfr"
] = {}  # Create a default report flux report
root.solution.report_definitions.flux["report_mfr"].zone_names = [
    "cold-inlet",
    "hot-inlet",
    "outlet",
]
root.solution.report_definitions.compute(report_defs=["report_mfr"])

###############################################################################
# Create and display a definition for velocity magnitude contours on the
# symmetry plane:
# Provide contour-vel for Contour Name. Select velocity magnitude. Select
# symmetry-xyplane from the Surfaces list. Display contour-vel contour.

root.results.graphics.contour["contour-vel"] = {}
root.results.graphics.contour["contour-vel"].print_state()
root.results.graphics.contour["contour-vel"].field = "velocity-magnitude"
root.results.graphics.contour["contour-vel"].surfaces_list = ["symmetry-xyplane"]
# root.results.graphics.contour["contour-vel"].display()

###############################################################################
# Create and display a definition for temperature contours on the symmetry
# plane:
# Provide contour-temp for Contour Name. Select temperature. Select
# symmetry-xyplane from the Surfaces list. Display contour-temp contour.

root.results.graphics.contour["contour-temp"] = {}
root.results.graphics.contour["contour-temp"].print_state()
root.results.graphics.contour["contour-temp"].field = "temperature"
root.results.graphics.contour["contour-temp"].surfaces_list = ["symmetry-xyplane"]
# root.results.graphics.contour["contour-temp"].display()

###############################################################################
# Create and display velocity vectors on the symmetry-xyplane plane:
# Provide vector-vel for Vector Name. Select arrow for the Style. Select
# symmetry-xyplane from the Surfaces selection list.
root.results.graphics.vector["vector-vel"] = {}
root.results.graphics.vector["vector-vel"].print_state()
root.results.graphics.vector["vector-vel"].field = "temperature"
root.results.graphics.vector["vector-vel"].surfaces_list = ["symmetry-xyplane"]
root.results.graphics.vector["vector-vel"].scale.scale_f = 4
root.results.graphics.vector["vector-vel"].style = "arrow"
# root.results.graphics.vector["vector-vel"].display()

###############################################################################
# Create an iso-surface representing the intersection of the plane z=0 and the
# surface outlet. Name: z=0_outlet

session.tui.solver.surface.iso_surface(
    "z-coordinate", "z=0_outlet", "outlet", "()", "()", "0", "()"
)

###############################################################################
# Create Contour on the iso-surface

root.results.graphics.contour["contour-z_0_outlet"] = {}
root.results.graphics.contour["contour-z_0_outlet"].print_state()
root.results.graphics.contour["contour-z_0_outlet"].field = "temperature"
root.results.graphics.contour["contour-z_0_outlet"].surfaces_list = ["z=0_outlet"]
# root.results.graphics.contour["contour-z_0_outlet"].display()

###############################################################################
# session.tui.solver.file.write_case_data("mixing_elbow1_set.cas.h5")
# Display and save an XY plot of the temperature profile across the centerline
# of the outlet for the initial solution

session.tui.solver.display.objects.create(
    "xy",
    "xy-outlet-temp",
    "y-axis-function",
    "temperature",
    "surfaces-list",
    "z=0_outlet",
    "()",
    "quit",
)

###############################################################################
# Write final case and data.
# session.tui.solver.file.write_case_data('mixing_elbow2_set.cas.h5')

###############################################################################
