import traceback


def check_syntax(code):
    """
    Check whether the Python code has syntax errors.
    """

    try:
        compile(code, "user_code.py", "exec")
        return None

    except SyntaxError as error:

        error_type = "SyntaxError"

        # IndentationError is a type of SyntaxError,
        # but we display it separately.
        if isinstance(error, IndentationError):
            error_type = "IndentationError"

        return {
            "type": error_type,
            "message": error.msg,
            "line": error.lineno,
            "column": error.offset
        }


def check_runtime(code):
    """
    Run the Python program and check for runtime errors.
    """

    try:
        # Execute the code.
        # __builtins__ is provided so normal Python functions
        # such as print(), len(), range(), etc. can work.
        exec(code, {"__builtins__": __builtins__})

        return None

    except Exception as error:

        # Get traceback information.
        traceback_info = traceback.extract_tb(
            error.__traceback__
        )

        line = None

        # Find the last line belonging to the user's program.
        for item in reversed(traceback_info):

            if item.filename == "user_code.py":
                line = item.lineno
                break

        return {
            "type": type(error).__name__,
            "message": str(error),
            "line": line,
            "column": None
        }


def analyze_code(code):
    """
    Perform complete analysis.

    First check syntax.
    If syntax is correct, check runtime errors.
    """

    # Step 1: Syntax checking
    syntax_error = check_syntax(code)

    if syntax_error:
        return syntax_error

    # Step 2: Runtime checking
    runtime_error = check_runtime(code)

    if runtime_error:
        return runtime_error

    # No errors
    return None