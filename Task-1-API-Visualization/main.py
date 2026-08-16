# ============================================================
# TASK 1 - API INTEGRATION AND DATA VISUALIZATION
# Project: Weather Data Analysis Dashboard
# ============================================================

# Import required libraries
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime


# ============================================================
# 1. CONFIGURATION
# ============================================================

# Coordinates for New Delhi, India
# These can be changed to another city later.
LATITUDE = 28.6139
LONGITUDE = 77.2090

# Number of previous days to retrieve
FORECAST_DAYS = 7

# API URL
API_URL = "https://api.open-meteo.com/v1/forecast"


# ============================================================
# 2. CREATE REQUIRED DIRECTORIES
# ============================================================

os.makedirs("data", exist_ok=True)
os.makedirs("dashboard", exist_ok=True)


# ============================================================
# 3. FETCH DATA FROM PUBLIC API
# ============================================================

def fetch_weather_data():
    """
    Fetch weather information from the Open-Meteo public API.

    Returns:
        dict: Weather data returned by the API.
    """

    parameters = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "hourly": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "surface_pressure,"
            "wind_speed_10m"
        ),
        "forecast_days": FORECAST_DAYS,
        "timezone": "auto"
    }

    print("Connecting to weather API...")

    try:
        response = requests.get(
            API_URL,
            params=parameters,
            timeout=10
        )

        # Raise an error if the API request failed
        response.raise_for_status()

        print("Weather data fetched successfully.")

        return response.json()

    except requests.exceptions.RequestException as error:
        print("Error while connecting to API:")
        print(error)
        return None


# ============================================================
# 4. CONVERT API DATA INTO PANDAS DATAFRAME
# ============================================================

def convert_to_dataframe(weather_data):
    """
    Convert the JSON weather response into a Pandas DataFrame.
    """

    if weather_data is None:
        return None

    hourly_data = weather_data["hourly"]

    dataframe = pd.DataFrame({
        "DateTime": hourly_data["time"],
        "Temperature_C": hourly_data["temperature_2m"],
        "Humidity_Percent": hourly_data["relative_humidity_2m"],
        "Feels_Like_C": hourly_data["apparent_temperature"],
        "Pressure_hPa": hourly_data["surface_pressure"],
        "Wind_Speed_kmh": hourly_data["wind_speed_10m"]
    })

    # Convert DateTime column into datetime format
    dataframe["DateTime"] = pd.to_datetime(
        dataframe["DateTime"]
    )

    return dataframe


# ============================================================
# 5. SAVE DATA TO CSV
# ============================================================

def save_data(dataframe):
    """
    Save weather data into a CSV file.
    """

    file_path = "data/weather_data.csv"

    dataframe.to_csv(
        file_path,
        index=False
    )

    print(f"Data saved successfully to: {file_path}")


# ============================================================
# 6. ANALYZE WEATHER DATA
# ============================================================

def analyze_data(dataframe):
    """
    Perform basic statistical analysis on weather data.
    """

    print("\n" + "=" * 60)
    print("WEATHER DATA ANALYSIS")
    print("=" * 60)

    # Temperature analysis
    max_temperature = dataframe["Temperature_C"].max()
    min_temperature = dataframe["Temperature_C"].min()
    average_temperature = dataframe["Temperature_C"].mean()

    # Humidity analysis
    average_humidity = dataframe["Humidity_Percent"].mean()

    # Wind analysis
    maximum_wind = dataframe["Wind_Speed_kmh"].max()
    average_wind = dataframe["Wind_Speed_kmh"].mean()

    # Pressure analysis
    average_pressure = dataframe["Pressure_hPa"].mean()

    print(f"Maximum Temperature : {max_temperature:.2f} °C")
    print(f"Minimum Temperature : {min_temperature:.2f} °C")
    print(f"Average Temperature : {average_temperature:.2f} °C")
    print(f"Average Humidity    : {average_humidity:.2f} %")
    print(f"Maximum Wind Speed  : {maximum_wind:.2f} km/h")
    print(f"Average Wind Speed  : {average_wind:.2f} km/h")
    print(f"Average Pressure    : {average_pressure:.2f} hPa")

    print("=" * 60)


