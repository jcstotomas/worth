from flask import Flask

app = Flask(__name__)

@app.route('/commodity', methods=["POST", "GET"])
def handle_commodity():
    # put logic here
    pass