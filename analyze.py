"""
FlightProject - Quick Business Insights from flight_data.csv
"""

import pandas as pd

# Load the CSV we saved earlier
df = pd.read_csv("flight_data.csv")

print("=" * 50)
print("BASIC OVERVIEW")
print("=" * 50)
print(f"Total flights: {len(df)}")
print(f"Airlines covered: {df['airline_name'].nunique()}")
print(f"Flight statuses: {df['flight_status'].unique()}")

print("\n" + "=" * 50)
print("FLIGHT STATUS BREAKDOWN")
print("=" * 50)
print(df['flight_status'].value_counts())

print("\n" + "=" * 50)
print("TOP 10 AIRLINES BY NUMBER OF FLIGHTS")
print("=" * 50)
print(df['airline_name'].value_counts().head(10))

print("\n" + "=" * 50)
print("AVERAGE ARRIVAL DELAY (minutes) - TOP 10 AIRLINES")
print("=" * 50)
avg_delay = df.groupby('airline_name')['arrival_delay'].mean().sort_values(ascending=False)
print(avg_delay.head(10))

print("\n" + "=" * 50)
print("BUSIEST DEPARTURE AIRPORTS")
print("=" * 50)
print(df['departure_airport'].value_counts().head(10))

print("\n" + "=" * 50)
print("FLIGHTS WITH DELAYS > 30 MIN")
print("=" * 50)
delayed = df[df['arrival_delay'] > 30]
print(f"Count: {len(delayed)} out of {len(df)} ({len(delayed)/len(df)*100:.1f}%)")