

@api.route("/hello")
def handle_hello():
    response_body = {"Welcome message": "hello"}

    return jsonify(response_body), 200
