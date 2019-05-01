import pytest
from meteorites.avg import MeteoriteStats
def test_average_mass():
    m = MeteoriteStats()
    data = m.get_data()
    assert m.average_mass(data) == 50190.19568930039
