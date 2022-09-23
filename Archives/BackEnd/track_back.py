import requests
import json


class TrackBack:
    def request_localization(self):
        self.code = self.tracking_code.text()

        url = "https://api.linketrack.com/track/json?" \
              "user=teste&" \
              "token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&" \
              f"codigo={self.code}"

        request = requests.request("GET", url).json()

        reque = request['eventos']

        for pontos in reque:
            for valores in pontos:
                self.label_result.setText(f'{pontos[valores]}') 
