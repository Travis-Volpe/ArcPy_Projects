import pandas as pd

ss_data = r'C:\Users\tvolpe\Desktop\SS_Data_Analysis\Data\SurvivalStudy2018_dbFields.csv'

ss = pd.read_table(ss_data, sep=',')

ss.columns

"""
Index([u'CT_Tag_ID', u'Date_Ptd', u'Cultivar', u'SciName', u'ID', u'FID',
       u'CmmnName', u'DBH', u'Program', u'Removed', u'Location', u'EventORAdd',
       u'Impervious', u'DBH1', u'DBH2', u'DBH3', u'DBH4', u'TotalHeigh',
       u'Width_NS', u'Width_EW', u'PercentMis', u'CrownCondi', u'TreeStruct',
       u'OverallHea', u'SpaceType1', u'Notes15', u'CrownBase', u'Notes_2016',
       u'Jurisdicti', u'SpaceTypeD', u'FID_1', u'CT_Tag_ID_1', u'Legacy_ID',
       u'Loc_Status', u'Date_Ptd_1', u'DBH_1', u'StockType', u'Nursery',
       u'Class_Code', u'SpaceType', u'Jurisdictn', u'Program_1', u'Fund_Type',
       u'Mntc_Condn', u'Removed_1', u'OBJECTID', u'Season'],
      dtype='object')
"""
ss.OverallHea.isnull().sum()
#130
ss.OverallHea.unique()
#['Good', 'Missing', 'Left Card', nan, 'Poor', 'Dead']

# Add a field noting whether the trees is alive or dead
isAlive = []
for row in ss['OverallHea']:
    if row == 'Dead':
        isAlive.append(0)
    elif row =='dead':
        isAlive.append(0)
    elif row =='Missing':
        isAlive.append(0)
    elif row =='nan':
        isAlive.append(0)        
    else:
        isAlive.append(1)

ss['isAlive'] = isAlive

ss.isAlive.value_counts()

#Make a NEW EXCEL/CSV File containing at least the overall health from previous years
# possibly DBH, Height, ecetera 

# Need to figure out what nan, missing, left card mean in terms of alive/dead


#Add column noting years alive, 






#'Remap' categoriacal fields to be numeric
