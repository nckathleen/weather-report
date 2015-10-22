from weather import SearchConditions # , SearchAlerts, SearchSun
import os

my_key = os.environ['WUNDERKEY']

zipcode = input("Please enter a zip code: ")


SearchConditions.run()
# SearchAlerts.run()
# SearchSun(zipcode).run()
