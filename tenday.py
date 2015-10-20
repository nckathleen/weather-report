import requests
import requests_mock
import json
import os


my_secret_key = os.environ[WUNDERKEY]



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
    call = SearchTenday(zipcode)
    res = call.run()
    print(res.text)


if __name__ == '__main__':
    main()