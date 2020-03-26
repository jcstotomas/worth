from flask import Flask, request
import randomize

app = Flask(__name__)

random_list = randomize.create_random_list("data.txt")


@app.route('/commodity', methods=["POST", "GET"])
def handle_commodity():
    # put logic here
    if request.method == "GET":
        comparison_list = randomize.run_pairs(random_list)
        return comparison_list

    elif request.method == "POST":
        return


if __name__ == "__main__":
    app.run()
