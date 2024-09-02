# data_engineering_sample/transform.py

def transform_countries_data(data):
    transformed_data = []
    for country in data:
        transformed_data.append({
            "name": country.get("name", {}).get("common"),
            "population": country.get("population"),
            "area": country.get("area"),
            "region": country.get("region")
        })
    return transformed_data