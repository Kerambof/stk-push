from flask import Flask, render_template, request, jsonify

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


@app.route("/mpesa/callback", methods=["POST"])
def mpesa_callback():

    data = request.get_json()

    print("=" * 60)
    print("CALLBACK RECEIVED")
    print(data)
    print("=" * 60)

    return jsonify({
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    })


if __name__ == "__main__":
    app.run(debug=True)