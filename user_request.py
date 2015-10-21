from weather import SearchConditions
import os

my_secret_key = os.environ['WUNDERKEY']

zipcode = input("Please enter a zip code: ")

# while True:
#     choice = input(
#         "What information would you like for zipcode {}?".format(zipcode))
#     print("Current Conditions - choose 1\n10 - day Forecast - choose 2\nWeather Alerts - choose 3\nSunrise and Sunset Times - choose 4\nHurricane Information - choose 5")
#     if choice not in ('1','2','3','4','5'):
#         print("Not an appropriate choice.")
#     else:
#         break



SearchConditions(zipcode).run()
