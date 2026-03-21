import traceback


def check_syntax(code):
    try:
        compile(code, "user_code.py", "exec")
        return None
    except SyntaxError as e:
        return {
            "type": "SyntaxError",
            "message": e.msg,
            "line": e.lineno
        }


def check_runtime(code):
    try:
        exec(code, {})
        return None
    except Exception as e:
        tb = traceback.extract_tb(e.__traceback__)
        line = tb[-1].lineno if tb else None

        return {
            "type": type(e).__name__,
            "message": str(e),
            "line": line
        }