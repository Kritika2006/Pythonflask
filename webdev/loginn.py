from flask import Flask, render_template, redirect, url_for, request

#creating an instance of class
app = Flask(__name__)

#home page
@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__ == "__main__":
    app.run()

