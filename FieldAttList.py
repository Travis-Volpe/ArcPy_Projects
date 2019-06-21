import arcpy

fc1 = 'E:/Park_Ivnt/Final_Data/2018_Park_Inventory_Final.shp'
fields = arcpy.ListFields(fc1)
file = open('E:/Park_Ivnt/fieldInfo2018.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc2 = 'P:/Science and Policy/Programs/Research/Park Inventory/2015-09 Fall/2015-08-01 Langdon Park/Old Datasets/Langdon_2015itree_Final.shp'
fields = arcpy.ListFields(fc2)
file = open('E:/Park_Ivnt/fieldInfo2015.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc3 = 'D:/Parks/PI/2016_17/2016_2017_Park_INV.shp'
fields = arcpy.ListFields(fc3)
file = open('E:/Park_Ivnt/fieldInfo201617.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()
