from flask import Flask

app = Flask(__name__)


@app.route("/hello-world")
def hello_world() -> str:
    return "<h1>Hello, World!</h1>"


@app.route("/tasks", methods=["GET"])
def todo_list() -> str:
    return ""


@app.route("/tasks/create", methods=["POST"])
def todo_create() -> str:
    return ""


@app.route("/tasks/<int:pk>/change_status", methods=["POST"])
def todo_change_status(pk: int) -> str:
    return ""


@app.route("/tasks/<int:pk>/delete", methods=["POST"])
def todo_delete(pk: int) -> str:
    return ""


if __name__ == "__main__":
    app.run()
