#!/usr/bin/python3

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.offline as plot
import matplotlib as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

cg = CoinGeckoAPI()
print(cg,'---------------')
price = cg.get_price(ids='bitcoin', vs_currencies='usd')
print(price,'++++++++++')
bitcoin_data = cg.get_coin_market_chart_by_id(id="bitcoin",vs_currency="usd",days=30)
#print(bitcoin_data)
bitcoin_price_data = bitcoin_data['prices']
bitcoin_price_data[0:5]
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp','Price'])
data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
candlestick_data = data.groupby(data.date,as_index=False).agg({'Price':['min','max','first','last']})
print(candlestick_data)
