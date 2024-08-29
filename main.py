from flask import Flask, render_template
import pandas as pd
import numpy as np

web_page = Flask(__name__)

variable = "Hello World"

stations = pd.read_csv("data_small/stations.txt", skiprows=17)

stations = stations[["STAID", "STANAME                                 "]]


@web_page.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


@web_page.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv(f"data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20, parse_dates=["    DATE"])
    df["TG0"] = df['   TG'].mask(df["   TG"] == -9999, np.nan)
    temperature = df.loc[df["    DATE"] == date]["TG0"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


@web_page.route("/api/v1/<station>")
def station(station):
    df = pd.read_csv(f"data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20,
                     parse_dates=["    DATE"]).squeeze()
    station_dict = df.to_dict(orient="records")
    return station_dict


@web_page.route("/api/v1/annual/<station>/<year>")
def yearly(station,year):
    df = pd.read_csv(f"data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))]
    result = result.to_dict(orient="records")
    return result


if __name__ == "__main__":
    web_page.run(debug=True)
