import requests

def get_weather(city_name, api_key):
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    # response = requests.get(complete_url)
    # data = response.json()
    
    if city_name != "":
        status = "Success"
        return {"title": city_name, "status": status}
    else:
        return {"title": "City Name Not Found", "status": "Failed"}
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "dummy_api_key"  # Replace with your OpenWeatherMap API key
    get_weather(city_name, api_key)