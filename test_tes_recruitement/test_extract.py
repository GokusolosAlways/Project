# tests/test_extract.py

import pytest
import requests
from tes_recruitement.extract import fetch_countries_data

def test_fetch_countries_data():
    data = fetch_countries_data()
    assert isinstance(data, list)
    assert len(data) > 0