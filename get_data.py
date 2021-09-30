import config, csv
from binance.client import Client
client = Client(config.API_KEY, config.API_SECRET)

#prices = client.get_all_tickers()
#for p in prices:
#    print(p)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('.csv', 'w', newline='')

candlestick_writer = csv.writer(csvfile, delimiter=',')

#for candlestick in candles:
#    print(candlestick)
#    candlestick_writer.writerow(candlestick)

#print(len(candles))
 
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Dec, 2017", "1 Jan, 2018")

#get real time data

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close()