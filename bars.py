import requests
import math


def load_data(file):
    return requests.get(file).json()
    
def get_biggest_bar(bars):
    bar_name_seats = {}
    for bar in bars:
        bar_name_seats[bar['properties']['Attributes']['Name']] = bar['properties']['Attributes']['SeatsCount']
    max_bar = max(bar_name_seats.values())
    return [x for x in bar_name_seats.keys() if bar_name_seats[x] == max_bar]

def get_smallest_bar(bars):
    bar_name_seats = {}
    for bar in bars:
        bar_name_seats[bar['properties']['Attributes']['Name']] = bar['properties']['Attributes']['SeatsCount']
    min_bar = min(bar_name_seats.values())
    return [x for x in bar_name_seats.keys() if bar_name_seats[x] == min_bar]
    


def get_closest_bar(data, longitude, latitude):
    bar_name_place = {}
    for bar in bars:
        bar_name_place[bar['properties']['Attributes']['Name']] = bar['geometry']['coordinates']
        
    long = float(longitude)
    lat = float(latitude)
    closest = 10000
    for name,c in bar_name_place.items():
        dist = math.sqrt((c[0] - long)**2 + (c[1] - lat)**2)
        if dist < closest:
            closest = dist
            near_bar = {name: bar_name_place[name]}
    return near_bar


url = 'https://devman.org/fshare/1503831681/4/'

bars = load_data(url)['features']

if __name__ == '__main__':
    input_number = int(input('''Чтобы найти бар с наибольшей вместимостью, нажмите 1\n\
Чтобы найти бар с наименьшей вместимостью, нажмите 2\n\
Чтобый найти ближайший бар, нажмите 3\n'''))

    if  input_number == 1:
        print ('Самый большой бар -',get_biggest_bar(bars))
    if input_number == 2:
        print ('Самый маленький бар-',get_smallest_bar(bars))    
    if input_number == 3:
        longitude=float(input("Введитете долготу: "))
        latitude=float(input("Введитете широту: "))
        print ("Ближайший бар - ",get_closest_bar(bars, longitude, latitude)) 
