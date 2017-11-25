# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:21:12 2017

@author: vaugeois
"""

import pandas as pd
ewma = pd.stats.moments.ewma

#Exponential Moving Average
def mae(data,interval):
    average=ewma(data['USDT_BTC'],com=interval,adjust=False)
    return average.fillna(method='bfill')


#Bollinger Bands
def bollinger(data,interval):
    ma=data['USDT_BTC'].rolling(window=interval).mean()        
    sigma=pd.rolling_std(data['USDT_BTC'], interval, min_periods=interval)
    data['MA']=ma.fillna(method='bfill')
    data['MAsup']=(ma+2*sigma).fillna(method='bfill')
    data['MAinf']=(ma-2*sigma).fillna(method='bfill')
    return data
    
#Ichimoku 
def Kijun_sen(data):
    period26_high = pd.rolling_max(data['USDT_BTC'], window=26)
    period26_low = pd.rolling_min(data['USDT_BTC'], window=26)
    data['kijun_sen'] = ((period26_high + period26_low) / 2).fillna(method='bfill')
    return data

def Tenkan_sen(data):
    period9_high = pd.rolling_max(data['USDT_BTC'], window=9)
    period9_low = pd.rolling_min(data['USDT_BTC'], window=9)
    data['tenkan_sen'] = ((period9_high + period9_low) / 2).fillna(method='bfill')
    return data
    
def Senkou_span_a(data):
    data['senkou_span_a'] = (((data['tenkan_sen'] + data['kijun_sen']) / 2).shift(26)).fillna(method='bfill')
    return data

def Senkou_span_b(data):
    period52_high = pd.rolling_max(data['high'], window=52)
    period52_low = pd.rolling_min(data['low'], window=52)
    data['senkou_span_b'] = (((period52_high + period52_low) / 2).shift(52)).fillna(method='bfill')
    return data

def Chikou_span(data):
    data['chikou_span'] = (data['USDT_BTC'].shift(-26)).fillna(method='bfill')
    return data

def Ichimoku(data):
    data=Kijun_sen(data)
    data=Tenkan_sen(data)
    data=Senkou_span_a(data)
    data=Senkou_span_b(data)
    data=Chikou_span(data)
    return data

    
