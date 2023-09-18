#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Define the index route
@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"

# Define the print_string route
@app.route('/print/<string:param>')
def print_string(param):
    # Print the string to the console
    print(param)
    # Display the string in the web browser
    return f"<p>Printed: {param}</p>"

# Define the count route
@app.route('/count/<int:param>')
def count(param):
    # Generate a list of numbers in the range and join them with line breaks
    numbers = "\n".join(str(i) for i in range(param))
    return f"<pre>{numbers}</pre>"

# Define the math route
@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    # Perform the specified operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"

    return f"<p>Result: {result}</p>"

if __name__ == '__main__':
    app.run()