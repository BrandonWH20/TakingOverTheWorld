import json
import requests

""" TODO: write a program that Buys a stock when the RSI goes from <32 to >54 within 24 hours.  """

# What do you love 0
# WHat are you good at? 0
# what does the world need? 0
# what can you get paid for? 0 vendiagram. Intersection is useful.

# Done: Get the data as a dictionary
function = "TIME_SERIES_INTRADAY"


# get number of values to compare
def value_count(data):
    # Returns  the number of values in json file.
    string = "Technical analysis:  " + function
    return len(data['Technical Analysis: RSI'])


# print rsi with dates
def print_rsid(data):
    # prints all of the RSI values
    for data['Technical Analysis: RSI'] in data:
        print(data['Technical Analysis: RSI'])


# returns a list with raw rsi values.
def get_rsil(data):
    dtl = list(data['Technical Analysis: RSI'])
    ls = []

    # for every object in the date list, append the corresponding RSI value.
    for d in dtl:
        # append raw RSI value
        ls.append((data['Technical Analysis: RSI'][d]['RSI']))

    return list(map(float, ls))


# TODO: Write a function that returns the lowest of the past x values given a list amd index number return 999 if failed
def find_low(data, indx=0, last=0):

    ls = get_rsil(data)

    if indx < last:
        return 999

    low = 999
    lv = indx - last
    i = 0;

    while i < lv:
        if ls[lv] < low:
            low = ls[lv]
        i += 1
    return low


# TODO: Given dictionary, print buy, if RSI goes from <32, to above 55 in last 24 hours
def buy_it(data):
    dtl = list(data['Technical Analysis: RSI'])
    rsi = get_rsil(data)
    list.reverse(dtl)
    list.reverse(rsi)
    i = 26
    max = value_count(data)
    buycount= 0

    while i < max:
        low = find_low(rsi, i, 52)
        if rsi[i] > 55 and low < 30:
            print(dtl[i], rsi[i])

            buycount += 1
        i += 1

    return print(buycount)


def mark_test():
    answer = input('Enter Symbol For RSI test: ')

    if answer == "X":
        exit
    else:
        data = pull_data(answer)
