#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tvolpe
#
# Created:     11/05/2018
# Copyright:   (c) tvolpe 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# Name: MultipleRingBuffer_Example2.py
# Description: Create multiple buffers for the input features

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "D:\WateringMaps\CT_3015.gdb"

# Set local variables
inFeatures = "CaseyTrees_3015"
outFeatureClass = "D:\WateringMaps\Buffer\ct_3015_buff.shp"
distances = [.25, .5, .75, 1, 1.25, 1.5, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5]
bufferUnit = "miles"

# Execute MultipleRingBuffer
arcpy.MultipleRingBuffer_analysis(inFeatures, outFeatureClass, distances, bufferUnit, "", "ALL")