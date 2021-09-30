from flask import Flask, render_template
import config, csv
from binance.client import Client
from binance.enums import *

client = Client(config.API_KEY, config.API_SECRET)

app = Flask(__name__)

@app.route('/')
def index():
    title = 'SPIRIBOT'

    account = client.get_account()
    balances = account['balances']

    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html',title=title, my_balances=balances, symbols=symbols)


@app.route('/buy')
def buy():
    
    order = client.create_order(
    symbol='BTCUSDT',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')
    return 'buy'


@app.route('/sell')
def sell():
    return 'sell'


@app.route('/settings')
def settings():
    return 'settings'




#python -m flask run => to run
#set instead of export