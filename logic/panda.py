# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame

# データ1の準備
attri_data1 = {'ID':['100','101','102','105','106','107']
                       ,'city':['Tokyo','Chiba','Kyoto','Gunma','Tokyo','Tokyo']
                       ,'birth_year':[1991,1992,1985,1996,1981,2008]
                       ,'name':['Yamada','Sato','Suzuki','Kitamura','Aoki','saru']}
data_frame1 = DataFrame(attri_data1)

# データ2の準備
attri_data2 = {'ID':['100','101','102','103','104']
                       ,'math':[34,77,45,81,98]
                       ,'English':[47,64,16,53,37]
                       ,'sex':['F','M','F','F','M']
                       ,'index_num':[0,1,2,3,4]}
data_frame2 = DataFrame(attri_data2)

#print(pd.merge(data_frame1, data_frame2, how="inner" ,on="ID"))
df=pd.merge(data_frame1, data_frame2, how="left" ,on="ID")
#print(df.to_html())
print df
