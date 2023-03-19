from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here


    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"Moscow"}

    headers = {
        "X-RapidAPI-Key": "988a3fca0fmsh09ec1fe9f3d9263p1ec578jsne8d811aac699",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