# ============================================================
# 7. CREATE VISUALIZATION DASHBOARD
# ============================================================

def create_dashboard(dataframe):
    """
    Create a weather visualization dashboard
    using Matplotlib and Seaborn.
    """

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")

    # Create a figure with four charts
    figure, axes = plt.subplots(
        2,
        2,
        figsize=(16, 10)
    )

    # --------------------------------------------------------
    # Chart 1: Temperature
    # --------------------------------------------------------

    axes[0, 0].plot(
        dataframe["DateTime"],
        dataframe["Temperature_C"],
        label="Temperature",
        linewidth=2
    )

    axes[0, 0].plot(
        dataframe["DateTime"],
        dataframe["Feels_Like_C"],
        label="Feels Like",
        linestyle="--"
    )

    axes[0, 0].set_title(
        "Temperature Trend"
    )

    axes[0, 0].set_xlabel("Date and Time")
    axes[0, 0].set_ylabel("Temperature (°C)")
    axes[0, 0].legend()

    # --------------------------------------------------------
    # Chart 2: Humidity
    # --------------------------------------------------------

    axes[0, 1].plot(
        dataframe["DateTime"],
        dataframe["Humidity_Percent"],
        linewidth=2
    )

    axes[0, 1].set_title(
        "Humidity Trend"
    )

    axes[0, 1].set_xlabel("Date and Time")
    axes[0, 1].set_ylabel("Humidity (%)")

    # --------------------------------------------------------
    # Chart 3: Wind Speed
    # --------------------------------------------------------

    axes[1, 0].plot(
        dataframe["DateTime"],
        dataframe["Wind_Speed_kmh"],
        linewidth=2
    )

    axes[1, 0].set_title(
        "Wind Speed Trend"
    )

    axes[1, 0].set_xlabel("Date and Time")
    axes[1, 0].set_ylabel("Wind Speed (km/h)")

    # --------------------------------------------------------
    # Chart 4: Atmospheric Pressure
    # --------------------------------------------------------

    axes[1, 1].plot(
        dataframe["DateTime"],
        dataframe["Pressure_hPa"],
        linewidth=2
    )

    axes[1, 1].set_title(
        "Atmospheric Pressure"
    )

    axes[1, 1].set_xlabel("Date and Time")
    axes[1, 1].set_ylabel("Pressure (hPa)")

    # --------------------------------------------------------
    # Dashboard title
    # --------------------------------------------------------

    figure.suptitle(
        "Weather Data Analysis Dashboard",
        fontsize=20,
        fontweight="bold"
    )

    # Automatically adjust spacing
    figure.tight_layout(
        rect=[0, 0, 1, 0.96]
    )

    # Save dashboard
    dashboard_path = "dashboard/weather_dashboard.png"

    plt.savefig(
        dashboard_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(
        f"\nDashboard saved successfully to: {dashboard_path}"
    )

    # Display dashboard
    plt.show()


# ============================================================
# 8. MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)
    print("WEATHER DATA ANALYSIS AND VISUALIZATION")
    print("=" * 60)

    # Fetch API data
    weather_data = fetch_weather_data()

    if weather_data is None:
        print("Unable to retrieve weather data.")
        return

    # Convert API data to DataFrame
    dataframe = convert_to_dataframe(
        weather_data
    )

    if dataframe is None:
        print("Unable to process weather data.")
        return

    # Display first five records
    print("\nFirst 5 records:")
    print(dataframe.head())

    # Save data
    save_data(dataframe)

    # Analyze data
    analyze_data(dataframe)

    # Create dashboard
    create_dashboard(dataframe)

    print("\nTask 1 completed successfully!")


# ============================================================
# 9. PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()