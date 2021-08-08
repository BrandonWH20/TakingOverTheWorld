# Put ya key for some bomb-diggity
key = str("2U2M12W6VQ47QS0J")

# TODO: Done
class CurrencyExchangeRate:
    def __init__(self, fromcurrency="BTC", tocurrency="USD"):
        self.function = "CURRENCY_EXCHANGE_RATE"
        self.fromcurrency = fromcurrency
        self.tocurrency = tocurrency
        self.call = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&" \
                    "from_currency=" + self.fromcurrency + "&to_currency=" + self.tocurrency + "&apikey=" + key


# TODO: Done
class CryptoRating:
    def __init__(self, symbol="BTC"):
        self.function = "CRYPTO_RATING"
        self.symbol = symbol
        self.call = "https://www.alphavantage.co/query?function=CRYPTO_RATING&symbol=" + self.symbol \
                    + "&apikey=" + key


# TODO: Done
class CryptoIntraday:
    def __init__(self, symbol="BTC", market="USD", interval="5", outputsize="compact"):
        self.function = "CRYPTO_INTRADAY"
        self.symbol = symbol
        self.market = market
        self.interval = interval
        self.outputsize = outputsize
        self.call = "https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=" + self.symbol \
                    + "&market=" + self.market + "&interval=" + self.interval + "&outputsize" \
                    + self.outputsize + "&apikey=demo"


# TODO: Done
class MACD:
    def __init__(self, symbol="BTCBNB", interval="5", series_type="open", fast="12", slow="26", signal="9"):
        self.function = "MACD"
        self.symbol = symbol
        self.interval = interval
        self.series_type = series_type
        self.fast = fast
        self.slow = slow
        self.signal = signal
        self.call = "https://www.alphavantage.co/query?function=MACD&symbol=" + self.symbol + \
                    "&interval=" + self.interval + "&series_type=" + self.series_type + "&apikey=" + key \
                    + "&fast=" + self.fast + "&slow=" + self.slow + "&signal=" + self.signal


# TODO: Done
class SMA:
    def __init__(self, symbol="BTCBNB", interval="5", series_type="open", time_period="12"):
        self.function = "SMA"
        self.pair = symbol
        self.interval = interval
        self.series_type = series_type
        self.time_period = time_period
        self.call = "https://www.alphavantage.co/query?function=SMA&symbol=" + self.symbol \
                    + "&interval=" + self.interval + "&time_period=" + time_period + "&series_type=" + series_type \
                    + "&apikey=" + key


# TODO: VWAPPPPPPPPPPPPPP
class VWAP:
    def __init__(self, symbol="BTCBNB", interval="5"):
        self.function = "VWAP"
        self.symbol = symbol
        self.interval = interval
        self.call = ""


# TODO:
class OBV:
    def __init__(self, symbol="BTCBNB", interval="5", ):
        self.function = "OBV"
        self.pair = symbol
        self.interval = interval
        self.call = "https://www.alphavantage.co/query?function=OBV" \
                    "&symbol=" + self.symbol + "&interval=" + self.interval + "&apikey="+ key