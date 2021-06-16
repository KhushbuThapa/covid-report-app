import requests

import env

RAPID_API_KEY = getattr(env, 'RAPID_API_KEY')

url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

# we are using covid-19 statistics api by Axisbits, it is based on public data by Johns Hopkins CSSE
# and also its FREE!!!
# rapid api link: https://rapidapi.com/axisbits-axisbits-default/api/covid-19-statistics/


# querystring = {"date": "2020-04-16"}

headers = {
    'x-rapidapi-key': RAPID_API_KEY,
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
}

# print(response.json())


def call_api():
    try:
        response = requests.request("GET", url, headers=headers)
        data = response.json()['data']
        return dict(
            last_updated=data['last_update'],
            total_infections=data['confirmed'],
            total_recovered=data['recovered'],
            total_deaths=data['deaths']
        )
    except:
        # bare exception for now
        pass
