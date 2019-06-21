import arcpy

fc = 'D:/Parks/PI/2016_17/2016_2017_aois.shp'
fields = arcpy.ListFields(fc)
file = open('E:/Park_Ivnt/aoi_fieldInfo201617.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()
