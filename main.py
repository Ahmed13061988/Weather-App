from flask import Flask, render_template
import pandas as pd
import numpy as np

web_page = Flask(__name__)


@web_page.route("/")
def home():
    return render_template("home.html")


@web_page.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv(f"data_small/TG_STAID" + str(station).zfill(6) + ".txt", skiprows=20, parse_dates=["    DATE"])
    df["TG0"] = df['   TG'].mask(df["   TG"] == -9999, np.nan)
    # station = df["STAID"].to_json
    # date = df.loc[df["    DATE"] == date]["    DATE"]
    temperature = df.loc[df["    DATE"] == date]["TG0"].squeeze() / 10
    print(temperature)
    return {"station": station,
            "date": date,
            "temperature": temperature}


# https://github.com/A988/Weather-App.git
if __name__ == "__main__":
    web_page.run(debug=True)
