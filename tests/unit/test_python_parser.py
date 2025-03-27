from llm_docgen.parsers.python_parser import parse_python_code

def test_function_extraction():
    code = """\
def add(a: int, b: int) -> int:
    \"\"\"Sum two numbers.\"\"\"
    return a + b
"""
    result = parse_python_code(code)
    assert len(result["functions"]) == 1
    assert result["functions"][0]["docstring"] == "Sum two numbers."