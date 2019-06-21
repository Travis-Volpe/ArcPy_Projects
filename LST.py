# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# LST.py
# Created on: 2019-04-22 10:34:24.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: LST <NDVI> <NDVImin> <NDVImax> <BAND_10> <RADIANCE_ADD_BAND_10> <RADIANCE_MULT_BAND_10> <RADIANCE_MULT_BAND_11> <RADIANCE_ADD_BAND_11> <BAND_11> <K1_CONSTANT_BAND_11> <K2_CONSTANT_BAND_11> <K1_CONSTANT_BAND_10> <K2_CONSTANT_BAND_10> <LST_Output> 
# Description: 
# To find land surface temperature.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
NDVI = arcpy.GetParameterAsText(0)

NDVImin = arcpy.GetParameterAsText(1)

NDVImax = arcpy.GetParameterAsText(2)

BAND_10 = arcpy.GetParameterAsText(3)

RADIANCE_ADD_BAND_10 = arcpy.GetParameterAsText(4)

RADIANCE_MULT_BAND_10 = arcpy.GetParameterAsText(5)

RADIANCE_MULT_BAND_11 = arcpy.GetParameterAsText(6)

RADIANCE_ADD_BAND_11 = arcpy.GetParameterAsText(7)

BAND_11 = arcpy.GetParameterAsText(8)

K1_CONSTANT_BAND_11 = arcpy.GetParameterAsText(9)

K2_CONSTANT_BAND_11 = arcpy.GetParameterAsText(10)

K1_CONSTANT_BAND_10 = arcpy.GetParameterAsText(11)

K2_CONSTANT_BAND_10 = arcpy.GetParameterAsText(12)

LST_Output = arcpy.GetParameterAsText(13)
if LST_Output == '#' or not LST_Output:
    LST_Output = "C:\\Users\\tvolpe\\Documents\\ArcGIS\\Default.gdb\\CellSta_LST11" # provide a default value if unspecified

# Local variables:
RAD10 = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\RAD10"
T10 = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\T10"
Pv = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\Pv"
e = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\e"
LST10 = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\LST10"
RAD11 = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\RAD11"
T11 = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\T11"
LST11 = "E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\LST11"

# Process: Raster Calculator (3)
arcpy.gp.RasterCalculator_sa("float(%RADIANCE_MULT_BAND_10%) * \"%BAND 10%\" + float(%RADIANCE_ADD_BAND_10%)", RAD10)

# Process: Raster Calculator (5)
arcpy.gp.RasterCalculator_sa("(float(%K2_CONSTANT_BAND_10%) / Ln((float(%K1_CONSTANT_BAND_10%) / \"%RAD10%\") + 1)) - 272.15", T10)

# Process: Raster Calculator
arcpy.gp.RasterCalculator_sa("Square((\"%NDVI%\" - float(%NDVImin%)) / (float(%NDVImax%) - float(%NDVImin%)))", Pv)

# Process: Raster Calculator (2)
arcpy.gp.RasterCalculator_sa("0.004 * \"%Pv%\" + 0.986", e)

# Process: Raster Calculator (7)
arcpy.gp.RasterCalculator_sa("\"%T10%\" / 1 + (\"%BAND 10%\" * \"%T10%\" / 14380) * Ln(\"%e%\")", LST10)

# Process: Raster Calculator (4)
arcpy.gp.RasterCalculator_sa("float(%RADIANCE_MULT_BAND_11%) * \"%BAND 11%\" + float(%RADIANCE_ADD_BAND_11%)", RAD11)

# Process: Raster Calculator (6)
arcpy.gp.RasterCalculator_sa("(float(%K2_CONSTANT_BAND_11%) / Ln((float(%K1_CONSTANT_BAND_11%) / \"%RAD11%\") + 1)) - 272.15", T11)

# Process: Raster Calculator (8)
arcpy.gp.RasterCalculator_sa("\"%T11%\" / 1 + (\"%BAND 11%\" * \"%T11%\" / 14380) * Ln(\"%e%\")", LST11)

# Process: Cell Statistics
arcpy.gp.CellStatistics_sa("E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\LST10;E:\\Remote_Sensing\\LandSurfaceTemperature\\Land_Surface_Temperature_Model\\LST11", LST_Output, "MEAN", "DATA")

