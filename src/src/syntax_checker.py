import ast

def check_syntax(code: str):
        """  
    Tries to analyze the code for syntax errors.  
    Returns a dictionary containing the analysis result.  
    """
    try:
        ast.parse(code)
        return {
            "error": False,
            "error_type": None,
            "line": None,
            "msg": None
        }
    except SyntaxError as e:
        return {
            "error": True,
            "error_type": e.__class__.__name__,
            "line": e.lineno,
            "msg": e.msg
        }
    except Exception as e:
        return {
            "error": True,
            "error_type": type(e).__name__,
            "line": None,
            "msg": str(e)
        }

