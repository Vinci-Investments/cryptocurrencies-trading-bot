# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:20:16 2017

@author: vaugeois
"""

import pandas as pd
import matplotlib.pyplot as plt
from Indicator import mae,bollinger,Ichimoku


USDT_BTC = "USDT_BTC.csv"

def load(file):
    #we create a filelist if we want to compute for many pairs 
    data = []
    # Create the base DataFrame
    data = pd.DataFrame()
    
    #add datas to the dataframe 
    tmp = pd.DataFrame(pd.read_csv(filepath_or_buffer=file, sep=';')['close'])
    tmp2=pd.DataFrame(pd.read_csv(filepath_or_buffer=file, sep=';')['date'])
    tmp3=pd.DataFrame(pd.read_csv(filepath_or_buffer=file, sep=';')['high'])
    tmp4=pd.DataFrame(pd.read_csv(filepath_or_buffer=file, sep=';')['low'])
    tmp['close']=tmp['close'].astype(float)
    tmp['high']=tmp3.astype(float)
    tmp['low']=tmp4.astype(float)
    tmp['date']=pd.to_datetime(tmp2['date'])
    # Rename the Close column to the correct index/future name
    tmp.rename(columns={'close': file.replace(".csv", "")}, inplace=True)
         
    # Merge with data already loaded
    # It's like a SQL join on the dates
    data = data.join(tmp, how = 'right')
    
    # Resort by the dates, in case the join messed up the order
    data = data.sort_index()
    
    data['MAE1']=mae(data,20)
    data['MAE2']=mae(data,60)
    data=bollinger(data,20)
    data=Ichimoku(data)
    
    data.time = pd.to_datetime(data['date'], format='%Y-%m-%d.%f')
    # Plot the USDT_BTC
    plt.plot(data['USDT_BTC'],'b', label='USDT_BTC',linewidth=4)
    
    #PLOT FOR EXPONENTIAL MOVING AVERAGE
    plt.plot(data['MAE1'],'g',label='MAE_20')
    plt.plot(data['MAE2'],'r',label='MAE_60')
    
    #PLOT FOR BOLLINGER
    plt.plot(data['MA'],'r',label='MA')
    plt.plot(data['MAsup'],'r',label='MA+2sigma')
    plt.plot(data['MAinf'],'r',label='MA-2sigma')
    plt.fill_between(data.index,data['MAsup'],data['MAinf'],facecolor="yellow")
    
    #PLOT FOR ICHIMOKU
    plt.plot(data['kijun_sen'],'m',label='kijun_sen')
    plt.plot(data['tenkan_sen'],'k',label='tenkan_sen')
    plt.plot(data['senkou_span_a'],'g',label='senkou_span_a')
    plt.plot(data['senkou_span_b'],'g',label='senkou_span_b')
    plt.plot(data['chikou_span'],label='chikou_span')
    plt.fill_between(data.index,data['senkou_span_a'],data['senkou_span_b'],facecolor="green")
    
    plt.ylabel('Price')
    plt.xlabel('Date')
    plt.grid()
    plt.legend(loc=0)
    # Display everything
    plt.show()
    
    print(data)

load(USDT_BTC)