# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:22:46 2019

@author: tvolpe
"""

import arcpy

arcpy.env.workspace = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV'

fc = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV/2015_2018_Park_INV/test_data.shp'

field = 'Scientific'

values = [row[0] for row in arcpy.da.SearchCursor(fc, field)]
uniqueValues = set(values)

print(uniqueValues)
