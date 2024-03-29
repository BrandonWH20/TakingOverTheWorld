import csv
import time

from AlphaFunctions import *
from Step3 import *

requestD = "https://www.alphavantage.co/query?function=func1&symbol=Ticker&" \
           "interval=intervalV&time_period=timeP&series_type=open&apikey=KEYA"

# Modify these settings.. they are referenced by everything else.
key = str("2U2M12W6VQ47QS0J")
keylimit = 5
crypt1 = "BTC"
crypt2 = "ETH"
market = "USD"
interval = "5"
period = "12"
series_type = "open"
fast = "12"
slow = "26"
signal = "9"
outputsize="compact"

# TODO: Basis for Auto-regression.. Run . regression correleation matrix Create a universal Function that takes in a ticker and a list of indicators and returns a CSV with the given information
# Given Ticker and a list of indicators, should return a csv.
# list of stocks to scan: TSLA MSFT GOOG AMD NVDA
# Indicators to check: Intraday ULTOSC SMA EMA VWAP  MACD OBV HT_SINE


# Stock indicators
ind = ("EMA", "SMA", "OBV", "RSI", "ULTOSC")

# Crypto Indicators to use: EMA, SMA, MACD, VWAP,
cind = {
        CurrencyExchangeRate(crypt1,crypt2,),
        CryptoRating(crypt1),
        # SMA(crypt1,interval,series_type,period),
        MACD(crypt1,interval,series_type,fast,slow,signal),
        VWAP(crypt1,interval),
        OBV(crypt1,interval),
        }
# #   Currency_Exchange_Rate
# #   CRYPTO_RATING
# #   CRYPTO_INTRADAY



# Economic Indicators
eind = {"REAL_GDP", "REAL_GDP_PER_CAPITA", "TREASURY_YIELD", "FEDERAL_FUNDS_RATE",
        "CPI" "INFLATION", "INFLATION_EXPECTATION", "CONSUMER_SENTIMENT", "RETAIL_SALES",
        "DURABLES", "UNEMPLOYMENT", "NONFARM_PAYROLL"}


# REAL_GDP
# REAL_GDP_PER_CAPITA
# TREASURY_YIELD
# FEDERAL_FUNDS_RATE
# CPI
# INFLATION
# INFLATION_EXPECTATION
# CONSUMER_SENTIMENT
# RETAIL_SALES
# DURABLES
# UNEMPLOYMENT
# NONFARM_PAYROLL


def get_CSV(ticker, IND=ind, interval="30min", period="60"):
    # List of tasks this should complete.
    # 1. Take in: ticker, List of indicators, interval, period
    # 2. Using the unfortunately hardcoded key, submit a pull request..(Need to rate limit.. See Alpha Vantage TOS)
    # 3. Save a CSV file that contains the appended values.

    # used to determine if time column has been set. We will use the first indicators time stamp.
    timeset = False

    dls = list()
    timel = []

    # 2 For each indicator in the list, return an array with the date stamp and corresponding IND value

    for d in range(len(IND)):

        # Per Alpha Vantage site.. 8/31/2020: 5 API requests per minute and 500 requests per day.
        alpha_rate_limit = False

        if len(IND) > 5:
            alpha_rate_limit = True

        # Submit Pull request, may need to rate limit due to Alpha Vantage restrictions.
        data = pull_data(IND[d], ticker, interval, period)

        if timeset is False:
            dtat = list(data['Technical Analysis: ' + IND[d]])
            for i in range(len(dtat)):
                timel.append(dtat[i])
            timeset = True

        # Turn Data into a list and append to dls
        dls.append(get_list(data, IND[d]))

        if alpha_rate_limit:
            time.sleep(12)

        # Append list to csv.
        # 1. Create CSV file
        # 2. Append row by row, by iterating through linked list sub-lists.

    # 3. Create CSV file. # Fuckkkk we neeed to write row by row... This is harder...
    append_to_csv(IND, dls, timel)

    return dls


# TODO: Rewrite get_CSV for crypto: Should include cind
# We should call this function when we need a list of indicators to compare..
# Should be Prep for correlation matrix: Knime
# Some useful code "https://www.alphavantage.co/query?function=SMA&symbol=USDEUR
# &interval=weekly&time_period=10&series_type=open&apikey=keya"
def get_crypt(ind=cind):
    #TODO: List of tasks this should complete.
    #
    # 1. Take in: crypt pair. List of indicators, interval, period
    # 2. Using the unfortunately hardcoded key, submit a pull request..(Need to rate limit.. See Alpha Vantage TOS)
    # 3. Save a CSV file that contains the appended values.

    # Theory Time.. How do we hunt the big fish? Run a correlation test on stocks.. money is moving somewhere..
    # What if we tried to follow funds? We target them by knowing their public stats and look for textbook plays..
    # Boom... Textbook plays.. Let's find Mr. Manager from "investing for dummy's 101"
    # Is it easier or harder to predict the masses? The way information spreads.

    # used to determine if time column has been set. We will use the first indicators time stamp.
    timeset = False

    # creates a cache used to hold what we need to append to the csv
    dls = list()

    # This is used when we pull time from the requested json file. time-List
    timel = []

    # TODO: Fix this loop
    #  For each indicator in the list, return an array with the date stamp and corresponding IND value
    for d in range(len(ind)):

        # Per Alpha Vantage site.. 8/31/2020: 5 API requests per minute and 500 requests per day.
        alpha_rate_limit = False

        if len(ind) > keylimit:
            alpha_rate_limit = True

        # Submit Pull request, may need to rate limit due to Alpha Vantage restrictions.
        data = ind[""]

        if timeset is False:
            dtat = list(data['Technical Analysis: ' + ind[d]])
            for i in range(len(dtat)):
                timel.append(dtat[i])
            timeset = True

        # Turn Data into a list and append to dls
        # This is a sweet little line of code tbh.
        dls.append(get_list(data, ind[d.function]))

        if alpha_rate_limit:
            time.sleep(12)

        # Append list to csv.
        # 1. Create CSV file
        # 2. Append row by row, by iterating through linked list sub-lists.

    # 3. Create CSV file. # Fuckkkk we neeed to write row by row... This is harder... solution: new function
    append_to_csv(ind, dls, timel)

    return dls


