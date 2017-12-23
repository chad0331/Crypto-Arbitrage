import ccxt

#prints all of exchanges listed in the API
print(ccxt.exchanges)

#Loads the market for each exchange
poloniex=ccxt.poloniex()
gate=ccxt.gateio()
#save market data
#market data has the format of:
#{maker,taker,precision{amount,price},limits{amount{min,max}},price{min,max},cost{min,max}}
poloniexMarkets=poloniex.load_markets()
gateMarkets=gate.load_markets()
#prints id with market
poloniexSymbols=poloniex.symbols
gateSymbols=gate.symbols
print(poloniexSymbols)
print(gateSymbols)


