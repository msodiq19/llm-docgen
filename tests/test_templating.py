# tests/test_templating.py
from llm_docgen.templating.renderer import render_template
import pytest

def test_template_rendering():
    context = {"project_name": "Test", "classes": []}
    output = render_template("api.md.j2", context)
    assert "# Test Documentation" in output
    assert "## API Reference" in output

def test_invalid_template():
    context = {"project_name": "Test", "classes": []}
    with pytest.raises(ValueError):
        render_template("nonexistent_template.md.j2", context)

def test_missing_context():
    context = {"classes": []}
    with pytest.raises(ValueError):
        render_template("api.md.j2", context)