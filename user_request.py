from weather import SearchConditions  #, SearchAlerts, SearchSun
import os

my_key = os.environ['WUNDERKEY']

zipcode = input("Please enter a zip code: ")


SearchConditions(zipcode).run()
# SearchAlerts(zipcode).run()
# SearchSun(zipcode).run()
