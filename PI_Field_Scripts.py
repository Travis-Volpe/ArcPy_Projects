# Park Inventory Scripts
# CSV to JSON

# Examining All Values
import arcpy

arcpy.env.workspace = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV'

fc = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV/2015_2018_Park_INV/test_data.shp'

fields = ['Scientific', 'CommonName']

with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        print(u'{0}, {1}'.format(row[0], row[1]))


# Repalce Values
#arcpy.da.SearchCursor(in_table, field_names, {where_clause}, {spatial_reference},
#    {explode_to_points}, {sql_clause})
#
#import pandas as pd
import arcpy

arcpy.env.workspace = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV'

fc = 'Q:/Projects/Parks/ParkInventory/2018/2018 Park INV/2015_2018_Park_INV/test_data.shp'

fields = ['Scientific', 'CommonName']

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        if (row[0] LIKE '%SciName%'):
            row[0] = "SciName" and row[1] = 'CmmnName'
        elif (row[SciName/0] LIKE '%SciName%'):
            row[0] = "SciName" and row[1] = 'CmmnName'
        elif (row[SciName/0] LIKE '%SciName%'):
            row[0] = "SciName" and row[1] = 'CmmnName'
        elif (row[SciName/0] LIKE '%SciName%'):
            row[0] = "SciName" and row[1] = 'CmmnName'

        cursor.updateRow(row)




OR

def Rename(field):
    type1_replace = ["VALUES TO Replace"]
    ...

    for n in type1_replace:
        field = field.replace(n, "Raplacement Value")
    ...
    return field
