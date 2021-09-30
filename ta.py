import numpy
import talib
from numpy import genfromtxt

#get the math done

my_data = genfromtxt('15minutes.csv', delimiter=',')

print(my_data)

closing_price = my_data[:,4]

print(closing_price)

rsi = talib.RSI(closing_price)

print(rsi)

#close = numpy.random.random(100)

#print(close)

#moving_average = talib.SMA(close,timeperiod=10)

#print(moving_average)

#rsi = talib.RSI(close)

#print(rsi)