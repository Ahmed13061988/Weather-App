from flask import Flask, render_template

web_page = Flask("Weather")


@web_page.route("/")
def home():
    return render_template("tutorial.html")


@web_page.route("/about/")
def about():
    return render_template("about.html")


web_page.run()
