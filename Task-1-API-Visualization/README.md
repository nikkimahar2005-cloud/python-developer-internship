# Task 1 - API Integration and Data Visualization

## Project Title

Weather Data Analysis and Visualization Dashboard

## Objective

The objective of this project is to fetch weather data from a public API using Python, analyze the collected data, and create visualizations using Matplotlib and Seaborn.

## Technologies Used

- Python
- Requests
- Pandas
- Matplotlib
- Seaborn
- Open-Meteo API

## Project Features

- Fetches weather data from a public API
- Processes API data using Pandas
- Stores processed data in CSV format
- Calculates weather statistics
- Visualizes temperature trends
- Visualizes humidity trends
- Visualizes wind speed
- Visualizes atmospheric pressure
- Generates a weather visualization dashboard

## Project Structure

```text
Task-1-API-Visualization/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── weather_data.csv
│
└── dashboard/
    └── weather_dashboard.png
```

## How to Run

### Step 1 - Install Required Libraries

Open the terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 2 - Run the Program

```bash
python main.py
```

## Output

After successful execution, the program generates:

### Weather Data

```text
data/weather_data.csv
```

This file contains the weather data retrieved from the API.

### Visualization Dashboard

```text
dashboard/weather_dashboard.png
```

The dashboard contains visualizations for:

- Temperature
- Feels-like temperature
- Humidity
- Wind speed
- Atmospheric pressure

## Working Process

```text
Public Weather API
        ↓
Fetch Weather Data
        ↓
Convert Data into DataFrame
        ↓
Analyze Weather Data
        ↓
Save Data as CSV
        ↓
Create Visualizations
        ↓
Generate Dashboard
```

## Conclusion

This project demonstrates how Python can be used to integrate data from a public API, process and analyze the data using Pandas, and create meaningful visualizations using Matplotlib and Seaborn.

## Internship Task

Task 1 - API Integration and Data Visualization