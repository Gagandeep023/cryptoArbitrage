import time
import ccxt
import requests
import redis
import sys


client = redis.Redis(host='127.0.0.1', port='6379')

# coin = ccxt.bithumb()
# money = coin.load_markets()
# for m in money:
#     print(m)
# quit()
def main():
    exchanges_us = [
        "kraken",
        "binanceus",
        "coinbasepro",
    ]
    exchanges_ind = [
        # "kucoin",
        "binance",
        "kraken",
    ]
    
    coin = sys.argv[1]

    symbols = [
        coin + "/USD",
        coin + "/USDT",
    ]
    i = 0
    if not client.get(coin):
        for symbol in symbols:
            
            print("{0}".format(symbol))
            if(i == 0):
                ask_exchange_id, ask_price, bid_exchange_id, bid_price = get_biggest_spread_by_symbol(
                exchanges_us, symbol)
                min_exchange_us =  ask_exchange_id
                min_price_us = ask_price 
                max_exchange_us= bid_exchange_id
                max_price_us= bid_price
                i+=1
            elif(i == 1):
                ask_exchange_id, ask_price, bid_exchange_id, bid_price = get_biggest_spread_by_symbol(
                exchanges_ind, symbol)
                min_exchange_ind =  ask_exchange_id
                min_price_ind = ask_price 
                max_exchange_ind= bid_exchange_id
                max_price_ind= bid_price
                i = 0
            

            if ask_price == 0 or bid_price == 0 or ask_price == 99999999 or bid_price == 99999999 :
                continue

            if ask_exchange_id == bid_exchange_id:
                continue

        

            increase_percentage = (bid_price - ask_price) / ask_price * 100
            # decrease_percentage = (ask_price - bid_price) / bid_price * 100
            # print("[Price of {0} on {1} is {2}, on {3} is {4} with {5:.4}%]".format(symbol, bid_exchange_id, bid_price, ask_exchange_id, ask_price, abs(increase_percentage)))

            
            if(abs(increase_percentage) > 5):
                base_url = 'https://api.telegram.org/secret&text="Price of {0} on {1} is {2}, on {3} is {4:.4} making a good chance of arbitrage with {5}%"'.format(symbol, bid_exchange_id, bid_price, ask_exchange_id,
                                                                    ask_price, abs(increase_percentage))
                requests.get(base_url)
                client.set(coin, 1, ex=1800)

        if not min_price_ind == 0 or not max_price_us == 0 or not min_price_us == 99999999 or not max_price_us == 99999999 :
            ind_percentage = (max_price_ind - min_price_us) / min_price_us * 100
            us_percentage = (max_price_us - min_price_ind) / min_price_ind * 100
        
            if ind_percentage > us_percentage:
                if(abs(ind_percentage) > 5):
                    base_url = 'https://api.telegram.org/secret&text="Price of {0} on {1} is {2}, on {3} is {4:.4} making a good chance of arbitrage with {5}%"'.format(coin, max_exchange_ind, max_price_ind, min_exchange_ind, min_price_us, abs(ind_percentage))
                    requests.get(base_url)
                    client.set(coin, 1, ex=1800)

            else:
                if(abs(us_percentage) > 5):
                    base_url = 'https://api.telegram.org/secret&text="Price of {0} on {1} is {2}, on {3} is {4:.4} making a good chance of arbitrage with {5}%"'.format(coin,max_exchange_us , max_price_us, min_exchange_us,
                                                                        min_price_ind, abs(us_percentage))
                    requests.get(base_url)
                    client.set(coin, 1, ex=1800)




def get_biggest_spread_by_symbol(exchanges, symbol):
    ask_exchange_id = ""
    min_ask_price = 99999999


    bid_exchange_id = ""
    max_bid_price = 0

    for exchange_id in exchanges:
        exchange = eval("ccxt.{0}()".format(exchange_id))
        print("{0}".format( exchange_id))
        try:
            order_book = exchange.fetch_order_book("{0}".format(symbol))
            bid_price = order_book['bids'][0][0] if len(
                order_book['bids']) > 0 else None
            ask_price = order_book['asks'][0][0] if len(
                order_book['asks']) > 0 else None

            print("{0}, {1}".format( exchange_id, ask_price))
            # print(ask_price)

            if ask_price < min_ask_price:
                ask_exchange_id = exchange_id
                min_ask_price = ask_price
            if bid_price > max_bid_price:
                bid_exchange_id = exchange_id
                max_bid_price = bid_price
        except:
            pass
            # print("")
            # print("{0} - There is an error!".format(exchange_id))



    return ask_exchange_id, min_ask_price, bid_exchange_id, max_bid_price


if __name__ == "__main__":
    main()
