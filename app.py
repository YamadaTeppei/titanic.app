from flask import Flask,render_template,request,redirect, url_for
import pandas as pd
app = Flask(__name__)
# topページ
@app.route("/")
def top():
    return render_template("top.html")

@app.route("/train/", methods=["GET", "POST"])
def train():
    if request.method == "GET":
        titanic_train = pd.read_csv("models/train_clean.csv")
        return render_template("train.html", titanic_train=titanic_train)
    else:
        pass
if __name__ == '__main__':
    app.secret_key = "jijjkla"
    app.run()
