import math
import sys
import matplotlib.pyplot as plt
import pandas as pd
import os
import time

def extractwords(db,words,out):
    for x in range(len(db)):
        coisa=db.iloc[x]
        c=coisa.iloc[2]
        for word in words:
            if c.lower().find(word)!=-1:
                out=pd.concat([out,coisa],axis=1)
            else:
                continue
    return out
    
def testid(ide,coisa):
    global out
    if coisa[0]==ide or coisa[4]==ide:
                out.append(coisa)
                return
            
def extractlinks(coisa,ids):
    global out
    try:
        [testid(ide,coisa) for ide in ids]
    except AttributeError:
        return 
