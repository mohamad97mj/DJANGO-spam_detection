import requests
import json
from enum import Enum


# from main.filters.utils import Labels

class Labels(Enum):
    APPROPRIATE = "appropriate"
    INAPPROPRIATE = "inappropriate"


class ApiFilter:

    def __init__(self):
        self.tokenKey = None
        self.base_url = "http://api.text-mining.ir/api/"
        self.api_key = "66c4f682-e66d-eb11-80ed-98ded002619b"
        self.__get_token()

    def __get_token(self):
        url = self.base_url + "Token/GetToken"
        querystring = {"apikey": self.api_key}
        response = requests.request("GET", url, params=querystring)
        data = json.loads(response.text)
        self.tokenKey = data['token']

    def __call_api(self, url, data):
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.tokenKey,
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", url, data=data.encode("utf-8"), headers=headers)
        return response.text  # return utfReverse(response.text.encode("utf-8"))

    def predict(self, text):
        url = self.base_url + "TextRefinement/SwearWordTagger"
        text = U'"{}"'.format(text)
        payload = text
        result = json.loads(self.__call_api(url, payload))
        for v in result.values():
            if v in ['StrongSwearWord', 'MildSwearWord']:
                predicted_label = Labels.INAPPROPRIATE.value
                break
        else:
            predicted_label = Labels.APPROPRIATE.value

        return {
            'predicted_label': predicted_label,
            'probability': 1
        }


# f = ApiFilter()
# texts = [
#     'سکسی',
#     'سکسی',
#     'سگ',
#     'سگ',
#     'سکسی',
#     'حروم زاده',
#     'سگ',
#     'حروم زاده',
#     'حروم زاده',
#     'سگ',
#     'حروم زاده',
#     'حروم زاده',
# ]
# for t in texts:
#     print(f.predict(t))
