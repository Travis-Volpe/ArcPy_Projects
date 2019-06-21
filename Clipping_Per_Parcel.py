import arcpy

arcpy.AddField_management("Religious_Orgs_Selection_Proj", "Per_GS", "Double", 10, 4)

arcpy.CalculateField_management("Religious_Orgs_Selection_Proj", "Per_GS",
                                "[Green_Spac] / [TotArea] * 100")

Clip_analysis (in_features, clip_features, out_feature_class, {cluster_tolerance})

in_features = SelectLayerByAttribute_management ("Religious_Orgs_Selection_Proj", "NEW_SELECTION", {where_clause}, {invert_where_clause})

where_clause = 


arcpy.SelectLayerByAttribute_management("states", "NEW_SELECTION",
                                        "[NAME] = 'California'")

for record in row:
    select by obj id - 0:418
    clip
