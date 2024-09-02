# data_engineering_sample/extract.py
import requests

def fetch_countries_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()
