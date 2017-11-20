# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:19:38 2017

@author: vaugeois
"""
import pandas as pd
import poloniex as px

gpair = "USDT_BTC"    # Use ETH pricing data on the BTC market
period = 86400       # Use 1 day candles  you can chqnge to 5/15/30 min or 2/4 hours
daysBack = 0       # Grab data starting 0 days ago
daysData = 730+730    # From there collect 60 days of data

# Request data from Poloniex
data = px.getPast(gpair, period, daysBack, daysData)

# Convert to Pandas dataframe with datetime format
data = pd.DataFrame(data)

data['date'] = pd.to_datetime(data['date'], unit='s')

writer = pd.ExcelWriter(gpair+".xlsx")
data.to_excel(writer,'Sheet1')
writer.save()