import os
import json
import requests
from dotenv import load_dotenv


# This gets fuel type data from the EIA API – the same API we looked at in the previous interview
# Results are cached for speed of development, and to ensure results are deterministic
# You don't need to change this function
def get_data(start_date: str, end_date: str, use_cache=True):
    cache_filepath = os.path.join(os.path.dirname(__file__), "cache", f"response_{start_date}_{end_date}.json")
    if use_cache and os.path.exists(cache_filepath):
        with open(cache_filepath, "r") as f:
            print(f"Loading from cache for {start_date} to {end_date}")
            return json.load(f)
    else:
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path=env_path)
        url = "https://api.eia.gov/v2/electricity/rto/fuel-type-data/data/"
        response = requests.get(url, params={
            "api_key": os.getenv("USA_EIA_API_KEY"),
            "frequency": "hourly", 
            "data[0]": "value",
            "facets[respondent][]": "BPAT",
            "start": start_date,
            "end": end_date,
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "offset": 0,
            "length": 5000
        })
        with open(cache_filepath, "w") as f:
            print(f"Saving to cache for {start_date} to {end_date}")
            json.dump(response.json(), f)
        return response.json()
    
    
def produce_csv(output_filepath: str = os.path.join(os.path.dirname(__file__), "hourly_carbon_intensity_july_2025.csv")) -> None:
    response_json = get_data("2025-07-01T01", "2025-07-31T23", use_cache=True)

    # Question:
    # 
    # Fuel type data from eia.gov is requested above – this is queried from the same portal we looked at in the previous interview
    # 
    # Please process the data from this API to produce a CSV called hourly_carbon_intensity_july_2025.csv in the current directory with the following columns:
    # 
    # - year (string as 2025)
    # - month (string as 01, 02, 03, etc)
    # - day (string as 01, 02, 03, etc)
    # - hour (string as 01, 02, 03, etc)
    # - tonnes_co2e_per_kwh (float)
    # The CSV must be sorted by year, month, day, hour in ascending order and should not include an index column.


if __name__ == "__main__":
    produce_csv()
