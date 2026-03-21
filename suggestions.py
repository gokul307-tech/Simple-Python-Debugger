SUGGESTIONS = {
    "SyntaxError": "Check for missing ':' or brackets.",
    "NameError": "Variable not defined.",
    "TypeError": "Wrong data types used.",
    "IndentationError": "Fix indentation.",
    "ZeroDivisionError": "Cannot divide by zero."
}


def smart_suggestion(error):
    etype = error["type"]
    msg = error["message"]

    suggestion = SUGGESTIONS.get(etype, "No suggestion available")

    if etype == "SyntaxError" and "expected ':'" in msg:
        suggestion = "Add ':' at the end of statements"

    return suggestion