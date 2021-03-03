from flask import Flask

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return """
        <html>
            <body>
                welcome
            </body>
        </html>"""


@app.route("/welcome/home")
def welcome_home():
    return """
        <html>
            <body>
                welcome home
            </body>
        </html>"""


@app.route("/welcome/back")
def welcome_back():
    return """
        <html>
            <body>
                welcome back
            </body>
        </html>"""
