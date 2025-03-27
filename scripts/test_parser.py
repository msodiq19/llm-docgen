from src.llm_docgen.parsers.python_parser import parse_python_code

code = """\
def add(a: int, b: int) -> int:
    \"\"\"Sum two numbers.\"\"\"
    return a + b

class Calculator:
    \"\"\"A simple calculator class.\"\"\"
    def multiply(self, x: int, y: int) -> int:
        \"\"\"Multiply two numbers.\"\"\"
        return x * y
"""

result = parse_python_code(code)
print(result) 