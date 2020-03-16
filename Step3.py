import json
import requests
import pickle
#

# TODO: write a program that Buys a stock when the RSI goes from <32 to >54 within 24 hours.

# How to use:
# Data = pull_[Technical Indicator]
# #Will return a variable called Data with a dictionary of values.



# Create string request
requestD = "https://www.alphavantage.co/query?function=func1&symbol=Ticker&" \
          "interval=intervalV&time_period=timeP&series_type=open&apikey=KEYA"

#   Pull_rsi(stockname), returns a dictionary.
def pull_rsi(ticker="TSLA", interval="30min", period="10"):
    # RETURNS A DICTIONARY OBJ

    key = str("2U2M12W6VQ47QS0J")

    # Create string request
    request = requestD

    # place in ticker, interval and period
    request = request.replace("func1", "RSI")
    request = request.replace("Ticker", ticker)
    request = request.replace("intervalV", interval)
    request = request.replace("timeP", period)
    request = request.replace("KEYA", key)

    data = requests.get(request)
    print(request)

    return json.loads(data.text)


def pull_sma(ticker="TSLA", interval="30min", period="10"):
    # RETURNS A DICTIONARY OBJ

    key = str("2U2M12W6VQ47QS0J")
    request = requestD

    # place in ticker, interval and period
    request = request.replace("func1", "SMA")
    request = request.replace("Ticker", ticker)
    request = request.replace("intervalV", interval)
    request = request.replace("timeP", period)
    request = request.replace("KEYA", key)

    data = requests.get(request)
    print(request)

    return json.loads(data.text)

def pull_macd(ticker="TSLA", interval="30min", period="10"):
    # RETURNS A DICTIONARY OBJ

    key = str("2U2M12W6VQ47QS0J")
    request = requestD

    # place in ticker, interval and period
    request = request.replace("func1", "MACD")
    request = request.replace("Ticker", ticker)
    request = request.replace("intervalV", interval)
    request = request.replace("timeP", period)
    request = request.replace("KEYA", key)

    data = requests.get(request)
    print(request)

    return json.loads(data.text)

# get number of values to compare
def value_count(data, techind="RSI"):
    value_name = 'Technical Analysis: ' + techind
    # Returns  the number of values in json file.
    return len(data[value_name])


# print rsi with dates
def print_rsid(data):
    # prints all of the RSI values
    lis = get_rsil(data)
    print(lis)


# returns a list with raw rsi values.
def get_rsil(data):
    dtl = list(data['Technical Analysis: RSI'])
    ls = []

    # for every object in the date list, append the corresponding RSI value.
    for d in dtl:
        # append raw RSI value
        ls.append((data['Technical Analysis: RSI'][d]['RSI']))

    return list(map(float, ls))


#  A function that returns the lowest of the past x values given a list amd index number return 999 if failed
def find_low(ls, indx=0, last=0):

    if indx <= last:
        return 99999

    low = 99999

    lv = indx - last
    i = 0

    while i < lv:
        if ls[lv] < low:
            low = ls[lv]
        i += 1
    return low


# function that returns the highest of the last n values given a list and index number. return -9 failed
def find_high(ls, indx=0, last=0):

    high = -9
    if indx <= last:
        return high

    lv = indx - last
    i = 0

    while i < lv:
        if ls[lv] > high:
            high = ls[lv]
        i += 1
    return high


# Given dictionary, print buy, if RSI goes from <32 to above 55 in last 13 trading hours
def buy_it_high(data, hours = 26, low = 30, high = 55):
    # Get list of dates, that correspond to RSI Values.
    dtl = list(data['Technical Analysis: RSI'])
    # Get RSI values.
    rsi = get_rsil(data)

    # Put lists in chronological order.
    list.reverse(dtl)
    list.reverse(rsi)

    last_buy = 6
    i = 0
    max = value_count(data)
    buycount = 0

    while i < max:

        nlow = find_low(rsi, i, hours)

        if rsi[i] > high and nlow < low and last_buy > 6:

            print(dtl[i], rsi[i])
            last_buy = 0
            buycount += 1

        last_buy += 1
        i += 1

    return print(buycount)


# Given dictionary, print the date if RSI goes from >55 to < 32 in the last 13 trading hours.

def buy_it_low(data, hours = 26, rhigh = 55, low = 32):
    # Should we be able to buy a stock if we already have a position? but only twice within 3 hours.

    # Get list of dates, that correspond to RSI Values.
    dtl = list(data['Technical Analysis: RSI'])
    # Get RSI values.
    rsi = get_rsil(data)

    # Put lists in chronological order.
    list.reverse(dtl)
    list.reverse(rsi)

    last_buy = 6
    i = 0
    max = value_count(data)
    buycount = 0

    while i < max:

        high = find_high(rsi, i, hours)

        if rsi[i] < low and high > rhigh and last_buy > 6:

            print(dtl[i], rsi[i])
            buycount += 1
            last_buy = 0

        last_buy +=1
        i += 1

    print(buycount)


# function that saves the dictionary to a file for future use, given file name and dictionary
def save(data, name):
    # Check for null values.
    if name is None:
        print("Please enter a name")
        return

    file = name + ".pickle"

    # open file
    pickle_out = open(file, "wb")

    # write file
    pickle.dump(data, pickle_out)

    # close
    pickle_out.close()

    print("Saved")
    return


#TODO: Implement ML



# function tha loads previously saved file.
def load(name):
    file = name + ".pickle"

    pickle_in = open(file, "rb")

    return pickle.load(pickle_in)
