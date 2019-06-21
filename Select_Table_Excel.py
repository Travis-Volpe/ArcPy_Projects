# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Select_Table_Excel.py
# Created on: 2018-05-17 14:15:28.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Tables = "D:\\WateringMaps\\Excel\\Tables"
v2018_Watering_Trees_Append = "2018_Watering_Trees_Append"
test1_1600Kenn_shp = "D:\\WateringMaps\\Models\\OFCs\\test1_1600Kenn.shp"
Table_test1a = test1_1600Kenn_shp
Table_test1a_xls = "D:\\WateringMaps\\Models\\Excel_Outputs\\Table_test1a.xls"

# Process: Select
arcpy.Select_analysis(v2018_Watering_Trees_Append, test1_1600Kenn_shp, "\"Location\" = '1600 Kennedy St. NW'")

# Process: Create Table
arcpy.CreateTable_management(Tables, "Table_test1a", "D:\\WateringMaps\\Models\\OFCs\\test1_1600Kenn.shp", "")

# Process: Table To Excel
arcpy.TableToExcel_conversion(Table_test1a, Table_test1a_xls, "NAME", "CODE")
