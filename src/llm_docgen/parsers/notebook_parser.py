import re
from nbformat import reads
from typing import List, Dict

EXAMPLE_REGEX = re.compile(
    r"# Example:\s*(.+?)\n(.*?)(?=\n#|$)", 
    re.DOTALL
)

def parse_notebook(notebook_path: str) -> List[Dict]:
    with open(notebook_path, "r") as f:
        nb = reads(f.read(), as_version=4)
    return process_cells(nb.cells)

def process_cells(cells) -> List[Dict]:
    return [
        extract_example(cell.source)
        for cell in cells
        if cell.cell_type == "code" and "# Example:" in cell.source
    ]

def extract_example(code: str) -> Dict:
    return [
        {"description": desc.strip(), "code": code.strip()}
        for desc, code in EXAMPLE_REGEX.findall(code)
    ]