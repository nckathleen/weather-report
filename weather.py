import requests
import requests_mock
import json
import os

my_secret_key = os.environ['WUNDERKEY']

zipcode = input("Please enter a zip code: ")



class SearchConditions:

    def __init__(self, q_string):
        self.q_string = q_string

    with open('fixtures/curr_cond.json') as data:
        curr_cond = json.loads(data.read())

    def run(self):
        url = 'http://api.wunderground.com/api/{key}/conditions/q/{zipcode}.json'.format(
            zipcode=self.q_string, key=my_secret_key)
        res = requests.get(url).json()

        curr_place = res['current_observation']['display_location']['full']
        curr_weather = res['current_observation']['weather']
        curr_temp = res['current_observation']['temp_f']
        curr_humidity = res['current_observation']['relative_humidity']
        curr_feel = res['current_observation']['feelslike_f']
        curr_wind = res['current_observation']['wind_mph']
        curr_time = res['current_observation']['observation_time']

        print("In {} it is currently {} and {}°.".format(
            curr_place, curr_weather, curr_temp))
        print("The relative humidity is {}, so it feels like {}°, with winds at {}mph.".format(
            curr_humidity, curr_feel, curr_wind))
        print(curr_time)

        # #artist = res['albums'][0]['artists'][0]['name']

        return res



#
# class SearchTenday(request):
#
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     zipcode = input()
#     def run(self):
#         url = 'http://api.wunderground.com/api/my_secret_key/forecast10day/q/{}.json'.format(
#             zipcode)
#         res = requests.get(url).json
#         return ten_day
#
#
# def main():
#     call = SearchTenday(zipcode)
#     res = call.run()
#
#
#



# class SearchAlerts:
#
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     zipcode = input()
#     def run(self):
#         url = 'http://api.wunderground.com/api/my_secret_key/alerts/q/{}.json'.format(
#             zipcode)
#         res = requests.get(url).json
#         return
#         # album = res['albums'][0]['name']
#         # artist = res['artists'][0]['name']
#
#         return alerts
#
#
# def main():
#     call = SearchHurricanes(zipcode)
#     res = call.run()
#     print(res.text)
#
#


#
# class SearchHurricanes:

#     def __init__(self, q_string):
#         self.q_string = q_string
#
#
#     def run(self):
#         url = 'http://api.wunderground.com/api/my_secret_key/currenthurricane/q/{}.json'.format(
#             zipcode)
#         res = requests.get(url).json
#             return
#         # album = res['albums'][0]['name']
#         # artist = res['artists'][0]['name']
#
#         return hurricane
#
#
# def main():
#     call = SearchHurricanes(zipcode)
#     res = call.run()
#     print(res.text)
#
#
# class SearchSun:
#
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     zipcode = input()
#     def run(self):
#         url = 'http://api.wunderground.com/api/my_secret_key/astronomy/q/{}.json'.format(
#             zipcode)
#         res = requests.get(url).json
#
#         return sun_rise_set
#
# def main():
#     call = SearchSun(zipcode)
#     res = call.run()
#     print(res.text)
#


if __name__ == '__main__':
    main()
