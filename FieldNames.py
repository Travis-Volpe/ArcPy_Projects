# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:47:04 2019

@author: tvolpe
"""

import arcpy
from arcpy import env

#Set envrionment variables / the file path of the project folder
env.workspace = r'E:/SurvivalStudy/Final_SS_Data'

################################################################################
#Export the fields names of the compontent data sets
fc1 = r'E:/SurvivalStudy/Final_SS_Data/All_Years_2018M_wCondition.shp'
fields1 = arcpy.ListFields(fc1)
file =  open(r'E:/SurvivalStudy/DataReclamation/Tabular/MergeFields2.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields1:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()