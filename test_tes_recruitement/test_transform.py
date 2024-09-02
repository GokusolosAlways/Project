# tests/test_transform.py

from tes_recruitement.transform import transform_countries_data

def test_transform_countries_data():
    sample_data = [
        {
            "name": {"common": "Country A"},
            "population": 1000000,
            "area": 50000,
            "region": "Region A"
        },
        {
            "name": {"common": "Country B"},
            "population": 2000000,
            "area": 100000,
            "region": "Region B"
        }
    ]
    result = transform_countries_data(sample_data)
    assert result == [
        {"name": "Country A", "population": 1000000, "area": 50000, "region": "Region A"},
        {"name": "Country B", "population": 2000000, "area": 100000, "region": "Region B"},
    ]

