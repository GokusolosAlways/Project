# tests/test_load.py
import json
import os
from tes_recruitement.load import  save_to_json

def test_save_to_json():
    sample_data = [
        {"name": "Country A", "population": 1000000, "area": 50000, "region": "Region A"},
        {"name": "Country B", "population": 2000000, "area": 100000, "region": "Region B"},
    ]
    filename = "test_output.json"
    save_to_json(sample_data, filename)
    assert os.path.exists(filename)

    with open(filename) as f:
        data = json.load(f)
        assert data == sample_data

    os.remove(filename)
