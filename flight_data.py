"""
FlightProject - Real-Time Flight Data Analysis
Business Analyst intern project using AviationStack API
"""

import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# AviationStack API endpoint for real-time flights
BASE_URL = "http://api.aviationstack.com/v1/flights"

def fetch_flight_data(limit=100):
    """
    Fetches real-time flight data from AviationStack API.
    limit: number of records to fetch (free plan = 100 requests/month total, be careful)
    """
    params = {
        "access_key": API_KEY,
        "limit": limit
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return []


def process_flight_data(raw_data):
    """
    Converts raw JSON flight data into a clean pandas DataFrame
    with only the columns useful for business analysis.
    """
    records = []

    for flight in raw_data:
        records.append({
            "flight_date": flight.get("flight_date"),
            "flight_status": flight.get("flight_status"),
            "airline_name": flight.get("airline", {}).get("name"),
            "flight_number": flight.get("flight", {}).get("iata"),
            "departure_airport": flight.get("departure", {}).get("airport"),
            "departure_scheduled": flight.get("departure", {}).get("scheduled"),
            "departure_delay": flight.get("departure", {}).get("delay"),
            "arrival_airport": flight.get("arrival", {}).get("airport"),
            "arrival_scheduled": flight.get("arrival", {}).get("scheduled"),
            "arrival_delay": flight.get("arrival", {}).get("delay"),
        })

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    print("Fetching flight data...")
    raw_data = fetch_flight_data(limit=100)

    if raw_data:
        df = process_flight_data(raw_data)
        print(f"Fetched {len(df)} flight records.")
        print(df.head())

        # Save to CSV for Power BI / Excel analysis later
        df.to_csv("flight_data.csv", index=False)
        print("Saved to flight_data.csv")
    else:
        print("No data fetched. Check your API key or plan limits.")