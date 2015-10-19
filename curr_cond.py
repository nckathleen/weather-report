import urllib
import requests
import requests_mock
import json
import os

#
# my_secret_key = os.environ[WUNDERKEY]
#


zipcode = input()

data = 
request.get('http://api.wunderground.com/api/fea49f9828395e54/conditions/q/{}.json'.format(zipcode))
response = urllib2.urlopen(data)
curr_cond = response.read()
print(curr_cond.json())

#
# class SearchAlbums:
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     def run(self):
#         url = 'https://mager-spotify-web.p.mashape.com/search/1/album.json?q={}'.format(self.q_string)
#
#         res = requests.get(url, headers={'X-Mashape-Key': os.environ['MASHAPE_KEY']}).json()
#
#         album = res['albums'][0]['name']
#         artist = res['albums'][0]['artists'][0]['name']
#
#         return artist, album
#
# class SearchCurrent:
#     def __init__(self, q_string):
#         self.q_string = q_string
#
#     def run(self):
#         url = 'https://mager-spotify-web.p.mashape.com/search/1/artist.json?q={}'.format(self.q_string)
#
#         res = requests.get(url, headers={'X-Mashape-Key': os.environ['MASHAPE_KEY']}).json()
#
#         if res.status != 200:
#             return
#         # album = res['albums'][0]['name']
#         artist = res['artists'][0]['name']
#
#         return artist
#
#
#
# def main():
#     call = SearchAlbums('thriller')
#     res = call.run()
#     print(res.text)
#
#
# if __name__ == '__main__':
#     main()