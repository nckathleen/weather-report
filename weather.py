import os
import requests


my_key = os.environ['WUNDERKEY']


class SearchConditions:

    '''Look for current weather conditions for given zip-code.'''

    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{key}/conditions/q/{zipcode}.json'.format(
            key=my_key,
            zipcode=self.q_string)
        res = requests.get(url).json()
        # if res.status_code == 200:
        #     with open('weather_stats.json', 'w') as f:
        #         f.write(res.text)
        # else:
        #     print(res.status_code)

        curr_place = res['current_observation']['display_location']['full']
        curr_weather = res['current_observation']['weather']
        curr_temp = res['current_observation']['temp_f']
        curr_humidity = res['current_observation']['relative_humidity']
        curr_feel = res['current_observation']['feelslike_f']
        curr_wind = res['current_observation']['wind_mph']
        curr_time = res['current_observation']['observation_time']

        print(curr_time)
        print("In {} it is currently {} and {}°.".format(curr_place, curr_weather, curr_temp))
        print("The relative humidity is {}.".format(curr_humidity))
        print("Winds are at {} mph.".format(curr_wind))
        print("With the humidity and wind, it actually feels like {}.".format(curr_feel))
        print ("")

        return res
#
# class SearchTenDay:
#
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     def run(self):
#         url = 'http://api.wunderground.com/api/{key}/forecast10day/q/{zipcode}.json'.format(
#             zipcode=self.q_string, key=my_key)
#         res = requests.get(url)
#
#         for day in res['forecast']['txt_forecast']['forecastday']:
#             self.periods.append(day['fcttext'])
#
#
# class SearchAlerts():
#
#     ''' Look for any weather alerts for the given zip-code.'''
#
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     def run(self):
#         url = 'http://api.wunderground.com/api/{key}/alerts/q/{zipcode}.json'.format(
#             zipcode=self.q_string, key=my_key)
#         res = requests.get(url)
#
#
#         if not res['alerts']:
#             print("There are no current alerts for your area.")
#         else:
#             alert_type = res['alerts'][0]['description']
#             alert_expire = res['alerts'][0]['expires']
#             alert_msg = res['alerts'][0]['message']
#             print("There is a {} for your area, which expires at {}.".format(alert_type, alert_expire))
#             print(alert_msg)
#
#         return res

#
# class SearchHurricanes:
#
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     def run(self):
#         url = 'http://api.wunderground.com/api/{key}/currenthurricane/q/{zipcode}.json'.format(
#             zipcode=self.q_string, key=my_key)
#         res = requests.get(url)
#
#         return hurricane

#
# class SearchSun():
#
#     ''' Give sunrise and sunset times for the given zip-code'''
#
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#
#     def run(self):
#         url = 'http://api.wunderground.com/api/{key}/astronomy/q/{zipcode}.json'.format(
#             zipcode=self.q_string, key=my_key)
#         res = requests.get(url)
#
#         sunrise = res['sun_phase']['sunrise']['hour']
#         sunset = res['sun_phase']['sunset']['hour']
#
#         print("Today sunrise is at {}.".format(sunrise))
#         print("Today sunset is at {}.".format(sunset))
#
#         return res
