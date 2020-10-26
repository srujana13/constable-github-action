import requests
import json
from config import FIREBASE_BASE_URL

class Badge:
    def __init__(self, _path: str) -> str:
            self.path = _path

    def get_shield_url(self, grade: str) -> str:   
        """
        _path: username/repositoryname/branch 
        e.g: ayushjain94/constable/master
        grade: A+
        """

        payload = {"grade": grade}
        url = '{}/{}.json'.format(FIREBASE_BASE_URL, self.path)
        r = requests.put(url, data = json.dumps(payload)) 
        shield = "https://img.shields.io/badge/dynamic/json?label=Constable&query=$.grade&url={data_url}".format(data_url = url)
        return shield
