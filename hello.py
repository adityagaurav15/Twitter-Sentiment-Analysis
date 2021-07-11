from flask import Flask, render_template, request, redirect, url_for
from tweet import SentimentAnalysis

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get_analysis", methods=["GET", "POST"])
def get_analysis():
    if request.method == "POST":

        user_id = request.form["userid"]
        hashtag = int(request.form["hashtag"])

        sentiment_analysis = SentimentAnalysis()
        result = sentiment_analysis.DownloadData(user_id, hashtag)
        print("I was called")
        return render_template("sentiment.html", code=result)
    else:
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()
