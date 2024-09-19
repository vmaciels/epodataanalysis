import math
import sys
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
import dataextraction

abst=pd.read_csv('teste.csv')
abst=abst.values.tolist()
ids=[a[1] for a in abst]
db=pd.read_csv(tls,header=0,skiprows=0,iterator=True,chunksize=100000)
coisa=pd.read_csv(tls,header=0,nrows=1000)
print(coisa.iloc[724])

words=["dengue"]
words=[word.lower() for word in words]

out=[]

for chunk in db:
    lista=chunk.values.tolist()
    [dataextraction.extractwords(coisa,ids) for coisa in lista]
    #print("--- %s seconds ---" % (time.time() - start_time))