from flask import Flask, render_template, redirect, url_for, request
from flask.wrappers import Response

from fake_db import fake_db

app = Flask(__name__)


def get_id_for_create_todo() -> int:
    todo_id = 0
    if fake_db:
        todo_id = max([item["id"] for item in fake_db])
    return todo_id + 1


@app.route("/hello-world")
def hello_world() -> str:
    return "<h1>Hello, World!</h1>"


@app.route("/tasks", methods=["GET"])
def todo_list() -> str:
    return render_template("todo_list.html", todo_list=fake_db)


@app.route("/tasks/create", methods=["POST"])
def todo_create() -> Response:
    if request.method == "POST":
        new_task = {
            "id": get_id_for_create_todo(),
            "title": request.form["title"],
            "description": request.form["description"],
        }
        fake_db.append(new_task)
    return redirect(url_for("todo_list"))


@app.route("/tasks/<int:pk>/change_status", methods=["POST"])
def todo_change_status(pk: int) -> str:
    return ""


@app.route("/tasks/<int:pk>/delete", methods=["POST"])
def todo_delete(pk: int) -> str:
    return ""


if __name__ == "__main__":
    app.run()
