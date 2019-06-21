#Script for adding fields to Park INV aoi Boundaries
import arcpy

arcpy.env.workspace = "E:/Park_Ivnt/AoIs/Park_AoIs.shp"

inFeatures = "Park_AoIs"

fieldName1 = "Name"
fieldAlias1 = "Name"

fieldName2 = "Year_"
fieldAlias2 = "Year_"

fieldName3 = "Tree_count"
fieldAlias3 = "Tree_count"

fieldName4 = "Ward"
fieldAlias4 = "Ward"

fieldName5 = "InvDate"
fieldAlias5 = "InvDate"

fieldName6 = "Ownership"
fieldAlias6 = "Ownership"

arcpy.AddField_management(inFeatures, fieldName1, "String", "50",
                          field_alias=fieldAlias1, field_is_nullable="NULLABLE")

arcpy.AddField_management(inFeatures, fieldName2, "Integer", "10",
                          field_alias=fieldAlias2, field_is_nullable="NULLABLE")

arcpy.AddField_management(inFeatures, fieldName3, "Single", "13",
                          field_alias=fieldAlias3, field_is_nullable="NULLABLE")

arcpy.AddField_management(inFeatures, fieldName4, "Integer", "10",
                          field_alias=fieldAlias4, field_is_nullable="NULLABLE")

arcpy.AddField_management(inFeatures, fieldName5, "Date", "8",
                          field_alias=fieldAlias5, field_is_nullable="NULLABLE")

arcpy.AddField_management(inFeatures, fieldName6, "String", "24",
                          field_alias=fieldAlias6, field_is_nullable="NULLABLE")
