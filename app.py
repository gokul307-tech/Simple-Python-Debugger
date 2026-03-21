from flask import Flask, render_template, request
import traceback

app = Flask(__name__)

# Suggestions
SUGGESTIONS = {
    "SyntaxError": "Check for missing ':' or brackets.",
    "NameError": "Variable not defined.",
    "TypeError": "Wrong data types used.",
    "IndentationError": "Fix indentation.",
    "ZeroDivisionError": "Cannot divide by zero."
}


def check_code(code):
    try:
        compile(code, "user_code.py", "exec")
        exec(code, {})
        return None
    except SyntaxError as e:
        return {
            "type": "SyntaxError",
            "message": e.msg,
            "line": e.lineno
        }
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        line = tb[-1].lineno if tb else None

        return {
            "type": type(e).__name__,
            "message": str(e),
            "line": line
        }


def get_suggestion(error):
    etype = error["type"]
    msg = error["message"]

    suggestion = SUGGESTIONS.get(etype, "Check your code")

    if etype == "SyntaxError" and "expected ':'" in msg:
        suggestion = "Add ':' at the end of if/for/while"

    if etype == "NameError":
        suggestion = "Define the variable before using it"

    return suggestion


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    code = ""
    error_line = ""

    if request.method == "POST":
        code = request.form.get("code", "")

        error = check_code(code)

        if error:
            lines = code.split("\n")
            if error["line"] and error["line"] <= len(lines):
                error_line = lines[error["line"] - 1]

            result = {
                "type": error["type"],
                "message": error["message"],
                "line": error["line"],
                "code_line": error_line,
                "suggestion": get_suggestion(error)
            }
        else:
            result = {"success": "No errors found!"}

    return render_template("index.html", result=result, code=code)


if __name__ == "__main__":
    app.run(debug=True)