import os
import requests
import requests_mock
from weather import SearchConditions

my_key = os.environ['WUNDERKEY']

url_46556 = 'http://api.wunderground.com/api/{key}/conditions/q/46556.json'.format(
    key=my_key)


@requests_mock.Mocker()
def test_curr_cond(m):
    with open('fixtures/curr_cond.json', 'w') as expected_result:
        m.get(url_46556, text=expected_result.read())

    conditions = SearchConditions('46556')
    conditions = conditions.check()
    assert conditions.temp_f == 66.6
    assert conditions.weather == 'Clear'

#
# def test_ten_day(m):
#     with open('fixtures/curr_cond.json', 'w') as expected_result:
#         m.get(url, text=expect_result.read())
#
#     conditions = SearchTenDay('46556')
#
#     assert 'High 73F' in forecast.periods[0]  #list of times of day
#     assert 'Low 59F' in forcast.periods[1]
