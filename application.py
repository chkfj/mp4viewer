# coding: utf-8
from video import Video
from settings import settings
from flask import Flask
from flask import render_template
from flask import make_response
import glob
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/videos")
def api_videos():
    videos = find_videos()
    videos_json = render_template("videos.json", videos=videos)
    response = make_response(videos_json)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

def find_videos(mp4_dir=settings["encoded_dir"]):
    return [Video(path) for path in glob.glob(mp4_dir + "/*.mp4")]

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")

