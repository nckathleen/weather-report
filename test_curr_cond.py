import os
import requests_mock
from weather import SearchConditions

my_secret_key = os.environ['WUNDERKEY']

@requests_mock.Mocker()
def test_curr_cond(m):

    with open('fixtures/curr_cond.json') as data:
        data = json.loads(data.read())

    data = SearchConditions('46556')
    res = data.run()
