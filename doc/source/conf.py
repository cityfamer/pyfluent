"""Sphinx documentation configuration file."""
from datetime import datetime
import os
import subprocess
import sys

import numpy as np
from pyansys_sphinx_theme import pyansys_logo_black
import pyvista
from sphinx_gallery.sorting import FileNameSortKey

from ansys.fluent.core import __version__

# Manage errors
pyvista.set_error_output_file("errors.txt")

# Ensure that offscreen rendering is used for docs generation
pyvista.OFF_SCREEN = True

# must be less than or equal to the XVFB window size
pyvista.rcParams["window_size"] = np.array([1024, 768])

# Save figures in specified directory
pyvista.FIGURE_PATH = os.path.join(
    os.path.abspath("./images/"), "auto-generated/"
)
if not os.path.exists(pyvista.FIGURE_PATH):
    os.makedirs(pyvista.FIGURE_PATH)

# necessary when building the sphinx gallery
pyvista.BUILDING_GALLERY = True

# -- Project information -----------------------------------------------------

project = "ansys.fluent.core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS Inc."

# The short X.Y version
release = version = __version__

# -- General configuration ---------------------------------------------------
extensions = [
    "jupyter_sphinx",
    "notfound.extension",
    "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
    "sphinxemoji.sphinxemoji",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "numpy": ("https://numpy.org/devdocs", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    "pyvista": ("https://docs.pyvista.org/", None),
}

# SS01, SS02, SS03, GL08 all need clean up in the code to be reactivated.
# numpydoc configuration
numpydoc_use_plots = True
numpydoc_show_class_members = False
numpydoc_xref_param_type = True
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    "SS03",  # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Copy button customization ---------------------------------------------------
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True


_THIS_DIR = os.path.dirname(__file__)
_START_FLUENT_FILE = os.path.normpath(
    os.path.join(_THIS_DIR, "..", "..", ".ci", "start_fluent.py")
)
_STOP_FLUENT_FILE = os.path.normpath(
    os.path.join(_THIS_DIR, "..", "..", ".ci", "stop_fluent.py")
)


def _start_or_stop_fluent_container(gallery_conf, fname, when):
    start_instance = bool(int(os.getenv("PYFLUENT_START_INSTANCE", "1")))
    if not start_instance:
        if when == "before":
            if fname in [
                "mixing_elbow.py",
            ]:
                args = ["3ddp", "-t2", "-meshing"]
            elif fname in [
                "exhaust_system.py",
            ]:
                args = ["3ddp", "-t2", "-meshing"]
            elif fname in [
                "parametric_static_mixer_1.py",
                "parametric_static_mixer_2.py",
                "parametric_static_mixer_3.py",
            ]:
                args = ["3ddp", "-t2"]
            subprocess.run([sys.executable, _START_FLUENT_FILE] + args)
        elif when == "after":
            subprocess.run([sys.executable, _STOP_FLUENT_FILE])


# -- Sphinx Gallery Options ---------------------------------------------------
sphinx_gallery_conf = {
    # convert rst to md for ipynb
    # "pypandoc": True,
    # path to your examples scripts
    "examples_dirs": ["../../examples/"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Patter to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # Modules for which function level galleries are created.  In
    "doc_module": "ansys-fluent-core",
    "image_scrapers": ("pyvista", "matplotlib"),
    "ignore_pattern": "flycheck*",
    "thumbnail_size": (350, 350),
    "reset_modules_order": "both",
    "reset_modules": (_start_or_stop_fluent_container),
}


# -- Options for HTML output -------------------------------------------------
html_short_title = html_title = "PyFluent"
html_theme = "pyansys_sphinx_theme"
html_logo = pyansys_logo_black
html_theme_options = {
    "github_url": "https://github.com/pyansys/pyfluent",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "pyfluentdoc"


# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        f"pyfluent-Documentation-{__version__}.tex",
        "ansys.fluent.core Documentation",
        author,
        "manual",
    ),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "ansys.fluent.core",
        "ansys.fluent.core Documentation",
        [author],
        1,
    )
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "ansys.fluent.core",
        "ansys.fluent.core Documentation",
        author,
        "ansys.fluent.core",
        "Pythonic interface for Fluent using gRPC",
        "Engineering Software",
    ),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]
