from time import time
from colorama import init
from colorama import Fore, Back, Style
import keys
from binance.client import Client
import time

init()
symbolTicker = "BTCUSDT"

client = Client(keys.apiKey, keys.secret, tld="com")

# Guardamos variables globales

ordenCompra= 0
ordenVenta= 0
valorCompra = 0
valorVenta = 0
minutos= 1
segundos = 60
tx = 0

while 1:
    while True:
        try:
            depth = client.get_order_book(symbol=symbolTicker)
        except Exception as e:
            print(e)
        else:
            break
    
    for buy in depth["bids"]:
        if float(buy[1]):
            ordenCompra = ordenCompra + float(buy[1])
            valorCompra = float(buy[0])
    
    for sell in depth["asks"]:
        if float(sell[1]):
            ordenVenta = ordenVenta + float(sell[1])
            valorVenta = float(sell[0])
    
    if( tx < minutos*segundos):
        result = ordenCompra - ordenVenta
        grafico  = len(str(result))
        barras = ""

        for g in range(grafico):
            barras += "|"
        if result > 0:
            print(f"{Fore.GREEN} {barras} {Style.RESET_ALL} {str(valorVenta)}")
        else:
            print(f"{Fore.RED} {barras} {Style.RESET_ALL} {str(valorCompra)}")
            
        tx += 1
    else:
        ordenCompra = 0
        ordenVenta = 0
        tx = 0
