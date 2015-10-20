import requests
import requests_mock
import json
import os


my_secret_key = os.environ[WUNDERKEY]


class SearchAlerts:

    def __init__(self, q_string):
        self.q_string = q_string

    zipcode = input()
    def run(self):
        url = 'http://api.wunderground.com/api/my_secret_key/alerts/q/{}.json'.format(
            zipcode)
        res = requests.get(url).json

        return alerts



class SearchConditions:

    def __init__(self, q_string):
        self.q_string = q_string

    zipcode = input()
    def run(self):
        url = 'http://api.wunderground.com/api/my_secret_key/conditions/q/{}.json'.format(
            zipcode)
        res = requests.get(url).json

        # album = res['albums'][0]['name']
        # artist = res['albums'][0]['artists'][0]['name']

        return conditions



class SearchHurricanes:

    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/my_secret_key/currenthurricane/q/{}.json'.format(
            zipcode)
        res = requests.get(url).json
            return
        # album = res['albums'][0]['name']
        artist = res['artists'][0]['name']

        return hurricane



class SearchSun:

    def __init__(self, q_string):
        self.q_string = q_string

    zipcode = input()
    def run(self):
        url = 'http://api.wunderground.com/api/my_secret_key/astronomy/q/{}.json'.format(
            zipcode)
        res = requests.get(url).json

        return sun_rise_set



class SearchTenday:

    def __init__(self, q_string):
        self.q_string = q_string

    zipcode = input()
    def run(self):
        url = 'http://api.wunderground.com/api/my_secret_key/forecast10day/q/{}.json'.format(
            zipcode)
        res = requests.get(url).json

        return ten_day


def main():
    call = SearchAlerts(zipcode)
    res = call.run()
    print(res.text)


if __name__ == '__main__':
    main()
