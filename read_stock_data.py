# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:25:09 2022

@author: baskar
"""

# Import packages
import yfinance as yf
import pandas as pd
import csv

#tickers = open('C:/Users/baska/Downloads/NUS/Big Data/Projects/tickers', 'w')
#f = open('C:/Users/baska/Downloads/NUS/Big Data/Projects/stock_data.csv', 'w')

# Read and print the stock tickers that make up S&P500
tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
#tickers.to_csv('C:/Users/baska/Downloads/NUS/Big Data/Projects/tickers.csv', encoding='utf-8')
print(tickers.head())

# Get the data for this tickers from yahoo finance
stock_data = yf.download(tickers.Symbol.to_list(),'2021-09-01','2022-04-01', auto_adjust=True)['Close']
sd = stock_data.to_csv('stock_data.csv', encoding='utf-8')
print(data.head())


import boto3 as boto3

s3 = boto3.resource('s3',aws_access_key_id='AKIA2I4L5O2NZ532672T', aws_secret_access_key='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')
bucket = s3.Bucket('bsaw-client-info','sd')
result = object.put(Body=sd)
    
    
