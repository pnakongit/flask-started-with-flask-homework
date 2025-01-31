from flask import Flask

app = Flask(__name__)


@app.route("/hello-world")
def hello_world() -> str:
    return "<h1>Hello, World!</h1>"


if __name__ == "__main__":
    app.run()
