from flask import Flask, render_template

web_page = Flask(__name__)


@web_page.route("/")
def home():
    return render_template("home.html")


@web_page.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    web_page.run(debug=True)
