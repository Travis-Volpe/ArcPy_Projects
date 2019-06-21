# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:01:40 2019

@author: tvolpe
"""

import pandas as pd

ss_data_path = r'E:/SurvivalStudy/Final_SS_Data/All_Years_2018M_wStatus.csv'

ss = pd.read_csv(ss_data_path, sep=',')

ss.shape

ss.index

ss.columns

"""Index([u'FID', u'Join_Count', u'TARGET_FID', u'CT_Tag_ID', u'Date_Ptd',
       u'Cultivar', u'SciName', u'CmmnName', u'DBH', u'Program', u'EventORAdd',
       u'Impervious', u'DBH1', u'DBH2', u'DBH3', u'DBH4', u'TotalHeigh',
       u'Width_NS', u'Width_EW', u'PercentMis', u'CrownCondi', u'TreeStruct',
       u'OverallHea', u'SpaceType1', u'CrownBase', u'Jurisdicti',
       u'MntcCondnD', u'SpaceTypeD', u'Cond_18', u'SpaceType', u'Condition',
       u'DDOE', u'PTG_Notes', u'Cond_12', u'Genus', u'Species', u'StockType',
       u'Class_Code', u'Mntc_Condn', u'Season', u'Nursery', u'Condit_13',
       u'POINT_X', u'POINT_Y', u'Cond_17', u'Cond_16', u'Cond_15', u'Cond_14',
       u'db_jdx', u'db_year', u'db_Season', u'db_removed', u'db_SpaceTy',
       u'db_Prog', u'db_StockT', u'db_ClassCo', u'db_Nursery', u'db_Genus',
       u'db_Species', u'db_mtc', u'db_pltdbh', u'isAlive', u'Death_Yr',
       u'Death_Age', u'Age', u'Cond_Agg'],
      dtype='object')"""


ss.dtypes

"""FID             int64
Join_Count      int64
TARGET_FID      int64
CT_Tag_ID      object
Date_Ptd       object
Cultivar       object
SciName        object
CmmnName       object
DBH           float64
Program        object
EventORAdd     object
Impervious     object
DBH1          float64
DBH2          float64
DBH3          float64
DBH4          float64
TotalHeigh    float64
Width_NS      float64
Width_EW      float64
PercentMis     object
CrownCondi     object
TreeStruct     object
OverallHea     object
SpaceType1     object
CrownBase       int64
Jurisdicti     object
MntcCondnD     object
SpaceTypeD     object
Cond_18        object
SpaceType      object
  
StockType      object
Class_Code     object
Mntc_Condn     object
Season         object
Nursery        object
Condit_13      object
POINT_X       float64
POINT_Y       float64
Cond_17        object
Cond_16        object
Cond_15        object
Cond_14        object
db_jdx         object
db_year         int64
db_Season      object
db_removed     object
db_SpaceTy     object
db_Prog        object
db_StockT      object
db_ClassCo      int64
db_Nursery     object
db_Genus       object
db_Species     object
db_mtc         object
db_pltdbh     float64
isAlive         int64
Death_Yr        int64
Death_Age       int64
Age             int64
Cond_Agg       object
Length: 66, dtype: object"""

ss.Death_Yr.value_counts()

"""0       7684
2017     520
2012     340
2016     340
2014     317
2018     296
2015     208
2013     156"""

#.describe

#.isnull().sum()

ss.Nursery.value_counts()

ss.Season.value_counts()

ss.Program.value_counts()

ss.Program.value_counts()

ss.Program.value_counts()


ss.Program.value_counts()
"""CTP           5686
REBATE        1159
DDOE           931
No Program     702
RiverSmart     620
RSH            332
DDOT Other     150
PEPCO          115
AER             91
FFS             58
DDOT Elms        7
                 5
TGA              4
DOEE             1"""


ss.groupby('SciName').Age.agg(['count', 'mean', 'min', 'max']).sort_values('mean')

ss.groupby('db_Genus').Age.agg(['count', 'mean', 'min', 'max']).sort_values('mean')

ss.groupby('Nursery').Age.agg(['count', 'mean', 'min', 'max']).sort_values('mean')
ss.groupby('db_Nursery').Age.agg(['count', 'mean', 'min', 'max']).sort_values('mean')

ss.groupby('db_Nursery').isAlive.agg(['count', 'mean', 'min', 'max']).sort_values('mean')

