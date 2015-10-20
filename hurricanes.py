import requests
import requests_mock
import json
import os


my_secret_key = os.environ[WUNDERKEY]



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


def main():
    call = SearchHurricanes(zipcode)
    res = call.run()
    print(res.text)


if __name__ == '__main__':
    main()
