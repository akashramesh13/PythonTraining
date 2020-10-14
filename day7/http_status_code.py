from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def sayHello():
    return "Hello, User"


USERS = {}


@app.route("/add", methods=["POST"])
def add_user():
    user_id = int(request.form["id"])
    username = request.form["username"]
    USERS[user_id] = username
    print(type(user_id))
    return jsonify(id=user_id, name=USERS[user_id], USERS=USERS), 200


@app.route("/<int:user_id>", methods=["PUT", "GET", "DELETE"])
def update_user(user_id: int):
    if request.method == "GET":
        if user_id in USERS:
            return jsonify(id=user_id, name=USERS[user_id])
        else:
            return jsonify(message=f"User with {user_id} does not exist"), 404
    elif request.method == "PUT":
        if user_id not in USERS:
            return jsonify(message=f"User with id {user_id} does not exist"), 404
        else:
            user_name = request.form["username"]
            USERS[user_id] = user_name
            return jsonify(id=user_id, name=USERS[user_id]), 200
    elif request.method == "DELETE":
        if user_id not in USERS:
            return jsonify(message=f"User with id {user_id} does not exist")
        else:
            del USERS[user_id]
            return '', 204


if __name__ == "__main__":
    app.run(debug=True)
