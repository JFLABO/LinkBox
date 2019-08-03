# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import pprint
import json

# データ1の準備
LOG = 'data01.json'
attri_data1 = open(LOG, 'r')
data_frame1 = DataFrame(attri_data1)

# データ2の準備
LOG = 'data02.json'
attri_data2 = open(LOG, 'r')
data_frame2 = DataFrame(attri_data2)

#print(pd.merge(data_frame1, data_frame2, how="inner" ,on="ID"))
df=pd.merge(data_frame1, data_frame2, how="left" ,on="ID")
#print(df.to_html())
pprint (df.to_json)