def pull_data(func="TIME_SERIES_INTRADAY", ticker="TSLA", interval="30min", period="10"):
    # RETURNS A DICTIONARY OBJ

    # probably should not be here.
    key = str("2U2M12W6VQ47QS0J")

    # Create string request
    request = "https://www.alphavantage.co/query?function=FUNC&symbol=Ticker&" \
              "interval=intervalV&time_period=timeP&series_type=open&apikey=KEYA"

    # place in ticker, interval and period
    request = request.replace("FUNC", func)
    request = request.replace("Ticker", ticker)
    request = request.replace("intervalV", interval)
    request = request.replace("timeP", period)
    request = request.replace("KEYA", key)

    # TODO: Need to scan for Indicators that don't use Series_Type..
    if (func == "ULTOSC"):
        request = request.replace("&time_period=timeP&series_type=open", "")

    data = requests.get(request)
    print(request)

    return json.loads(data.text)


# returns a list of raw iND values.
def get_list(data, iND):
    dtl = list(data['Technical Analysis: ' + iND])
    ls = []

    for d in dtl:
        # append without date.
        ls.append((data['Technical Analysis: ' + iND][d][iND]))

    return list(map(float, ls))


def get_time(data):
    timels = []

    for d in range(len(data)):
        timels.append(d)

    return timels


def create_CSV(title):
    with open(title + '.csv', 'w', newline='') as outfile:
        time.sleep(0.01)
    return outfile


# takes in a list of values.. Appends values to given CSV.
# iND is the list of indicators. datalist is the actual data to be appended. timel = time list titl
def append_to_csv(iND, datalist, timel, title='data'):
    # use temp as the write row.
    if not timel:
        temp = [float]
        n = 0
        header = ['time']
        timel.clear

        # this seems dumn, but we always need to add the time/date to the csv header file, and this is my solution.
        for i in range(len(iND)):
            header.append(iND[i])

    # We now have a list of lists...
    # for each sublist m, we need to take the n'th value and append to temp write row..
    # Since we are using tuples, this should give us a very quick read time.. Will not scale..

    # Each list will be the same length, so if we use this to keep count of what to add.
    with open(title + '.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)

        while n < len(datalist[0]) - 1:

            # clear temp for new row..
            temp.clear()
            m = 0

            # Append time to first column
            temp.append(timel[n])

            # Access each sublist, and append value to temp.
            while m < len(datalist):
                temp.append(datalist[m][n])
                m += 1

            # Write temp row to csv.
            writer.writerow(temp)
            n += 1

# TODO: I don't actually use the code below this.. Just some legacy stuff from 2018!
# returns a list with raw rsi values.
def get_rsil(data):
    dtl = list(data['Technical Analysis: RSI'])
    ls = []
    time = []
    # for every object in the date list, append the corresponding RSI value.
    for d in dtl:
        # append raw RSI value
        time.append(d)
        ls.append((data['Technical Analysis: RSI'][d]['RSI']))

    return list(map(float, ls)), time;

    # returns a list with raw rsi values.


def get_macdl(data):
    dtl = list(data['Technical Analysis: MACD'])
    ls = []
    # for every object in the date list, append the corresponding RSI value.
    for d in dtl:
        # append raw value
        ls.append((data['Technical Analysis: MACD'][d]['MACD']))

    return list(map(float, ls))


def get_smal(data):
    dtl = list(data['Technical Analysis: SMA'])
    ls = []
    # for every object in the date list, append the corresponding RSI value.
    for d in dtl:
        # append raw RSI value
        ls.append((data['Technical Analysis: SMA'][d]['SMA']))

    return list(map(float, ls))


def collection(symbol, interval, period):
    print(symbol + interval + period)

    # Pulls the json files from Alphavantage
    rsi_json = pull_rsi(symbol, interval, period)
    macd_json = pull_macd(symbol, interval, period)
    sma_json = pull_sma(symbol, interval, period)
    print(sma_json)

    # Converts json files to lists
    rsi_list, time = get_rsil(rsi_json)
    macd_list = get_macdl(macd_json)
    sma_list = get_smal(sma_json)

    print(time)
    with open('data.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        temp1 = {"Time/Data", "RSI", "MACD", "SMA"}
        writer.writerow(temp1)
        for i in range(len(rsi_list)):
            temp = [time[i], rsi_list[i], macd_list[i], sma_list[i]]
            writer.writerow(temp)


def mark_append_to_csv():
    if __name__ == "__main__":
        ticker = 'string'
        interval = 'string'
        period = 'string'
        ticker = input("Please specify ticker symbol (eg: TSLA): ")
        interval = input("Please specify time interval(1min, 5min, 15min, 30min or 60min): ")
        period = input("Please specify ticker symbol (positive numbers): ")
        collection(ticker, interval, period)
