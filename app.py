from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api_key = '4aa499f5a5cf5863de109dc38a4ee1fc'
        weather_data = fetch_weather_data(city, api_key)
        return render_template('weather.html', weather_data=weather_data)
    return render_template('index.html')

def fetch_weather_data(city, api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        # Log the error or handle it in a way that makes sense for your application
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == '__main__':
    app.run()
