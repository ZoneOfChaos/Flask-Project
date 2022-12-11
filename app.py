from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page" + name + "--" + str(id)

if __name__ == '__main__':
    app.run(debug=True)
