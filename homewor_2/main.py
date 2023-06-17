from flask import Flask, request
from PythonPro.project.flask_home.utils import generate_customers, space_numbers


app = Flask(__name__)


@app.route("/requirements")
def requirements():
    f = open('requirements.txt')
    return f.read()


@app.route("/generate-users")
def generate_users():
    lenght = request.args.get('lenght', '100')
    if lenght.isdigit():
        lenght = int(lenght)
        if lenght > 200:
            return 'Lenght should be less than 100'
    else:
        return f'Invalid lenght value: {lenght}'
    return generate_customers(lenght)


@app.route("/space")
def space():
    return space_numbers()


if __name__ == '__main__':
    app.run()
