from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route('/<City>')
def index(City):  # put application's code here


    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": City}

    headers = {
        "X-RapidAPI-Key": "988a3fca0fmsh09ec1fe9f3d9263p1ec578jsne8d811aac699",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    list_of_data = json.loads(response.content)

    data = {
        'city_code': str(list_of_data['location']['name']),
        'country_code': str(list_of_data['location']['region']),
        'local_time': str(list_of_data['location']['localtime']),
        'icon': str(list_of_data['current']['condition']['icon']),
        'current_temp': str(list_of_data['current']['temp_c']),
        'wind_speed': str(list_of_data['current']['wind_kph']),
        'wind_direction': str(list_of_data['current']['wind_dir']),
        'feels_like_c': str(list_of_data['current']['feelslike_c']),
        'humidity': str(list_of_data['current']['humidity']),
        'vis_km': str(list_of_data['current']['vis_km']),
        'uv_index': str(list_of_data['current']['uv'])

    }

    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
