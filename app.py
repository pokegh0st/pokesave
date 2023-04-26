from flask import Flask, render_template, request, redirect, abort
from pytube import YouTube

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("videoUrl")
        yt = YouTube(link)
        try:
            streams = yt.streams.filter(progressive=True, file_extension='mp4')
            return render_template("download.html", streams=streams)
        except:
            return render_template("index.html", error="Try to chill a bit, pops.")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
