from flask import Flask, render_template, request # type: ignore
from waitress import serve

from whether import get_weather


app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city, "$DDFDT-fdgfdg")
        return render_template('weather.html',
                            title = weather_data['title'],
                            status = weather_data['status'],
                           )
    return render_template('weather.html')

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
