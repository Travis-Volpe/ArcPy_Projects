# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:14:38 2019

@author: tvolpe
"""

import arcpy

arcpy.env.workspace = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV'

fc = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV/2015_2018_Park_INV/test_data.shp'

indexes = arcpy.ListIndexes(fc)
for index in indexes:
    print("Name        : {0}".format(index.name))
    print("IsAscending : {0}".format(index.isAscending))
    print("IsUnique    : {0}".format(index.isUnique))