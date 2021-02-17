import requests
import json
from enum import Enum
from main.filters.utils import *


# from main.filters.utils import Labels

class Labels(Enum):
    APPROPRIATE = "appropriate"
    INAPPROPRIATE = "inappropriate"


class ApiFilter:

    def __init__(self):
        self.tokenKey = None
        self.base_url = "http://api.text-mining.ir/api/"
        self.api_key = "66c4f682-e66d-eb11-80ed-98ded002619b"
        self.is_ready = False
        self.__get_token()

    def __get_token(self):
        try:
            url = self.base_url + "Token/GetToken"
            querystring = {"apikey": self.api_key}
            response = requests.request("GET", url, params=querystring)
            data = json.loads(response.text)
            self.tokenKey = data['token']
            self.is_ready = True
        except requests.exceptions.ConnectionError:
            Logger.warn("Failed to build api filter")

    def __call_api(self, url, data):
        try:
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + self.tokenKey,
                'Cache-Control': "no-cache"
            }
            response = requests.request("POST", url, data=data.encode("utf-8"), headers=headers)
            return response.text  # return utfReverse(response.text.encode("utf-8"))
        except requests.exceptions.ConnectionError:
            Logger.warn("Failed to call api filter")

    def predict(self, bio):
        if self.is_ready:
            Logger.info("predicting using api filter")
            url = self.base_url + "TextRefinement/SwearWordTagger"
            bio = U'"{}"'.format(bio)
            payload = bio
            response = self.__call_api(url, payload)
            if response:
                result = json.loads(self.__call_api(url, payload))
                for v in result.values():
                    if v in ['StrongSwearWord', 'MildSwearWord']:
                        predicted_label = Labels.INAPPROPRIATE.value
                        break
                else:
                    predicted_label = Labels.APPROPRIATE.value

                return {
                    'predicted_label': predicted_label,
                    'probability': '1'
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


# requests.exceptions.ConnectionError:
