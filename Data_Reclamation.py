# Name: Data_Reclamation.py
# Description:
#
#
#
################################################################################
#Part 1 Merge  Feild Mappings
# import system modules
import arcpy
from arcpy import env

#Set envrionment variables / the file path of the project folder
env.workspace = r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear'

################################################################################
#Export the fields names of the compontent data sets
fc1 = r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear/2012.shp'
fields1 = arcpy.ListFields(fc1)
file =  open(r'E:/SurvivalStudy/DataReclamation/Tabular/2012Fields.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields1:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc2 =r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear/2013.shp'
fields2 = arcpy.ListFields(fc2)
file = open(r'E:/SurvivalStudy/DataReclamation/Tabular/2013Fields.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields2:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc3 =r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear/2014.shp'
fields3 = arcpy.ListFields(fc3)
file = open(r'E:/SurvivalStudy/DataReclamation/Tabular/2014Fields.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields3:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc4 =r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear/2015.shp'
fields4 = arcpy.ListFields(fc4)
file = open(r'E:/SurvivalStudy/DataReclamation/Tabular/2015Fields.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields4:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc5 =r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear/2016_proj.shp'
fields5 = arcpy.ListFields(fc5)
file = open(r'E:/SurvivalStudy/DataReclamation/Tabular/2016Fields.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields5:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc6 =r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear/2017.shp'
fields6 = arcpy.ListFields(fc6)
file = open(r'E:/SurvivalStudy/DataReclamation/Tabular/2017Fields.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields6:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()

fc7 =r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear/2018_proj.shp'
fields7 = arcpy.ListFields(fc7)
file = open(r'E:/SurvivalStudy/DataReclamation/Tabular/2018Fields.txt', 'w')
file.write('Name, Type, Length\n')
for field in fields7:
    file.write('{},{},{}\n' .format(field.name, field.type, field.length))
file.close()
################################################################################
#import arcpy
#Code for adding fields 

# Local variables:
v2012 = "2012"
v2012__3_ = v2012
v2012__4_ = v2012__3_

# Process: Add Field
arcpy.AddField_management(v2012, "Cond_12", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(v2012__3_, "Cond_12", "[Conditio_1]", "VB", "")


################################################################################


# The feature classes to be merged
ss2012 = '2012.shp'
ss2013 = '2013.shp'
ss2014 = '2014.shp'
ss2015 = '2015.shp'
ss2016 = '2016_proj.shp'
ss2017 = '2017.shp'
ss2018 = '2018_proj.shp'

# Create FieldMappings object to manage merge output fields
fieldMappings = arcpy.FieldMappings()

# Add all fields from both oldStreets and newStreets
fieldMappings.addTable(ss2012)
fieldMappings.addTable(ss2013)
fieldMappings.addTable(ss2014)
fieldMappings.addTable(ss2015)
fieldMappings.addTable(ss2016)
fieldMappings.addTable(ss2017)
fieldMappings.addTable(ss2018)

# Add input fields "STREET_NAM" & "NM" into new output field
fldMap_SciName = arcpy.FieldMap()
fldMap_SciName.addInputField(ss2012,"SCI_NM")
fldMap_SciName.addInputField(ss2013,"SCI_NM")
fldMap_SciName.addInputField(ss2014,"SciName")
fldMap_SciName.addInputField(ss2015,"SciName")
fldMap_SciName.addInputField(ss2016,"SciName")
fldMap_SciName.addInputField(ss2017,"SciName")
fldMap_SciName.addInputField(ss2018,"SciName")

#CmmnName
fldMap_CmmnName = arcpy.FieldMap()
fldMap_CmmnName.addInputField(ss2012,"CMMN_NM")
fldMap_CmmnName.addInputField(ss2013,"CMMN_NM")
fldMap_CmmnName.addInputField(ss2014,"CmmnName")
fldMap_CmmnName.addInputField(ss2015,"CmmnName")
fldMap_CmmnName.addInputField(ss2016,"CmmnName")
fldMap_CmmnName.addInputField(ss2017,"CmmnName")
fldMap_CmmnName.addInputField(ss2018,"CmmnName")

#Date_Ptd
fldMap_Date = arcpy.FieldMap()
fldMap_Date.addInputField(ss2012,"DATE_PLNTD")
fldMap_Date.addInputField(ss2013,"DATE_PLNTD")
fldMap_Date.addInputField(ss2014,"Date_Ptd")
fldMap_Date.addInputField(ss2015,"Date_Ptd")
fldMap_Date.addInputField(ss2016,"Date_Ptd")
fldMap_Date.addInputField(ss2017,"Date_Ptd")
fldMap_Date.addInputField(ss2018,"Date_Ptd")

#TotalHeigh
fldMap_Height = arcpy.FieldMap()
fldMap_Height.addInputField(ss2012,"Total_He_1")
fldMap_Height.addInputField(ss2013,"DATE_PLNTD")
fldMap_Height.addInputField(ss2014,"TotalHeigh")
fldMap_Height.addInputField(ss2015,"TotalHeigh")
fldMap_Height.addInputField(ss2016,"TotalHeigh")
fldMap_Height.addInputField(ss2017,"TotalHeigh")
fldMap_Height.addInputField(ss2018,"TotalHeigh")

TotalHeigh
Width_NS
Width_EW
PercentMis
Location
EventORAdd
Impervious



DBH_ptd
DHB1
DBH2
DBH3
DBH4
DBH5
DBH6

# Set name of new output field "Street_Name"
#SciName = fldMap_SciName.outputField
#SciName.name = "Scientific_Name"
#fldMap_SciName.outputField = SciName
# Add output field to field mappings object
#fieldMappings.addFieldMap(fldMap_SciName)
#
# Remove all output fields from the field mappings, except fields "Street_Class", "Street_Name", & "Distance"
#for field in fieldMappings.fields:
#    if field.name not in ["Scientific_Name","Common_Name","Vicinity","Condition","DATE_PLANT", "Plant_Date","Date_Ptd","Genus", "GENUS_NAME", "FAME_NAME", "Species", "Cultivar", "Jurisdiction"  ]:
#        fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(field.name))
#
# Since both oldStreets and newStreets have field "Distance", no field mapping is required
#
# Use Merge tool to move features into single dataset
uptodateSS = r'E:/SurvivalStudy/DataReclamation/All_Years/Pre_Merge_byYear'
arcpy.Merge_management([ss2012, ss2013, ss2014, ss2015, ss2016, ss2017, ss2018],
    uptodateSS,
    fieldMappings)
