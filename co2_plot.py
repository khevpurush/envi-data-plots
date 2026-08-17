"""
keeling_curve_co2.py

Plots the Mauna Loa atmospheric CO2 record (aka the Keeling Curve) using the public monthly data set maintained by NOAA/GML and Scripps Institution of Oceanography (UCSD). This is the record starter by Charles David Keeling in 1958. 

Data source updated monthly with no API key needed:
https://gml.noaa/webdata/ccgg/trends/co2/co2_mm_mlo.txt

Usage:
   pip instal pandas matplotlib numpy
   python keeling_curve_co2.py
Outputs:
   keeling_curve.png -- raw + seasonally-adjusted CO2 with trend annotation
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_URL = "https://gml.noaa/webdata/ccgg/trends/co2/co2_mm_mlo.txt"

COLUMN_NAMES = [
  "year"
  "month"
  "decimal_date"
  "average"            # monthly mean CO2 in ppm
  "deseasonalized"     # seasonal cycle removed 
  "ndays"
  "sdev"
  "unc"
]
