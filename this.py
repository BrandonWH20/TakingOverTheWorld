import requests


def pull_ema():
    info = requests.get('https://www.alphavantage.co/query?function=EMA&symbol=TSLA&interval=30min&time_period=15&series_type=close&apikey=DLWWI58LSBLSWMWK')
    info = info.json()
    print(info)
    return info



def grab_recent_ema(data):
    key1 = str(sorted(data.keys())[1])
    sub_data = data[key1]
    key2 = str(sorted(sub_data.keys())[-1])
    sub_data1 = sub_data[key2]
    key3 = str(sorted(sub_data1.keys())[-1])
    ema = data.get(key1).get(key2).get(key3)
    return ema


data = pull_ema()
value = grab_recent_ema(data)
key = str(sorted(data.keys())[0])

print(key)
print(value)
