import json
import requests
import math

def load_data(file):
    return requests.get(file).json()
    
def get_biggest_bar(data):
    bar_name_seats = {}
    for bar in data:
        bar_name_seats[bar['properties']['Attributes']['Name']] = bar['properties']['Attributes']['SeatsCount']
    #biggest = sorted(bar_name_seats.items(), key=lambda k: -k[1])[0]
    m = max(bar_name_seats.values())
    return [x for x in bar_name_seats.keys() if bar_name_seats[x] == m]

def get_smallest_bar(data):
    bar_name_seats = {}
    for bar in data:
        bar_name_seats[bar['properties']['Attributes']['Name']] = bar['properties']['Attributes']['SeatsCount']
    m = min(bar_name_seats.values())
    return [x for x in bar_name_seats.keys() if bar_name_seats[x] == m]
    


def get_closest_bar(data, longitude, latitude):
    bar_name_place = {}
    for bar in bars:
        bar_name_place[bar['properties']['Attributes']['Name']] = bar['geometry']['coordinates']
        
    long, lat = input('Введите координаты через пробел (долгота, широта): ').split()
    long = float(long)
    lat = float(lat)
    closest = 10000
    for name,c in bar_name_place.items():
        dist = math.sqrt((c[0] - long)**2 + (c[1] - lat)**2)
        if dist < closest:
            closest = dist
            near_bar = {name: closest}
    return near_bar


url = 'https://devman.org/fshare/1503831681/4/'

bars = load_data(url)['features']
