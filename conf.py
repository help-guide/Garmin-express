# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add project-specific modules if needed
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Garmin Express Setup Guide'
copyright = '2025, Garmin'
author = 'Garmin'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = []

# Paths that contain templates
templates_path = ['_templates']

# List of patterns, relative to source directory, to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output options -----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Set Up Garmin Express – Garmin.com/express"

# Optional short title (used in navigation bar)
html_short_title = "Garmin Express Setup"

# Favicon
html_favicon = 'favicon.ico'

# Choose a theme (you can uncomment and install sphinx_rtd_theme if needed)
# html_theme = 'sphinx_rtd_theme'

# Hide the "View page source" link
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths for static files (CSS, JS, images, etc.)
# html_static_path = ['_static']  # Uncomment if you have custom assets
