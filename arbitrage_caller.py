import os
import sys
import schedule
import time
coins = [
    '1INCH',
    'AAVE',
    'ADA',
    'AKRO',
    'ALGO',
    'ANKR',
    'ARPA',
    'ATOM',
    'AVA',
    'AVAX',
    'BAL',
    'BAND',
    'BAR',
    'BAT',
    'BCH',
    'BNB',
    'BTC',
    'BTT',
    'CAKE',
    'CELO',
    'CHR',
    'CHZ',
    'CKB',
    'COMP',
    'CRV',
    'DAI',
    'DEGO',
    'DGB',
    'DIA',
    'DODO',
    'DOGE',
    'DOT',
    'ENJ',
    'EOS',
    'ETC',
    'ETH',
    'FIL',
    'FORTH',
    'FTM',
    'GRT',
    'ICP',
    'IOST',
    'JST',
    'KSM',
    'LINK',
    'LRC',
    'LTC',
    'LUNA',
    'MASK',
    'MATIC',
    'MIR',
    'NANO',
    'OGN',
    'OMG',
    'ONE',
    'ONT',
    'ORN',
    'PUNDIX',
    'QTUM',
    'ROSE',
    'SHIB',
    'SUSD',
    'SUSHI',
    'SXP',
    'THETA',
    'TRX',
    'UMA',
    'UNI',
    'USDC',
    'VET',
    'WAVES',
    'WIN',
    'XEM',
    'XLM',
    'XMR',
    'XRP',
    'XTZ',
    'XVG',
    'YFI',
    'YFII',
    'ZEN',
    'ZIL',
]
file = sys.argv[1]
i = 0
for coin in coins:
    i+=1
    if i % 5 == 1 and i > 4:
        time.sleep(60)

    cmd = "python3 " + file + " " + coin
    print (str(i) + " " + cmd)
    os.popen(cmd)
    
