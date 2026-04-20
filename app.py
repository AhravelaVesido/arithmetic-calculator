from flask import Flask, render_template, request

app = Flask(__name__)


def calculate(num1, num2, operation):
    if operation == "addition":
        return (num1 + num2)
    elif operation == "subtraction":
        return (num1 - num2)
    elif operation == "multiplication":
        return (num1 * num2)
    elif operation == "division":
        if num2 == 0:
            raise ValueError("Can't divide with zero")
        return (num1 / num2)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]
            if not operation:
                error = "Please select an operation first!"
            else:
                result = calculate(num1, num2, operation)
        except ValueError as e:
            error = str(e)
    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
