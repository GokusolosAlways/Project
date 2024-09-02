# main_pipeline_run.py
from tes_recruitement.extract import fetch_countries_data
from tes_recruitement.transform import transform_countries_data
from tes_recruitement.load import save_to_json

def main():
    data = fetch_countries_data()
    transformed_data = transform_countries_data(data)
    save_to_json(transformed_data)

if __name__ == "__main__":
    main()
