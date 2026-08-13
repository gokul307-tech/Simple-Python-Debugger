from flask import Flask, render_template, request

from analyzer import analyze_code
from suggestions import get_suggestion, get_explanation


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    code = ""

    if request.method == "POST":

        # Get code from the textarea
        code = request.form.get("code", "")

        # Remove unnecessary spaces at the beginning/end
        code = code.strip()

        # Check whether the user entered anything
        if not code:

            result = {
                "success": False,
                "type": "EmptyCode",
                "message": "No Python code was entered.",
                "line": None,
                "column": None,
                "code_line": "",
                "explanation":
                    "The debugger needs a Python program to analyze.",
                "suggestion":
                    "Enter some Python code and click Analyze Code."
            }

        else:

            # Analyze the Python program
            error = analyze_code(code)

            if error:

                # Get the line containing the error
                error_line = ""

                if error["line"]:

                    lines = code.splitlines()

                    if error["line"] <= len(lines):
                        error_line = lines[
                            error["line"] - 1
                        ]

                result = {
                    "success": False,
                    "type": error["type"],
                    "message": error["message"],
                    "line": error["line"],
                    "column": error["column"],
                    "code_line": error_line,
                    "explanation":
                        get_explanation(error["type"]),
                    "suggestion":
                        get_suggestion(error["type"])
                }

            else:

                # Code has no detected errors
                result = {
                    "success": True,
                    "message":
                        "No errors found in your Python program."
                }

    return render_template(
        "index.html",
        result=result,
        code=code
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )