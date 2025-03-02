from flask import Flask


application = Flask(__name__)


@application.route('/')
def hello_world():
    return ('<h1>Witaj, BigData z Pythonem!</h1><p>Przykład CI/CD - automatyczne wdrożenie!</p><p>Bartosz Bryniarski</p>')


if __name__ == '__main__':
    application.run(debug=True)