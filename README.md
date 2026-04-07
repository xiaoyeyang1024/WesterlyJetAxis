# WesterlyJetAxis
code and data for "WesterlyJetAxis"

Overview

This Python script calculates and visualizes the latitude of the westerly jet axis based on 200 hPa summer wind speed data. It includes:

Morphological smoothing of wind speed data using closing and opening operations.Detection of the westerly jet axis by finding the maximum wind speed along longitudes and limiting abrupt latitude jumps.Remove small-scale disturbances.Visualization of both wind speed and the jet axis .Requirements

The following Python packages are required:

numpy

xarray

scipy

matplotlib

cartopy
