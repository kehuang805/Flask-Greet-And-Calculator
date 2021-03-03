# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)


@app.route("/add")
def add():
    """Adds two numbers provided in query"""
    num1 = int(request.args.get("a"))
    num2 = int(request.args.get("b"))
    return f"""
        <html>
            <body>
                {operations.add(num1, num2)}
            </body>
        </html>   
        """


@app.route("/sub")
def subtracts():
    """Subtracts two numbers provided in query"""
    num1 = int(request.args.get("a"))
    num2 = int(request.args.get("b"))
    return f"""
        <html>
            <body>
                {operations.sub(num1,num2)}
            </body>
        </html>   
        """


@app.route("/mult")
def multiply():
    """Multiplies two numbers provided in query"""
    num1 = int(request.args.get("a"))
    num2 = int(request.args.get("b"))
    return f"""
        <html>
            <body>
                {operations.mult(num1,num2)}
            </body>
        </html>   
        """


@app.route("/div")
def divide():
    num1 = int(request.args.get("a"))
    num2 = int(request.args.get("b"))
    """Divides two numbers provided in query"""
    return f"""
        <html>
            <body>
                {operations.div(num1,num2)}
            </body>
        </html>   
        """
