SUGGESTIONS = {

    "SyntaxError":
        "Check for missing ':', brackets, quotes, commas, or incorrect Python syntax.",

    "IndentationError":
        "Check the indentation. Use consistent spaces, preferably 4 spaces.",

    "NameError":
        "Make sure the variable or function is defined before you use it.",

    "TypeError":
        "Check the data types. Make sure you are using compatible data types.",

    "ValueError":
        "Check the value you are using. It may not be in the required format.",

    "IndexError":
        "Check the list or tuple index. Make sure the index exists.",

    "KeyError":
        "Check the dictionary key. Make sure the key exists before accessing it.",

    "AttributeError":
        "Check the object and make sure the attribute or method name is correct.",

    "ZeroDivisionError":
        "You cannot divide by zero. Check the value of the divisor.",

    "FileNotFoundError":
        "Check the file name and path. Make sure the file exists.",

    "ModuleNotFoundError":
        "Check the module name and make sure the required module is installed.",

    "ImportError":
        "Check the imported function, class, or module name.",

    "UnboundLocalError":
        "Make sure the local variable gets a value before you use it.",

    "RecursionError":
        "Check the recursive function and make sure it has a proper stopping condition.",

    "OverflowError":
        "The calculated value is too large. Check the numbers used in the calculation.",

    "AssertionError":
        "The condition inside the assert statement is False."
}


EXPLANATIONS = {

    "SyntaxError":
        "Python could not understand the structure of your program.",

    "IndentationError":
        "Python found incorrect indentation in your program.",

    "NameError":
        "Python could not find the variable or function you are trying to use.",

    "TypeError":
        "The program is trying to perform an operation using incompatible data types.",

    "ValueError":
        "The data type is correct, but the value is not suitable for the operation.",

    "IndexError":
        "The program tried to access an index that does not exist.",

    "KeyError":
        "The program tried to access a dictionary key that does not exist.",

    "AttributeError":
        "The object does not have the attribute or method you are trying to use.",

    "ZeroDivisionError":
        "The program tried to divide a number by zero.",

    "FileNotFoundError":
        "Python could not find the requested file.",

    "ModuleNotFoundError":
        "Python could not find the requested Python module.",

    "ImportError":
        "Python could not import the requested item.",

    "UnboundLocalError":
        "A local variable was used before it was assigned a value.",

    "RecursionError":
        "The function called itself too many times.",

    "OverflowError":
        "A numerical calculation produced a value that is too large.",

    "AssertionError":
        "An assert condition evaluated to False."
}


def get_suggestion(error_type):
    """
    Get a suggestion based on the error type.
    """

    return SUGGESTIONS.get(
        error_type,
        "Check the reported line and the surrounding code."
    )


def get_explanation(error_type):
    """
    Get a simple explanation of the error.
    """

    return EXPLANATIONS.get(
        error_type,
        "Python found a problem while processing your program."
    )