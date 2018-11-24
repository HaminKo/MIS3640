import json
import urllib.request
import pprint

YAHOO_WEATHER_URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Wellesley%2C%20MA%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode('utf-8')
        response_data = json.loads(response_text)

    return response_data


def main():
    weather_json = get_json(YAHOO_WEATHER_URL)
    # pprint.pprint(weather_json)
    today = weather_json['query']['results']['channel']['item']['forecast'][0]
    print(f"High: {today['high']}, Low: {today['low']}, Desc: {today['text']}")


if __name__ == '__main__':
    main()
