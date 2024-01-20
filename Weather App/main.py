import tkinter as tk
from tkinter import messagebox, font, Toplevel
from datetime import datetime
import requests
import json

class WeatherViewer:
    def __init__(self, weather_api_key):
        self.api_key = weather_api_key
        self.weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
        self.setup_ui()

    def fetch_weather_data(self, city_name):
        try:
            request_params = {
                "q": city_name,
                "appid": self.api_key,
                "units": "metric"
            }

            api_response = requests.get(self.weather_api_url, params=request_params)
            weather_data = json.loads(api_response.text)

            if api_response.status_code == 200:
                self.show_weather_details(city_name, weather_data)
            else:
                messagebox.showerror("Error", "Failed to retrieve weather data.")

        except Exception as error:
            messagebox.showerror("Error", f"An error occurred: {str(error)}")

    def show_weather_details(self, city, weather_data):
        weather_window = Toplevel(self.main_window)
        weather_window.title(f"Weather in {city}")
        weather_window.geometry("400x300")

        info_font = font.Font(family="Helvetica", size=12)

        details = self.extract_weather_details(weather_data)

        for detail in details:
            tk.Label(weather_window, text=detail, font=info_font).pack(pady=5)

        tk.Button(weather_window, text="Close", command=weather_window.destroy).pack(pady=10)

    def extract_weather_details(self, weather_data):
        details = [
            f"Temperature: {weather_data['main']['temp']}°C",
            f"Humidity: {weather_data['main']['humidity']}%",
            f"Description: {weather_data['weather'][0]['description']}",
            f"Wind Speed: {weather_data['wind']['speed']} m/s",
            f"Pressure: {weather_data['main']['pressure']} hPa",
            f"Visibility: {weather_data.get('visibility', 'N/A')} meters",
            f"Cloudiness: {weather_data['clouds']['all']}%",
            f"Sunrise: {datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%H:%M:%S')}",
            f"Sunset: {datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%H:%M:%S')}",
            f"Coordinates: Lat: {weather_data['coord']['lat']}, Lon: {weather_data['coord']['lon']}"
        ]
        return details

    def setup_ui(self):
        self.main_window = tk.Tk()
        self.main_window.title("Weather Viewer 🌤️")
        self.configure_main_window()

        input_frame = tk.Frame(self.main_window, bg='#ADD8E6')
        input_frame.pack(pady=20)

        control_frame = tk.Frame(self.main_window, bg='#ADD8E6')
        control_frame.pack(pady=20)

        tk.Label(input_frame, text="Enter City Name:", font=self.default_font, bg='#ADD8E6').pack()
        self.city_name_entry = tk.Entry(input_frame, font=self.default_font)
        self.city_name_entry.pack(pady=5)

        # Button customization
        button_style = {'font': self.default_font, 'bg': '#90EE90', 'fg': 'black', 'height': 2, 'width': 15}

        weather_button = tk.Button(control_frame, text="Get Weather 🌥️", **button_style, command=self.retrieve_weather)
        exit_button = tk.Button(control_frame, text="Exit ❌", **button_style, command=self.main_window.quit)

        # Adjusting layout and spacing
        weather_button.pack(side=tk.LEFT, padx=10, pady=10)
        exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.main_window.mainloop()

    def configure_main_window(self):
        window_width, window_height = 600, 400
        screen_width, screen_height = self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()
        center_x, center_y = int(screen_width / 2 - window_width / 2), int(screen_height / 2 - window_height / 2)
        self.main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.main_window.configure(background='#ADD8E6')
        self.default_font = font.Font(family="Helvetica", size=12)

    def retrieve_weather(self):
        city_name = self.city_name_entry.get()
        self.fetch_weather_data(city_name)


if __name__ == "__main__":
    api_key = "7d81a319292decb1a2730e030fc76219"  # Replace with your API key
    weather_app = WeatherViewer(api_key)
