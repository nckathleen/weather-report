import requests
import requests_mock
import json
import os


my_secret_key = os.environ[WUNDERKEY]



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


def main():
    call = SearchConditions(zipcode)
    res = call.run()
    print(res.text)


if __name__ == '__main__':
    main()
