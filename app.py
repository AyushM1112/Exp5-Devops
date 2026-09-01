from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Experiment 5</title>
        </head>
        <body>
            <h1>Welcome to DevOps Experiment 5</h1>
            <p>Python Selenium Testing</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)