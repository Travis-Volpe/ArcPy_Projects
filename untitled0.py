# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:19:43 2019

@author: tvolpe
"""

import arcpy

arcpy.env.workspace = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV'

fc = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV/2015_2018_Park_INV/test_data.shp'

fields = ['Scientific']

values = [row[0] for row in arcpy.da.SearchCursor(fc, fields)]
uniqueValues = set(values)

print(uniqueValues)

#with arcpy.da.SearchCursor(fc, fields) as cursor:
#    for row in cursor:
#        print(u'{0}, {1}'.format(row[0], row[1]))
        