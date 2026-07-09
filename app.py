from flask import Flask, render_template, request

from mpesa import stk_push

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/pay", methods=["POST"])
def pay():

    phone = request.form["phone"]

    amount = request.form["amount"]

    response = stk_push(phone, amount)

    return render_template(
        "response.html",
        response=response
    )


if __name__ == "__main__":
    app.run(debug=True)