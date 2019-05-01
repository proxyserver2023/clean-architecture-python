import urllib.request
import json
from calc import calc


class MeteoriteStats:
    def get_data(self):
        URL = ("https://data.nasa.gov/resource/y77d-th95.json")

        with urllib.request.urlopen(URL) as url:
            data = json.loads(url.read().decode())
        return data

    def average_mass(self, data):
        masses = [float(d['mass']) for d in data if 'mass' in d]
        print(masses)

        avg_mass = calc.Calc().avg(*masses)
        return avg_mass
