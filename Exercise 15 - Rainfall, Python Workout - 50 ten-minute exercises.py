# Specifically, write a function, get_rainfall, that tracks rainfall
# in a number of cities. Users of your program will enter the name of
# a city; if the city name is blank, then the function prints a report
# (which I’ll describe) before exiting. If the city name isn’t blank,
# then the program should also ask the user how much rain has fallen
# in that city (typically measured in millimeters). After the user
# enters the quantity of rain, the program again asks them for
# a city name, rainfall amount, and so on--until the user presses
# Enter instead of typing the name of a city. When the user enters
# a blank city name, the program exits--but first, it reports how
# much total rainfall there was in each city. Thus, if I enter
#
# Boston
# 5
# New York
# 7
# Boston
# 5
# [Enter; blank line] the program should output
# Boston: 10
# New York: 7
#
# The order in which the cities appear is not important, and the cities
# aren’t known to the program in advance.


def get_rainfall():
    cities_list = []
    rainfall_list = []
    program = True
    while program:
        city_input = input('Enter the name of a city: ')
        rainfall_amount = input('Enter the rainfall amount: ')
        if city_input != '':
            cities_list.append(city_input)
            rainfall_list.append(rainfall_amount)
        elif city_input == '':
            # data = [item for sublist in zip(cities_list, rainfall_list) for item in sublist]
            # print(data)
            i = cities_list.index(cities_list[-1])
            for y in range(0, i+1):
                print(f'{cities_list[y]}: {rainfall_list[y]}')
            break

get_rainfall()

# Book solution:
# def get_rainfall():
#     rainfall = {}
#
#     while True:
#         city_name = input('Enter city name: ')
#         if not city_name:
#             break
#
#         mm_rain = input('Enter mm rain: ')
#         rainfall[city_name] = rainfall.get(city_name,
#                                            0) + int(mm_rain)
#
#         for city, rain in rainfall.items():
#             print(f'{city}: {rain}')
#
# get_rainfall()
