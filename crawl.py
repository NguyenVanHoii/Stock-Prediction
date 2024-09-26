import requests
import json
import csv

# Define the URL
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&month=2022-12&outputsize=full&apikey=421YOM1NM6H8MNN7"

# Fetch the data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Extracting relevant information
    meta_data = data.get("Meta Data", {})
    time_series = data.get("Time Series (60min)", {})

    # Define the CSV file name
    csv_file = "time_series_data_thang_12_2022.csv"

    # Write the data to a CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the meta data
        writer.writerow(["Meta Data"])
        for key, value in meta_data.items():
            writer.writerow([key, value])
        
        # Write a blank row for separation
        writer.writerow([])
        
        # Write the header for time series data
        header = ["timestamp", "open", "high", "low", "close", "volume"]
        writer.writerow(header)
        
        # Write the time series data
        for timestamp, values in time_series.items():
            row = [
                timestamp,
                values["1. open"],
                values["2. high"],
                values["3. low"],
                values["4. close"],
                values["5. volume"]
            ]
            writer.writerow(row)

    print(f"Data has been written to {csv_file}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
