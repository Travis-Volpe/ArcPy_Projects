import arcpy

fc = 'E:/Data/Property/Tax_Lots/Tax_Lots.shp'
fields = arcpy.ListFields(fc)
file = open('E:/Data/Property/TaxLot_fieldInfo.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()
 
