import arcpy

arcpy.env.workspace = r"E:/Park_Ivnt"

arcpy.MakeXYEventLayer_management(table="E:/Park_Ivnt/2018_PI_Final_Single.csv",
    in_x_field="POINT_X",
    in_y_field="POINT_Y",
    out_layer="2018_pi_Merged_Points",
    spatial_reference="4326")

arcpy.FeatureToPoint_management(in_features="2018_pi_Merged_Points",
    out_feature_class="E:/Park_Ivnt/2018_pi_Merged_Points.shp",
    point_location="CENTROID")
