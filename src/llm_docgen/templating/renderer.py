from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

def render_template(template_name: str, context: dict) -> str:
    """Render a Jinja template with provided context."""
    # Path to package's templates directory
    template_dir = Path(__file__).parent.parent / "templates"
    
    # Configure Jinja environment
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True
    )
    
    # Validate template exists
    try:
        env.get_template(template_name)
    except TemplateNotFound:
        raise ValueError(f"Template {template_name} not found")
    
    # Validate required context variables
    required_vars = ["project_name"]
    for var in required_vars:
        if var not in context:
            raise ValueError(f"Missing required context variable: {var}")
    
    return env.get_template(template_name).render(context)