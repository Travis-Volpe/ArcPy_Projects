# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:28:08 2019

@author: tvolpe
"""

import arcpy

arcpy.env.workspace = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV'

fc = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV/2015_2018_Park_INV/test_data.shp'

#fields = ['Scientific', 'CommonName']

rows = arcpy.SearchCursor(fc, fields="Scientific")
for row in rows:
    print("{0}".format(
            row.getValue("Scientific")))
#            row.getValue("CommonName")))
