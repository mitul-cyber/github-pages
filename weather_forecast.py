import requests
import datetime
import matplotlib.pyplot as plt

class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"

    # 1. Get Current Weather
    def get_current_weather(self, city):
        url = f"{self.base_url}weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    # 2. Get 7-Day Forecast
    def get_weekly_forecast(self, city):
        url = f"{self.base_url}forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None

    # 3. Get Temperature for a Given Date
    def get_temperature_on_date(self, city, date):
        forecast = self.get_weekly_forecast(city)
        if forecast:
            for item in forecast["list"]:
                if date in item["dt_txt"]:
                    return item["main"]["temp"]
        return None

    # 4. Get Humidity Level
    def get_humidity(self, city):
        data = self.get_current_weather(city)
        return data["main"]["humidity"] if data else None

    # 5. Get Wind Speed
    def get_wind_speed(self, city):
        data = self.get_current_weather(city)
        return data["wind"]["speed"] if data else None

    # 6. Get Weather Description
    def get_weather_description(self, city):
        data = self.get_current_weather(city)
        return data["weather"][0]["description"] if data else None

    # 7. Get Sunrise Time
    def get_sunrise_time(self, city):
        data = self.get_current_weather(city)
        if data:
            sunrise_timestamp = data["sys"]["sunrise"]
            return datetime.datetime.fromtimestamp(sunrise_timestamp).strftime('%H:%M:%S')
        return None

    # 8. Get Sunset Time
    def get_sunset_time(self, city):
        data = self.get_current_weather(city)
        if data:
            sunset_timestamp = data["sys"]["sunset"]
            return datetime.datetime.fromtimestamp(sunset_timestamp).strftime('%H:%M:%S')
        return None

    # 9. Check if it's Raining
    def is_raining(self, city):
        data = self.get_weather_description(city)
        return "rain" in data.lower() if data else False

    # 10. Get Minimum Temperature of the Day
    def get_min_temp(self, city):
        data = self.get_current_weather(city)
        return data["main"]["temp_min"] if data else None

    # 11. Get Maximum Temperature of the Day
    def get_max_temp(self, city):
        data = self.get_current_weather(city)
        return data["main"]["temp_max"] if data else None

    # 12. Plot Temperature Variation for 5 Days
    def plot_temperature_trend(self, city):
        forecast = self.get_weekly_forecast(city)
        if forecast:
            dates = []
            temps = []
            for item in forecast["list"]:
                dates.append(item["dt_txt"])
                temps.append(item["main"]["temp"])
            
            plt.figure(figsize=(10, 5))
            plt.plot(dates[:10], temps[:10], marker='o', linestyle='-', color='b')
            plt.xticks(rotation=45)
            plt.xlabel("Date and Time")
            plt.ylabel("Temperature (°C)")
            plt.title(f"Temperature Trend in {city}")
            plt.show()

    # 13. Get Pressure
    def get_pressure(self, city):
        data = self.get_current_weather(city)
        return data["main"]["pressure"] if data else None

    # 14. Get Visibility
    def get_visibility(self, city):
        data = self.get_current_weather(city)
        return data["visibility"] if data else None

    # 15. Check if it's Snowing
    def is_snowing(self, city):
        data = self.get_weather_description(city)
        return "snow" in data.lower() if data else False
