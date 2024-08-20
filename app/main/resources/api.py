@api.route("/hi")
def handle_hello():
    response_body = {"message": "Hi"}

    return jsonify(response_body), 200
